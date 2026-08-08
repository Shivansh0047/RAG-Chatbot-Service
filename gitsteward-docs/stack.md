---
source_anchor: "README.md#stack"
source_commit: "4282fd4b246413c8ead576e1b52a44f68eefdf45"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The embeddings layer has changed from HuggingFace Inference API to Google Generative AI / gitsteward-docs/stack.md: The embeddings layer has changed from HuggingFace Inference API to Google Generative AI

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `models/gemini-embedding-001` via Google Generative AI |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace Inference API |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |  
---
