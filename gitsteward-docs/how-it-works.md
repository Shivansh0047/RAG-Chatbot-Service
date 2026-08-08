---
source_anchor: "README.md#how-it-works"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: The LLM used in the chat request process has changed from Google Generative AI to HuggingFace Inference API

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded → stored in Qdrant Cloud
2. On a chat request, the question is embedded → most relevant chunks retrieved from Qdrant → passed as context to HuggingFace Inference API → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects
