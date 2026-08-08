---
source_anchor: "README.md#how-it-works"
source_commit: "4282fd4b246413c8ead576e1b52a44f68eefdf45"
status: "updated"
---

**Why flagged:** gitsteward-docs/stack.md: The embeddings step in the workflow has changed from using HuggingFace Inference API to Google Generative AI

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded using Google Generative AI's Gemini embedding model → stored in Qdrant Cloud
2. On a chat request, the question is embedded using Google Generative AI's Gemini embedding model → most relevant chunks retrieved from Qdrant → passed as context to Llama 3.1 → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects
