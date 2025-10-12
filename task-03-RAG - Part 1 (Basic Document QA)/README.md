# 📄 RAG-based Document QA with Google Gemini

This project implements a **Retrieval-Augmented Generation (RAG) system** that allows you to ask questions over PDFs, such as SOPs, machine manuals, or ISO standards, using **Google Gemini Pro** models and **FAISS** for vector search. The system is built using **LangChain** and provides a simple **Streamlit UI**.

---

## Features

* Load and split PDF documents into chunks.
* Generate embeddings using HuggingFace `all-MiniLM-L6-v2`.
* Store embeddings in a **FAISS vector index** for efficient retrieval.
* Use **Google Gemini Pro** to answer user questions based on document context.
* Streamlit interface with:

  * Input field for questions.
  * Display of answers.
  * Expandable source documents for reference.
* Cached vectorstore for faster repeated queries.

---
## Screenshots
![alt text](<Screenshot 2025-10-03 183959.png>)
---
## Folder Structure

```
Task 3 RAG - Part 1 (Basic Document QA)/
│
├── app.py                     # Streamlit app entry point
├── configs/
│   └── settings.yaml          # Configuration for PDF path, index path, model, etc.
├── data/
│   └── SOP_Hazardous_Processes.pdf  # Example PDF
├── index/                     # FAISS index folder
├── src/
│   ├── config.py              # Load YAML config
│   ├── loader.py              # PDF loading and splitting
│   ├── embedder.py            # FAISS index creation/loading
│   ├── retriever.py           # Vectorstore -> retriever
│   └── qa_system.py           # Gemini Pro LLM wrapper + RetrievalQA chain
├── vectorstore.pkl            # Optional cached vectorstore
└── requirements.txt           # Required Python packages
```

---

## Configuration

Edit `configs/settings.yaml` to customize:

```yaml
pdf_path: "data/SOP_Hazardous_Processes.pdf"
index_path: "index/sop_faiss_index"
chunk_size: 500
chunk_overlap: 100
retrieval_k: 3
llm_model: "gemini-2.5-flash"
```

* `pdf_path`: Path to your PDF document.
* `index_path`: Directory where FAISS index is stored.
* `chunk_size` & `chunk_overlap`: Text splitting parameters.
* `retrieval_k`: Number of documents to retrieve for each query.
* `llm_model`: Google Gemini Pro model to use.

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Enter your question in the input field.
* The system will display:

  * The generated **answer**.
  * Expandable **source documents** used for retrieval.

⚡ **Note:** The first run may take longer as PDFs are loaded, split, and indexed. Subsequent queries will be faster thanks to caching.

---

## Dependencies

Key Python packages used:

* `streamlit`
* `langchain`
* `langchain_community`
* `faiss-cpu`
* `sentence-transformers`
* `transformers`
* `pypdf`
* `pyyaml`
* `google-generativeai`
* `tqdm`

---

## Notes

* The system currently supports **single PDF documents**, but you can extend it to multiple PDFs by loading a list in `loader.py`.
* FAISS index caching ensures the system **does not recompute embeddings** on every query.
* Gemini Pro LLM wrapper is fully compatible with **LangChain RetrievalQA**.

---