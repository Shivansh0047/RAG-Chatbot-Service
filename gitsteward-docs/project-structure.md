---
source_anchor: "README.md#project-structure"
source_commit: "7f4d602a67052d562242dd52460b7dbcf3913d53"
status: "updated"
---

**Why flagged:** app/rag/embeddings.py: embeddings.py now uses HuggingFaceEndpointEmbeddings instead of Google Generative AI, so the comment in the tree is outdated

app/
├── main.py               # FastAPI app entrypoint
├── config.py             # all env vars in one place
├── auth.py               # API key → project_id resolution
├── models.py             # request/response schemas
├── routes/
│   ├── ingest.py         # POST /ingest/note, POST /ingest/upload
│   └── chat.py           # POST /chat
├── rag/
│   ├── embeddings.py     # HuggingFace endpoint embeddings
│   ├── llm.py            # Gemini via Google
│   ├── vectorstore.py    # Qdrant client, per-project collections
│   ├── splitter.py       # text chunking
│   └── chain.py          # retrieve → prompt → generate
└── ingestion/
├── mongo_reader.py   # reads notes from MongoDB
└── pdf_extract.py    # extracts text from uploaded PDFs
scripts/
└── backfill_from_mongo.py  # one-time knowledge base seeding
