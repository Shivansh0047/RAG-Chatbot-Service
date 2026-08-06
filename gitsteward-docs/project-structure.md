---
source_anchor: "README.md#project-structure"
source_commit: "5b7f65d10ac4ea1c3c10df6b41a83618f4f95c06"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The project structure has changed with the update from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings.py file has changed to use Google Generative AI instead of HuggingFace

```
app/
├── main.py               # FastAPI app entrypoint
├── config.py             # all env vars in one place
├── auth.py               # API key → project_id resolution
├── models.py             # request/response schemas
├── routes/
│   ├── ingest.py         # POST /ingest/note, POST /ingest/upload
│   └── chat.py           # POST /chat
├── rag/
│   ├── embeddings.py     # Google Generative AI remote embeddings
│   ├── llm.py            # Llama via HuggingFace Inference API
│   ├── vectorstore.py    # Qdrant client, per-project collections
│   ├── splitter.py       # text chunking
│   └── chain.py          # retrieve → prompt → generate
└── ingestion/
├── mongo_reader.py   # reads notes from MongoDB
└── pdf_extract.py    # extracts text from uploaded PDFs
scripts/
└── backfill_from_mongo.py  # one-time knowledge base seeding
```
