import streamlit as st
import uuid
from agent import react_graph
from langchain_core.messages import HumanMessage

# --- Page Setup ---
st.set_page_config(
    page_title="AI Agent Factory",
    page_icon="🤖",
    layout="centered",
)

st.markdown("<h1 style='text-align: center;'>🤖 AI Agent Factory</h1>", unsafe_allow_html=True)
st.caption("Ask me about **efficiency, downtime, inventory, stocks, or weather**")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🗑️ Clear Conversation"):
        st.session_state["messages"] = []
        st.session_state["thread_id"] = str(uuid.uuid4())
        st.rerun()
    st.markdown("---")
    st.markdown("Built with [LangGraph](https://docs.langgraph.io/) + Streamlit")

# --- Display Chat History ---
max_messages = 50  # limit for performance
for msg in st.session_state["messages"][-max_messages:]:
    role = msg.get("role", "user")
    content = msg.get("content", "")
    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").markdown(content)

# --- Input Box ---
user_input = st.chat_input("Type your question here...")
if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Show spinner while agent is processing
    with st.spinner("🤖 Agent is thinking..."):
        inputs = {"messages": [HumanMessage(content=user_input)]}
        result = react_graph.invoke(
            inputs,
            config={"configurable": {"thread_id": st.session_state["thread_id"]}}
        )

    # Extract assistant reply
    last_msg = result["messages"][-1].content
    reasoning = None
    final_answer = last_msg

    if "Final Answer:" in last_msg:
        parts = last_msg.split("Final Answer:")
        reasoning = parts[0].strip()
        final_answer = parts[1].strip()

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(f"{final_answer}")
        if reasoning:
            with st.expander("🔍 See reasoning steps"):
                st.text(reasoning)

    # Save assistant message
    st.session_state["messages"].append({"role": "assistant", "content": final_answer})
