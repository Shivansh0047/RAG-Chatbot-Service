---
source_anchor: "README.md#required-environment-variables"
source_commit: "e622abcad2e46cb44d16445b91886aee8df4f53b"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: The environment variable `HF_TOKEN` is no longer used and should be replaced with `GOOGLE_API_TOKEN`

| Variable | Description |
|---|---|
| `QDRANT_URL` | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant Cloud API key |
| `GOOGLE_API_TOKEN` | Google API token (for embeddings + LLM) |
| `MONGO_URI` | MongoDB connection string (for backfill) |
| `MONGO_DB_NAME` | MongoDB database name |
| `MONGO_NOTES_COLLECTION` | MongoDB collection name |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` |
