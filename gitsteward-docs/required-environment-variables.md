---
source_anchor: "README.md#required-environment-variables"
source_commit: "c8cffe6942ee4c870987950fdb5324224562423a"
status: "updated"
---

**Why flagged:** app/config.py: The addition of GOOGLE_API_TOKEN to the config file is not reflected in the list of required environment variables. / app/rag/llm.py: The HuggingFace token is replaced with Google API token

| Variable | Description |
|---|---|
| `QDRANT_URL` | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant Cloud API key |
| `GOOGLE_API_TOKEN` | Google API token (for embeddings + LLM) |
| `MONGO_URI` | MongoDB connection string (for backfill) |
| `MONGO_DB_NAME` | MongoDB database name |
| `MONGO_NOTES_COLLECTION` | MongoDB collection name |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` |
