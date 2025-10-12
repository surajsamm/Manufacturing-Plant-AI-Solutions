import os
import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from tools.efficiency import calculate_efficiency
from tools.downtime import estimate_downtime_cost
from tools.inventory import check_reorder
from tools.api_tools import get_stock_price, get_weather
from prompts.prompts import AGENT_PROMPT
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key = os.getenv("GEMINI_API_KEY"), temperature=0)

db_path = "chat_memory.db"
    
print(f"DB Path = {db_path}")
conn = sqlite3.connect(db_path, check_same_thread=False)


# ----- Efficiency Tool -----
def efficiency_query_tool(units_produced: int, target_units: int) -> str:
    """
    Calculate production efficiency based on units produced vs target units.
    
    Inputs:
        units_produced (int): Actual units produced.
        target_units (int): Planned target units.
    Output:
        str: Efficiency percentage with explanation.
    """
    try:
        result = calculate_efficiency(units_produced, target_units)
        return result
    except Exception as e:
        return f"Error calculating efficiency: {str(e)}"

# ----- Downtime Tool -----
def downtime_cost_tool(hours: float, cost_per_hour: float) -> str:
    """
    Estimate downtime cost based on hours and hourly cost.
    
    Inputs:
        hours (float): Downtime duration in hours.
        cost_per_hour (float): Cost per hour of downtime.
    Output:
        str: Total downtime cost formatted as currency.
    """
    try:
        result = estimate_downtime_cost(hours, cost_per_hour)
        return result
    except Exception as e:
        return f"Error calculating downtime cost: {str(e)}"

# ----- Inventory Tool -----
def inventory_check_tool(daily_demand: int, lead_time: int, safety_stock: int, current_stock: int) -> str:
    """
    Check if inventory needs reordering.
    
    Inputs:
        daily_demand (int): Units consumed per day.
        lead_time (int): Lead time in days.
        safety_stock (int): Buffer stock units.
        current_stock (int): Current inventory level.
    Output:
        str: Recommendation whether to reorder or not.
    """
    try:
        result = check_reorder(daily_demand, lead_time, safety_stock, current_stock)
        return result
    except Exception as e:
        return f"Error checking inventory: {str(e)}"

# ----- Stock API Tool -----
def stock_price_tool(ticker: str) -> str:
    """
    Fetch the current stock price for a given ticker.
    
    Inputs:
        ticker (str): Stock symbol (e.g., TSLA)
    Output:
        str: Current stock price or error message.
    """
    try:
        result = get_stock_price(ticker)
        return result
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"

# ----- Weather API Tool -----
def weather_tool(city: str) -> str:
    """
    Fetch the current weather for a given city.
    
    Inputs:
        city (str): City name (e.g., Berlin)
    Output:
        str: Weather description and temperature or error message.
    """
    try:
        result = get_weather(city)
        return result
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"


tools = [efficiency_query_tool, downtime_cost_tool, inventory_check_tool, stock_price_tool, weather_tool]
llm_with_tools = llm.bind_tools(tools)

State = MessagesState

# System message
sys_msg = SystemMessage(
    content= AGENT_PROMPT
)
# Node
def assistant(state: State):
    print("Assistant node started!!")
    messages = [sys_msg] + state["messages"]
    # print(state["messages"])
    # for m in messages:
    #     m.pretty_print()
    return {"messages": state["messages"] + [llm_with_tools.invoke(messages)]}

# Graph
builder = StateGraph(State)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
# builder.add_node(summarize_conversation)

# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
# builder.add_edge("tools", "assistant")
builder.add_edge("tools", "assistant")
builder.add_edge("assistant", END)
memory = SqliteSaver(conn)
react_graph = builder.compile(checkpointer=memory)
# react_graph = builder.compile()