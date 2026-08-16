---
source_anchor: "README.md#how-it-works"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: the workflow still says the context is sent to Google Generative AI, which is no longer true

1. Notes are ingested (via MongoDB back‑fill or direct API call) → chunked → embedded → stored in Qdrant Cloud.  
2. On a chat request:  
   - The user question is embedded.  
   - The most relevant chunks are retrieved from the project‑specific Qdrant collection.  
   - Those chunks are supplied as context to the LLM, which is now a **Hugging Face** model (`meta‑llama/Llama‑3.1‑8B‑Instruct`) accessed through `ChatHuggingFace` and a `HuggingFaceEndpoint`.  
   - The LLM generates an answer, which is returned together with source attribution for the retrieved chunks.  
3. Each project gets its own isolated Qdrant collection via API‑key‑based `project_id` mapping, ensuring data never crosses between projects.  
4. The LLM client is instantiated once and cached (`@lru_cache(maxsize=1)`) by `get_llm()`, which builds the `HuggingFaceEndpoint` with the configured repository ID, task, token limits, sampling settings, and the Hugging Face API token from the application settings.
