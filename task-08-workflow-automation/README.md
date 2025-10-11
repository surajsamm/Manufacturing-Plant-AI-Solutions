# Task 08: Workflow Automation with n8n

<img width="1048" height="434" alt="image" src="https://github.com/user-attachments/assets/951e41c4-0996-4353-9ed1-8e79aa20ae9d" />

<img width="1159" height="564" alt="image" src="https://github.com/user-attachments/assets/738b05e0-68a8-400b-960f-93b0a8f1bc36" />

<img width="1352" height="641" alt="image" src="https://github.com/user-attachments/assets/141a5cce-9cbf-4dbf-b66c-d290f03b020b" />



## 📌 Objective
Automate operational alerts, supplier communications, and QA logging using **n8n** workflows. The workflow integrates outputs from LangChain pipelines via webhooks.

---

## ⚙️ Tech Stack / Tools
- **n8n.io** (cloud or self-hosted)  
- **Nodes Used**:
  - **Webhook**: Receives payload from LangChain outputs (summarization, RAG, SQL).  
  - **Slack**: Sends real-time alerts to channels.  
  - **Gmail / Email**: Sends automated emails to suppliers or supervisors.  
  - **HTTP Request**: Interacts with external APIs.  
  - **Google Sheets / Airtable**: Logs QA or summarization results.  

---

## 🔹 Flow Setup
1. **Webhook Trigger**
   - A webhook node listens for POST requests from your LangChain or SQL pipeline.
   - Example payload:
     ```json
     {
       "summary": "Machine downtime exceeded threshold",
       "downtime_hours": 5,
       "sentiment_score": -0.7
     }
<img width="1502" height="907" alt="image" src="https://github.com/user-attachments/assets/e493bcd9-befb-4899-9ce8-fc137ad55c17" />

     
     ```

2. **Conditional Nodes**
   - Check for thresholds:
     - `downtime_hours > 4` → trigger Slack/email alert.
     - `defect_rate > 5%` → trigger QA notification.
     - `investment > 50L` → trigger client email.

<img width="1850" height="914" alt="image" src="https://github.com/user-attachments/assets/0983412c-aa55-4311-99cd-03bdb9cfa491" />

       

3. **Action Nodes**
   - **Gmail**: Send email to supervisor or supplier.

<img width="1890" height="1004" alt="image" src="https://github.com/user-attachments/assets/4b92b07d-2056-46a0-b573-7cceab59cc13" />


   - **Google Sheets / Airtable**: Log summary, sentiment, or alert details for record keeping.


<img width="1886" height="987" alt="image" src="https://github.com/user-attachments/assets/cd626719-cdf4-407c-929e-06e379a5b890" />




3. **Transformation / Formatting**
   - Use **Function nodes** to format LangChain output into readable messages for Slack/email/Sheets.

---

## 🔹 How Webhook Integrates with LangChain
- LangChain pipeline outputs JSON via **HTTP POST** to the n8n webhook.  
- The webhook node receives data and passes it through the workflow:
  1. **Transform payload** → Function Node  
  2. **Conditional logic** → IF Node (thresholds)  
  3. **Send output** → Slack / Gmail / Sheets nodes  

- Example integration in Python (FastAPI):
  ```python
  import requests

  payload = {
      "summary": "Negative sentiment detected in QA logs",
      "sentiment_score": -0.8
  }
  webhook_url = "https://<your-n8n-domain>/webhook/langchain-alert"
  requests.post(webhook_url, json=payload)
