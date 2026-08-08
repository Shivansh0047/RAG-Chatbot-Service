---
source_anchor: "README.md#stack"
source_commit: "e622abcad2e46cb44d16445b91886aee8df4f53b"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: The embeddings layer has changed from HuggingFace Inference API to Google Generative AI

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `models/gemini-embedding-001` via Google Generative AI |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace Inference API |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |
