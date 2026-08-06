---
source_anchor: "README.md#local-setup"
source_commit: "c8cffe6942ee4c870987950fdb5324224562423a"
status: "updated"
---

**Why flagged:** app/config.py: The local setup instructions do not account for the new GOOGLE_API_TOKEN environment variable.

To set up the project locally, follow these steps:
```bash
git clone https://github.com/Shivansh0047/rag-chatbot-service
cd rag-chatbot-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # fill in real values, including GOOGLE_API_TOKEN
uvicorn app.main:app --reload
```  
Visit `http://localhost:8000/docs` for interactive API docs.
