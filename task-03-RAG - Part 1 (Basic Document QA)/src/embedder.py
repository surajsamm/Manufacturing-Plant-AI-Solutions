from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

def create_or_load_index(docs, index_path: str = "index/sop_faiss_index"):
    """
    Create FAISS index from documents or load existing one.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    if os.path.exists(index_path):
        print("Loading existing FAISS index...")
        return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(index_path)
    print("FAISS index created!")
    return vectorstore
