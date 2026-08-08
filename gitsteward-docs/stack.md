---
source_anchor: "README.md#stack"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: The embeddings layer choice has changed from Google Generative AI to HuggingFace and the LLM choice has changed from Gemini via Google to meta-llama/Llama-3.1-8B-Instruct via HuggingFace Inference API

The embeddings layer and LLM choice have changed. The embeddings layer has changed from Google Generative AI to HuggingFace and the LLM choice has changed from Gemini via Google to meta-llama/Llama-3.1-8B-Instruct via HuggingFace Inference API 

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 via HuggingFace |
| LLM | meta-llama/Llama-3.1-8B-Instruct via HuggingFace Inference API |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |
