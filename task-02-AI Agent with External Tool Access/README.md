# 🤖 AI Agent Factory

**AI Agent Factory** is a Streamlit-based web application that leverages **LangGraph** and **Gemini LLM** to help businesses calculate **production efficiency**, estimate **downtime costs**, manage **inventory reordering**, and fetch **external data** like stock prices and weather. The agent uses a **ReAct-style reasoning approach** to dynamically choose tools and provide multi-step answers.

---
## Screenshots
![alt text](<Screenshot 2025-10-03 121404.png>)

![alt text](<Screenshot 2025-10-03 121552.png>)
---
## 🚀 Features

* **Production Efficiency Calculation**
  Calculate efficiency based on actual vs target units produced.

* **Downtime Cost Estimation**
  Estimate financial impact of production downtime.

* **Inventory Reorder Check**
  Determine if inventory needs replenishing based on demand, lead time, and safety stock.

* **Stock Price Lookup**
  Fetch real-time stock prices using the Alpha Vantage API (or mocked if API key is missing).

* **Weather Data Lookup**
  Fetch current weather for a given city via OpenWeather API (or mocked if API key is missing).

* **Multi-Step Reasoning**
  Supports queries that combine multiple tools, e.g., efficiency + downtime cost.

* **Persistent Chat Memory**
  Stores conversation history using SQLite (`chat_memory.db`) for each user session.

* **Professional Streamlit UI**
  Clean chat interface with collapsible reasoning, sidebar controls, and responsive design.

---

## ⚙️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Open your browser at `http://localhost:8501`.

* Type queries in the input box like:

  * `"Line A produced 450 units instead of 500, what’s the efficiency?"`
  * `"Do I need to reorder inventory if daily demand is 100, lead time 5 days, safety stock 200, and current stock is 650?"`
  * `"What’s Tesla’s stock price and the weather in Berlin?"`

* Use the **sidebar** to:

  * Clear conversation
  * View project info

* Advanced users can expand **reasoning steps** to see the ReAct chain (`Thought → Action → Observation → Final Answer`).

---

## 📂 Project Structure

```
ai-agent-factory/
│
├─ agent.py              # LangGraph agent setup & tool bindings
├─ app.py                # Streamlit front-end interface
├─ prompts/
│   └─ prompts.py        # AGENT_PROMPT with tool instructions
├─ tools/
│   ├─ efficiency.py     # Production efficiency calculator
│   ├─ downtime.py       # Downtime cost estimator
│   ├─ inventory.py      # Inventory reorder checker
│   └─ api_tools.py      # Stock price & weather API tools
├─ chat_memory.db        # SQLite database for persistent memory
├─ requirements.txt      # Python dependencies
└─ README.md             # Project documentation
```

---

## 🎯 Example Queries

* Inventory: `"Do I need to reorder inventory if daily demand is 100, lead time is 5 days, safety stock 200, current stock 650?"`
* Efficiency: `"Line A produced 450 units instead of 500, what’s the efficiency?"`
* Downtime: `"If downtime is 2 hours at $2000/hr, what’s the total cost?"`
* Multi-tool: `"Line A produced 450 units instead of 500. What’s the efficiency and cost impact if downtime was 2 hours at $1500/hr?"`
* External Data: `"What is Tesla's stock price and the weather in New York?"`

---

## ⚡ Tech Stack

* **Python 3.10+**
* **Streamlit** – Interactive web app
* **LangGraph** – Orchestrates LLM + tool reasoning
* **Google Gemini LLM** – AI reasoning engine
* **SQLite** – Persistent memory for conversations
* **Requests** – Fetch data from APIs

---

## 💡 Notes

* If no API keys are provided, the agent returns **mocked responses** for stock prices and weather.
* Lead time for inventory calculations must be provided in **days**, not minutes.
* Long conversations are capped at the last 50 messages in the UI for performance.

---

## 📌 Future Improvements

* Add **chat bubble styling** with colors for user vs assistant.
* Token-by-token streaming of LLM responses for smoother UX.
* Dark/light theme toggle.
* Web deployment with **FastAPI + Streamlit for multi-user access**.

---

