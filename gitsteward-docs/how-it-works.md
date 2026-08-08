---
source_anchor: "README.md#how-it-works"
source_commit: "e622abcad2e46cb44d16445b91886aee8df4f53b"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: The LLM used in the chat request has changed from Llama to Gemini, which may require updates to the explanation of the chat request process.

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded → stored in Qdrant Cloud
2. On a chat request, the question is embedded → most relevant chunks retrieved from Qdrant → passed as context to Gemini 2.5 → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects
