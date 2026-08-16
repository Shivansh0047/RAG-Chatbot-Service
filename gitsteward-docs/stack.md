---
source_anchor: "README.md#stack"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: The LLM entry still lists `gemini-2.5-flash` via Google, but the code now uses a HuggingFace Llama model.

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `gemini-embedding-001` via Google Generative AI |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace (text‑generation endpoint) |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read‑only, for backfill) |
| Hosting | Render (free tier, Oregon) |
