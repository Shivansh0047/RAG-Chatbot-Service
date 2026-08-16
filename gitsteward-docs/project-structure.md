---
source_anchor: "README.md#project-structure"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: embeddings.py now uses HuggingFace embeddings instead of Google Generative AI

app/
├── main.py               # FastAPI application entry point
├── config.py             # Centralized environment variables (includes `hf_token` for HuggingFace)
├── auth.py               # Resolves API key to project ID
├── models.py             # Pydantic request/response schemas
├── routes/
│   ├── ingest.py         # POST /ingest/note, POST /ingest/upload
│   └── chat.py           # POST /chat
├── rag/
│   ├── embeddings.py     # HuggingFace sentence‑transformer embeddings via `HuggingFaceEndpointEmbeddings`
│   ├── llm.py            # Llama 3.1 accessed through LangChain’s HuggingFace wrapper
│   ├── vectorstore.py    # Qdrant client with per‑project collections
│   ├── splitter.py       # Text chunking utilities
│   └── chain.py          # Retrieval → prompt → generation pipeline
└── ingestion/
    ├── mongo_reader.py   # Reads notes from MongoDB
    └── pdf_extract.py    # Extracts text from uploaded PDFs
scripts/
└── backfill_from_mongo.py  # One‑time knowledge‑base seeding script

**Key implementation detail**

* `app/rag/embeddings.py` now defines `get_embeddings()` (cached with `@lru_cache`) that returns a `HuggingFaceEndpointEmbeddings` instance configured with the `sentence-transformers/all-MiniLM-L6-v2` model and the HuggingFace Hub token from `settings.hf_token`. The previous Google Generative AI embedding code has been removed.
