---
source_anchor: "README.md#how-it-works"
source_commit: "c8cffe6942ee4c870987950fdb5324224562423a"
status: "updated"
---

**Why flagged:** app/rag/llm.py: The LLM used in the chat request has changed from Llama 3.1 to Gemini 2.5

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded → stored in Qdrant Cloud
2. On a chat request, the question is embedded → most relevant chunks retrieved from Qdrant → passed as context to Gemini 2.5 → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects
