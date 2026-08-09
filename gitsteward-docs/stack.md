---
source_anchor: "README.md#stack"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: The LLM layer has changed from Gemini via Google to meta-llama/Llama-3.1-8B-Instruct via HuggingFace Inference API

The embeddings layer has changed from HuggingFace to Google Generative AI and the LLM layer has changed from Gemini via Google to meta-llama/Llama-3.1-8B-Instruct via HuggingFace Inference API 

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `models/gemini-embedding-001` via Google Generative AI |
| LLM | `meta-llama/Llama-3.1-8B-Instruct` via HuggingFace Inference API |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |
