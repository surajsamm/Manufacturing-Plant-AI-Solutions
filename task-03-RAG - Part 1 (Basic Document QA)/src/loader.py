from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split(pdf_path: str, chunk_size: int = 500, overlap: int = 100):
    """
    Load PDF and split into smaller chunks.
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    print("Documents loaded and split!")
    return splitter.split_documents(documents)
