---
source_anchor: "README.md#stack"
source_commit: "c8cffe6942ee4c870987950fdb5324224562423a"
status: "updated"
---

**Why flagged:** app/rag/llm.py: The LLM is changed from HuggingFace to Google Generative AI

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` via HuggingFace Inference API |
| LLM | `gemini-2.5-flash` via Google Generative AI |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |  
---
