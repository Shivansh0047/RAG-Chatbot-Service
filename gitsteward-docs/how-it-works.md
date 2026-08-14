---
source_anchor: "README.md#how-it-works"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: The embeddings step now uses Hugging Face instead of Google Generative AI

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded → stored in Qdrant Cloud
2. On a chat request, the question is embedded → most relevant chunks retrieved from Qdrant → passed as context to Hugging Face → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects
