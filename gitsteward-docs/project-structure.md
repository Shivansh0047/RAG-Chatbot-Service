---
source_anchor: "README.md#project-structure"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: llm.py now uses HuggingFace Llama instead of Gemini, so the description is outdated.

app/
├── main.py               # FastAPI app entrypoint
├── config.py             # Centralized environment variables (including HF token)
├── auth.py               # API key → project_id resolution
├── models.py             # Pydantic request/response schemas
├── routes/
│   ├── ingest.py         # POST /ingest/note, POST /ingest/upload
│   └── chat.py           # POST /chat
├── rag/
│   ├── embeddings.py     # Google Generative AI embeddings
│   ├── llm.py            # HuggingFace Llama 3.1 via LangChain HuggingFace wrapper
│   ├── vectorstore.py    # Qdrant client, per‑project collections
│   ├── splitter.py       # Text chunking utilities
│   └── chain.py          # Retrieval → prompt → generation pipeline
└── ingestion/
    ├── mongo_reader.py   # Reads notes from MongoDB
    └── pdf_extract.py    # Extracts text from uploaded PDFs
scripts/
└── backfill_from_mongo.py  # One‑time knowledge‑base seeding script
