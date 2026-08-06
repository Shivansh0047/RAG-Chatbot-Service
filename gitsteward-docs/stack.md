---
source_anchor: "README.md#stack"
source_commit: "7b3d1f2688fc0c849da3d444467ee40ddd1b5f7b"
status: "updated"
---

**Why flagged:** gitsteward-docs/project-structure.md: The stack description in the README no longer matches the updated technology stack, specifically the change from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings layer has changed from HuggingFace to Google Generative AI

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | Google Generative AI |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace Inference API |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |
