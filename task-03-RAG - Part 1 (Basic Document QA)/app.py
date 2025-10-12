import streamlit as st
from src.config import load_config
from src.loader import load_and_split
from src.embedder import create_or_load_index
from src.retriever import get_retriever
from src.qa_system import build_qa_chain
import os
import pickle

# ----------------------
# Page config
# ----------------------
st.set_page_config(page_title="📄 Document QA with Gemini", layout="wide")

# ----------------------
# Load Config
# ----------------------
config = load_config("configs/settings.yaml")
VECTORSTORE_PATH = "vectorstore.pkl"

# ----------------------
# Cache vector store
# ----------------------
@st.cache_resource(show_spinner="🔎 Loading and indexing documents...")
def get_vectorstore():
    if os.path.exists(VECTORSTORE_PATH):
        with open(VECTORSTORE_PATH, "rb") as f:
            vectorstore = pickle.load(f)
    else:
        docs = load_and_split(config["pdf_path"], config["chunk_size"], config["chunk_overlap"])
        vectorstore = create_or_load_index(docs, config["index_path"])
        with open(VECTORSTORE_PATH, "wb") as f:
            pickle.dump(vectorstore, f)
    return vectorstore

# Build retriever from cached vectorstore
vectorstore = get_vectorstore()
retriever = get_retriever(vectorstore, config["retrieval_k"])

# ----------------------
# Build QA Chain (Gemini)
# ----------------------
qa_chain = build_qa_chain(retriever, config["llm_model"])

# ----------------------
# Streamlit UI
# ----------------------
st.title("📄 RAG-powered Document QA")
st.write("Ask questions about your PDF documents using **Google Gemini Pro**!")

query = st.text_input("💬 Enter your question:")

if query:
    with st.spinner("🤔 Thinking..."):
        result = qa_chain.invoke({"query": query})

    st.subheader("✅ Answer")
    st.write(result["result"])

    with st.expander("📚 Sources"):
        for doc in result["source_documents"]:
            st.markdown(f"- **Source**: {doc.metadata.get('source', 'Unknown')}")
            st.write(doc.page_content[:400] + "...")
