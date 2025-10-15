# Multi-Step AI Agent with Groq, LangChain & LangGraph

This project demonstrates building a **multi-step AI agent** capable of performing calculations, fetching external data, and reasoning over structured tasks using **Groq LLM**, **LangChain**, and **LangGraph** in Python.

---

## **Features**

- Calculate **production efficiency**.
- Perform **multi-step Python calculations** using a REPL tool.
- Fetch external data via **HTTP requests**.
- ReAct-style agent integration with **tool selection**.
- Structured JSON outputs for easy parsing.

---

## **Tech Stack**

- Python 3.11+
- [LangChain](https://python.langchain.com)
- [LangChain-Groq](https://pypi.org/project/langchain-groq/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- Groq LLM (`llama-3.1-8b-instant`)
- Requests / HTTP APIs

---

## **Installation**

```bash
pip install langchain langchain-groq langgraph requests langchain-experimental==0.3.5rc1
