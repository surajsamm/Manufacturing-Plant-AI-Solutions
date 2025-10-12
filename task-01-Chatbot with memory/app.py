import os
from dotenv import load_dotenv
import streamlit as st

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------------------
# 1. Load API Key
# ---------------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.warning("No GOOGLE_API_KEY found in .env!")

# ---------------------------
# 2. Hardcoded factory data
# ---------------------------
factory_data = {
    "Line A": {"product": "automotive shafts", "target": 500, "completed": 320},
    "Line B": {"product": "engine blocks", "target": 300, "completed": 280},
    "Line C": {"product": "gear assemblies", "target": 400, "completed": 150},
    "Line D": {"product": "brake discs", "target": 350, "completed": 340},
}

# ---------------------------
# 3. Initialize LLM
# ---------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

# ---------------------------
# 4. Prompt Template and Memory
# ---------------------------
system_prompt = """
You are ManuWorks Operations Assistant, an AI chatbot with memory.
You provide concise and professional answers to factory operators, supervisors, or suppliers.
Use the factory data provided. Keep answers factual and operational.
"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=f"{system_prompt}\n\n{{history}}\nOperator: {{input}}\nBot:"
)

memory = ConversationBufferMemory(return_messages=True)
chat_chain = ConversationChain(llm=llm, memory=memory, prompt=prompt, verbose=False)

# ---------------------------
# 5. Streamlit UI
# ---------------------------
st.set_page_config(page_title="⚙️ ManuWorks Chatbot", page_icon="⚙️", layout="wide")
st.title("⚙️ ManuWorks Manufacturing Chatbot")

# Initialize session state for conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ---------------------------
# 6. Structured Response Function
# ---------------------------
def structured_response(query: str):
    q_lower = query.lower()
    if "target" in q_lower:
        return ", ".join(
            [f"{line}: {factory_data[line]['target']} {factory_data[line]['product']}" 
             for line in factory_data]
        )
    elif "completed" in q_lower or "done" in q_lower:
        return ", ".join(
            [f"{line}: {factory_data[line]['completed']} completed" for line in factory_data]
        )
    elif "remaining" in q_lower or "left" in q_lower:
        return ", ".join(
            [f"{line}: {factory_data[line]['target'] - factory_data[line]['completed']} remaining"
             for line in factory_data]
        )
    return None


# ---------------------------
# 7. Callback to handle input submission
# ---------------------------
def handle_input():
    query = st.session_state.user_input
    if query:
        response = structured_response(query)
        if not response:
            response = chat_chain.run(query)
        st.session_state.conversation.append(("Operator", query))
        st.session_state.conversation.append(("Bot", response))
        st.session_state.user_input = ""  # clears the input safely

# ---------------------------
# 8. Input box with callback
# ---------------------------
st.text_input("Type your question here...", key="user_input", on_change=handle_input)

# ---------------------------
# 9. Display chat
# ---------------------------
for role, msg in st.session_state.conversation:
    if role == "Operator":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)
