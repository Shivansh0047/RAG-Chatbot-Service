---
source_anchor: "README.md#required-environment-variables"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: The environment variable usage has changed, with GOOGLE_API_TOKEN now used for a different purpose and HF_TOKEN still being used

The environment variable `HF_TOKEN` is still used, while `GOOGLE_API_TOKEN` is now used for a different purpose. 

| Variable | Description |
|---|---|
| `QDRANT_URL` | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant Cloud API key |
| `GOOGLE_API_TOKEN` | Google API token (for a different purpose) |
| `HF_TOKEN` | Hugging Face API token (for embeddings) |
| `MONGO_URI` | MongoDB connection string (for backfill) |
| `MONGO_DB_NAME` | MongoDB database name |
| `MONGO_NOTES_COLLECTION` | MongoDB collection name |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` |
