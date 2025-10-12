# ManuWorks Manufacturing Chatbot (with Memory)

## Overview

This is a **Streamlit-based chatbot** designed for manufacturing operations. It helps factory operators, supervisors, and suppliers ask questions about production targets, completed units, and remaining work. The chatbot **remembers the conversation context** using LangChain memory so follow-up questions are answered accurately.

The bot provides **structured answers** for common queries and can also generate natural language responses using **Gemini Pro** via Google AI Studio.

---
## Screenshots
![alt text](<Screenshot 2025-10-03 181255.png>)
---

## Features

* Chatbot with **memory** to track conversation context.
* Handles **production queries** like target, completed units, and remaining units.
* **Clean and professional UI** using Streamlit chat messages.
* **Input box clears automatically** after each question.
* Structured answers can be **comma-separated** for readability.
* Hardcoded synthetic **factory data** for demonstration.

---

## Requirements

* Python 3.10+
* Packages listed in `requirements.txt`:

```text
streamlit
langchain
google-generativeai
langchain-google-genai
python-dotenv
```

---

## Setup

1. **Create and activate a virtual environment:**

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file** with your Google API key:

```text
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE
```

---

## Running the Chatbot

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`) to interact with the chatbot.

---

## Usage

* Type your question in the input box (e.g., “What is today’s production target?”).
* Press **Enter** to submit.
* The bot will respond and the input box will clear for the next question.
* Ask follow-up questions; the bot remembers prior conversation.

**Examples:**

* “What are today’s targets?”
  Output: `Line A: 500 automotive shafts, Line B: 300 engine blocks, Line C: 400 gear assemblies, Line D: 350 brake discs`

* “How many units are completed so far?”
  Output: `Line A: 320 completed, Line B: 280 completed, Line C: 150 completed, Line D: 340 completed`

* “How many are remaining?”
  Output: `Line A: 180 remaining, Line B: 20 remaining, Line C: 250 remaining, Line D: 10 remaining`

---

## Notes

* The chatbot uses **hardcoded factory data** for demonstration. In production, this can be replaced with **live database or API queries**.
* Memory is handled via LangChain’s `ConversationBufferMemory`.
* Gemini Pro (via Google AI Studio) is used for **fallback natural language responses**.

---
