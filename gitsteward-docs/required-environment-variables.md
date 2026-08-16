---
source_anchor: "README.md#required-environment-variables"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: `GOOGLE_API_TOKEN` is no longer required for LLM calls after switching to HuggingFace

| Variable | Description |
|---|---|
| `QDRANT_URL` | URL of the Qdrant Cloud cluster |
| `QDRANT_API_KEY` | API key for authenticating with Qdrant Cloud |
| `HF_TOKEN` | HuggingFace Hub API token used for both embedding generation and LLM calls via the HuggingFace endpoint |
| `MONGO_URI` | MongoDB connection string for back‑fill operations |
| `MONGO_DB_NAME` | Name of the MongoDB database |
| `MONGO_NOTES_COLLECTION` | Name of the MongoDB collection that stores notes |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` for external service authentication |
