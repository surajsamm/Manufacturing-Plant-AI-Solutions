def get_retriever(vectorstore, k: int = 3):
    """
    Convert FAISS vectorstore into retriever.
    """
    return vectorstore.as_retriever(search_kwargs={"k": k})
