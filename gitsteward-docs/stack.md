---
source_anchor: "README.md#stack"
source_commit: "5b7f65d10ac4ea1c3c10df6b41a83618f4f95c06"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The stack has changed with the update from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings layer has changed from HuggingFace to Google Generative AI

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `models/gemini-embedding-001` via Google Generative AI |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace Inference API |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |
