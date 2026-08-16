---
source_anchor: "README.md#project-structure"
source_commit: "db57fb315705446f88164f57e19633e0ec89f2ae"
status: "updated"
---

**Why flagged:** app/rag/llm.py: llm.py is no longer Gemini via Google but HuggingFace Llama

app/
├── main.py               # FastAPI app entrypoint
├── config.py             # all env vars in one place
├── auth.py               # API key → project_id resolution
├── models.py             # request/response schemas
├── routes/
│   ├── ingest.py         # POST /ingest/note, POST /ingest/upload
│   └── chat.py           # POST /chat
├── rag/
│   ├── embeddings.py     # Google Generative AI
│   ├── llm.py            # HuggingFace Llama via LangChain
│   ├── vectorstore.py    # Qdrant client, per-project collections
│   ├── splitter.py       # text chunking
│   └── chain.py          # retrieve → prompt → generate
└── ingestion/
├── mongo_reader.py   # reads notes from MongoDB
└── pdf_extract.py    # extracts text from uploaded PDFs
scripts/
└── backfill_from_mongo.py  # one-time knowledge base seeding
