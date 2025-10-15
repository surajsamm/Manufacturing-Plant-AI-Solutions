# 🏭 Manufacturing Chatbot with Memory

<img width="1920" height="988" alt="image" src="https://github.com/user-attachments/assets/9cf6e336-1e2a-4dc5-958a-8b1213b013ed" />


## Overview
This project implements a **manufacturing assistant chatbot** that can handle queries from operators, supervisors, and suppliers. The bot remembers previous conversations using **LangChain's `ConversationBufferMemory`** and logs all chat exchanges in a **JSON file** for persistent records. The chatbot is powered by **Groq LLaMA 3.1 8B Instant** model and uses **Gradio** for an interactive web interface.

---

## Features

- **Context-Aware Responses:** The chatbot remembers conversation history and gives relevant answers.
- **Memory Logging:** Each user-bot interaction is automatically saved in `sample_conversations.json`.
- **Interactive UI:** Users can interact with the chatbot via Gradio interface.
- **Manufacturing Focus:** Provides assistance with production targets, maintenance schedules, and operations updates.

---

## Tech Stack

- **LLM:** Groq (`llama-3.1-8b-instant`)
- **Framework:** LangChain
- **Memory Management:** ConversationBufferMemory
- **UI:** Gradio
- **Data Logging:** JSON (`sample_conversations.json`)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <repo-folder>
