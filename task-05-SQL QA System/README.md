# Task 5: SQL QA System (Clients & Investments)
<img width="718" height="504" alt="image" src="https://github.com/user-attachments/assets/73055d63-3cd4-40a2-ad32-078e8aff0875" />



## Objective
Create a natural language SQL query system for finance data. Users can ask questions in plain English, and the system will:

1. Generate SQL queries from the questions.
2. Execute them on a SQLite database.
3. Return raw results (or optionally summarize using Groq LLaMA).

---

## Folder Structure

task-05-sql-qa/
│
├── task5_sql_qa.ipynb       # Main notebook with SQL QA system
├── finance.db               # SQLite database (clients + investments)
├── query_summaries/         # Folder to store query results
└── README.md                # Project documentation

## Setup Instructions

1. **Install dependencies**  

pip install groq langchain pandas 


Set your Groq API key in the notebook:

from groq import Groq
api_key = "YOUR_GROQ_API_KEY"
client = Groq(api_key=api_key)


## Run the notebook to:

Create clients and investments tables.

Insert 30+ sample clients and investments.

Ask natural language questions and generate SQL queries.

Execute queries and optionally save results in query_summaries/.

## How It Works

**Natural Language → SQL**

generate_sql(question) uses Groq LLaMA to convert English questions to SQL.

**Execute SQL**

execute_sql(cursor, sql) runs the query on the SQLite database and returns raw rows.

**Optional Saving**

Query results are saved into the query_summaries/ folder as text files:

query_1_results.txt
query_2_results.txt
...
<img width="710" height="483" alt="image" src="https://github.com/user-attachments/assets/fcdde9ca-33ac-4f37-8d20-70e767f34b1c" />


**Example Usage**
questions = [
    "List clients with portfolio value over 50 lakh.",
    "Show investments in 'Alpha Fund' over 1 lakh."
]

for idx, q in enumerate(questions, 1):
    sql_query = generate_sql(q)
    results = execute_sql(cursor, sql_query)
    print(f"Question {idx}: {q}")
    print(f"SQL: {sql_query}")
    print(f"Results: {results}")

**Notes**

Works with SQLite, but can be adapted for MySQL/PostgreSQL.

Groq summarization is optional for manager-friendly reports.

All query outputs are stored in query_summaries/ for easy reference.
