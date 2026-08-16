---
source_anchor: "README.md#required-environment-variables"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: It claims `GOOGLE_API_TOKEN` is needed for embeddings, but the new HuggingFace implementation requires an `hf_token` instead.

| Variable | Description |
|---|---|
| `QDRANT_URL` | URL of the Qdrant Cloud cluster |
| `QDRANT_API_KEY` | API key for authenticating with Qdrant Cloud |
| `HF_TOKEN` | HuggingFace Hub API token used for embedding generation |
| `GOOGLE_API_TOKEN` | Google API token used for Google‑based LLM calls (no longer required for embeddings) |
| `MONGO_URI` | MongoDB connection string for back‑fill operations |
| `MONGO_DB_NAME` | Name of the MongoDB database |
| `MONGO_NOTES_COLLECTION` | Name of the MongoDB collection that stores notes |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` for external service authentication |
