---
source_anchor: "README.md#how-it-works"
source_commit: "7b3d1f2688fc0c849da3d444467ee40ddd1b5f7b"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The embeddings step now uses Google Generative AI instead of HuggingFace / gitsteward-docs/project-structure.md: The description of how the service works may no longer be accurate due to the change from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The change in embeddings layer may affect the embedding and retrieval process

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded using Google Generative AI → stored in Qdrant Cloud
2. On a chat request, the question is embedded using Google Generative AI → most relevant chunks retrieved from Qdrant → passed as context to Llama 3.1 → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects
