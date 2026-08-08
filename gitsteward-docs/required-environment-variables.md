---
source_anchor: "README.md#required-environment-variables"
source_commit: "4282fd4b246413c8ead576e1b52a44f68eefdf45"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The environment variable `HF_TOKEN` is no longer used and should be replaced with `GOOGLE_API_TOKEN` / gitsteward-docs/stack.md: A new environment variable may be required for Google Generative AI, and the description of HF_TOKEN may need to be updated

| Variable | Description |
|---|---|
| `QDRANT_URL` | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant Cloud API key |
| `GOOGLE_API_TOKEN` | Google API token (for embeddings + LLM) |
| `MONGO_URI` | MongoDB connection string (for backfill) |
| `MONGO_DB_NAME` | MongoDB database name |
| `MONGO_NOTES_COLLECTION` | MongoDB collection name |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` |
