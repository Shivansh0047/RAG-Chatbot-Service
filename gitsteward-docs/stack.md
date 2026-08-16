---
source_anchor: "README.md#stack"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: Embeddings entry still lists `gemini-embedding-001` via Google Generative AI

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` via HuggingFace |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace (text‑generation endpoint) |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read‑only, for backfill) |
| Hosting | Render (free tier, Oregon) |
