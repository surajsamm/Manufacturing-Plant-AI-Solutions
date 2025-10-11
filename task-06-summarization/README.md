# Task 06: Summarization Engine

## 📌 Objective
Summarize large operational and compliance documents (e.g., safety audits, maintenance logs, compliance reviews) into concise, actionable summaries.

---

## ⚙️ Tech Stack
- **Groq API** with LLaMA model (`llama-3.3-70b-versatile`)
- **LangChain** for text splitting and summarization chaining
- **PyPDFLoader / TextLoader** for loading PDF or text documents
- **Python 3.10+**  

---

## 🛠 Key Features
1. **Summarization Chains**
   - Uses **MapReduce-style summarization**:
     - **Map**: Split large documents into chunks and summarize each chunk individually.
     - **Reduce**: Combine chunk summaries into a final coherent summary.
   - This method ensures:
     - No loss of context in long documents
     - Faster processing and reliable summaries
   - Optional: Can use **Refine chains** for iterative improvement of summaries (not implemented in this script but supported by LangChain).

2. **Chunking Mechanism**
   - Large documents are split into smaller **chunks** (e.g., 2000 characters with 200-character overlap) using **LangChain’s `RecursiveCharacterTextSplitter`**.

<img width="353" height="289" alt="image" src="https://github.com/user-attachments/assets/415a1cc5-6df2-41a2-84d7-c8c88d932db8" />

   - **Overlap** ensures continuity between chunks so context isn’t lost between sections.
   - Each chunk is summarized individually by the Groq LLaMA model and then combined.

4. **Supported Document Types**

   <img width="982" height="130" alt="image" src="https://github.com/user-attachments/assets/0a4df681-53be-4cae-bdb3-e1f2bb45c2a6" />

   - PDF (`.pdf`)
   - Text (`.txt`)

5. **Output**
   - Summaries are combined into a single file: `final_summary.txt`
   - Prints a preview of the summary in console.
     
<img width="765" height="366" alt="image" src="https://github.com/user-attachments/assets/77aef02e-1cbb-4145-911c-6b7cc9930b69" />

<img width="1493" height="746" alt="image" src="https://github.com/user-attachments/assets/a45d6889-7681-48bb-860b-72687f4c9c58" />

---

## 🏃 How to Run
1. Place your documents in the `sample_documents/` folder.
2. Set your **Groq API key** in the script:
   ```python
   api_key = "your_api_key_here"
