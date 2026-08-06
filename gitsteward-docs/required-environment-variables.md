---
source_anchor: "README.md#required-environment-variables"
source_commit: "5b7f65d10ac4ea1c3c10df6b41a83618f4f95c06"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The environment variable HF_TOKEN is no longer used and should be replaced with GOOGLE_API_TOKEN / gitsteward-docs/required-environment-variables.md: The section still references the deprecated `HF_TOKEN` environment variable. / gitsteward-docs/stack.md: The HuggingFace token is no longer used for embeddings, but still used for LLM

| Variable | Description |
|---|---|
| `QDRANT_URL` | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant Cloud API key |
| `GOOGLE_API_TOKEN` | Google API token (for embeddings) |
| `HF_TOKEN` | HuggingFace token (for LLM) |
| `MONGO_URI` | MongoDB connection string (for backfill) |
| `MONGO_DB_NAME` | MongoDB database name |
| `MONGO_NOTES_COLLECTION` | MongoDB collection name |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` |
