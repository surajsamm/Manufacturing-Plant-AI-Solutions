
# Task 03: RAG - Part 2 (Memory + Multi-step Retrieval)
<img width="718" height="504" alt="image" src="https://github.com/user-attachments/assets/fcdde9ca-33ac-4f37-8d20-70e767f34b1c" />

## Objective
Enable deeper **Q&A with memory** and **multi-turn dialogue** for manufacturing documents, ISO standards, and safety SOPs with **advanced conversational capabilities**.

---

## Tech Stack

- **Groq API** with LLaMA models (`llama-3.3-70b-versatile` + `llama-3.1-8b-instant`)  
- **LangChain** for memory management, retrieval chains, and document processing  
- **FAISS** for vector storage and similarity search  
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`)  
- **Gradio** for enhanced web interface  
- **PyPDFLoader** for PDF document processing  
- **Python 3.11+**  

---

## Key Features

### **Conversational Memory System**
- **ConversationBufferMemory:** Maintains complete chat history across sessions  
- **Context Retention:** Remembers previous questions and answers  
- **Multi-turn Dialogue:** Enables natural follow-up conversations  

### **Multi-Query Retrieval**
- **Intelligent Query Expansion:** Uses MultiQueryRetriever to generate multiple query variations  
- **Enhanced Context:** Retrieves 4 most relevant document chunks  
- **Better Coverage:** Diverse query perspectives improve answer quality  

### **Dual-Model Architecture**
- **Fast Retrieval:** `llama-3.1-8b-instant` for quick query processing  
- **Quality Responses:** `llama-3.3-70b-versatile` for detailed, accurate answers  
- **Optimized Performance:** Balanced speed and response quality  

### **Advanced Document Processing**
- **Smart Chunking:** 1000-character chunks with 100-character overlap  
- **FAISS Vector Store:** Fast local similarity searches  
- **Source Tracking:** Shows document sources and page numbers  

### **Manufacturing-Focused Design**
- **Custom Prompts:** Specialized for technical documentation  
- **Comparative Analysis:** Supports "compare X with Y" queries  
- **Standards Awareness:** Understands ISO standards and safety protocols  

---

## Example Usage

```python
from langchain.chains import ConversationalRetrievalChain

# Load PDF documents, split into chunks, create vector embeddings, FAISS store
# Initialize memory-enabled RAG chain with Groq LLaMA
query = "Compare maintenance procedures for Machine A and Machine B"
answer, sources = memory_rag_chain.run(query)
print(f"Answer: {answer}")
print(f"Sources: {sources}")
