---
source_anchor: "README.md#project-structure"
source_commit: "4282fd4b246413c8ead576e1b52a44f68eefdf45"
status: "updated"
---

**Why flagged:** gitsteward-docs/README.md: The project structure may have changed due to the update of the embeddings layer from HuggingFace Inference API to Google Generative AI / gitsteward-docs/stack.md: The embeddings.py file has changed to use Google Generative AI instead of HuggingFace Inference API

Project structure

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
│   ├── embeddings.py     # Google Generative AI embeddings
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
