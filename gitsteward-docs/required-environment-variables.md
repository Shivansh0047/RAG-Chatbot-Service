---
source_anchor: "README.md#required-environment-variables"
source_commit: "7b3d1f2688fc0c849da3d444467ee40ddd1b5f7b"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The environment variable HF_TOKEN is no longer used and should be replaced with GOOGLE_API_TOKEN / gitsteward-docs/modified_gitsteward_readme.md: The section lists HF_TOKEN as being used for both embeddings and LLM, but the code diff indicates that GOOGLE_API_TOKEN is used for embeddings and HF_TOKEN is used for LLM. / gitsteward-docs/project-structure.md: The required environment variables may have changed due to the update from HuggingFace to Google Generative AI, potentially requiring a new token or API key / gitsteward-docs/required-environment-variables.md: The section still references the deprecated `HF_TOKEN` environment variable and its usage is outdated. / gitsteward-docs/stack.md: The HuggingFace token environment variable may no longer be needed or may need to be replaced with a Google Generative AI token

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
