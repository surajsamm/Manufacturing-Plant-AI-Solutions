# Task 03: RAG - Part 1 (Basic Document QA)
<img width="718" height="504" alt="image" src="https://github.com/user-attachments/assets/fcdde9ca-33ac-4f37-8d20-70e767f34b1c" />

## Objective
Enable **Q&A over machine manuals, ISO standards, and safety SOPs** using **Retrieval-Augmented Generation (RAG)** with Groq's LLaMA models.

---

## Tech Stack

- **Groq API** with LLaMA model (`llama-3.3-70b-versatile`)  
- **LangChain** for document processing and retrieval chains  
- **FAISS** for vector storage and similarity search  
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`)  
- **Gradio** for web interface  
- **PyPDFLoader** for PDF document processing  
- **Python 3.11+**  

---

## Key Features

### **Document Processing Pipeline**
- **PDF Loading:** Uses PyPDFLoader to extract text from PDF documents  
- **Smart Chunking:** 1000-character chunks with 100-character overlap using RecursiveCharacterTextSplitter  
- **Vector Embeddings:** Converts text to vectors using HuggingFace's `all-MiniLM-L6-v2` model  

### **Vector Storage & Retrieval**
- **FAISS Vector Store:** Local vector database for fast similarity searches  
- **Semantic Search:** Retrieves 3 most relevant document chunks for each query  
- **Efficient Storage:** Saves vector index locally for reuse  

### **RAG Chain Implementation**
- **RetrievalQA Chain:** Combines document retrieval with LLM generation  
- **Custom Prompts:** Manufacturing-focused prompt templates  
- **Context-Aware Answers:** Provides answers based on document content  

### **User Interface**
- **Gradio Web App:** Simple and intuitive chat interface  
- **Real-time Q&A:** Instant answers based on uploaded documents  
- **Error Handling:** Robust error management for smooth user experience  

---

## Example Usage

```python
from langchain.chains import RetrievalQA

# Load PDF documents, split into chunks, create vector embeddings, FAISS store
# Initialize RAG chain with Groq LLaMA
# Example query:
query = "What are the safety procedures for Machine X?"
answer, sources = rag_chain.run(query)
print(f"Answer: {answer}")
print(f"Sources: {sources}")
