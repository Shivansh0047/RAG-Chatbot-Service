# rag-chatbot-service

A standalone RAG (Retrieval-Augmented Generation) chatbot service built with **FastAPI** and **LangChain**. Answers questions from a shared knowledge base built from exam notes — currently integrated with the [AI Exam Notes Generator](https://github.com/Shivansh0047/AI_EXAM_NOTES_GENERATOR) project, but designed to support any project via isolated knowledge bases.  
**Live URL:** `https://rag-chatbot-service-1poi.onrender.com`  
---

## How it works

1. Notes are ingested (from MongoDB backfill or direct API call) → chunked → embedded → stored in Qdrant Cloud
2. On a chat request, the question is embedded → most relevant chunks retrieved from Qdrant → passed as context to Google Generative AI → answer returned with source attribution
3. Each project gets its own isolated Qdrant collection via API key → `project_id` mapping — data never crosses between projects

## Stack

| Layer | Choice |
|---|---|
| API | FastAPI |
| RAG | LangChain (plain LCEL) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` via HuggingFace Inference API |
| LLM | `gemini-2.5-flash` via Google Generative AI |
| Vector store | Qdrant Cloud (free tier, AWS Oregon) |
| Source DB | MongoDB (read-only, for backfill) |
| Hosting | Render (free tier, Oregon) |

## Authentication

Every request requires an `X-API-Key` header. Keys are mapped to a `project_id` server-side — the caller never needs to know or specify the project ID directly.  
```
X-API-Key: your-secret-key-here
```  
Missing or invalid key returns `401 Unauthorized`. Contact the repo owner to get a key issued for your project.  
---

### `GET /health`

Liveness check. No auth required.  
**Response**
```json
{
"status": "ok",
"environment": "production"
}
```  
---

### `POST /ingest/note`

Ingest a single note into the knowledge base. Called automatically by the Express backend after a note is generated.  
**Headers**
```
X-API-Key: your-secret-key-here
Content-Type: application/json
```  
**Request body**
```json
{
"note_id": "mongo-document-id",
"owner_id": "user-id",
"title": "Newton's Laws of Motion",
"text": "full plain text content of the note"
}
```  
**Response**
```json
{
"status": "ok",
"chunks_indexed": 4
}
```  
---

### `POST /ingest/upload`

Ingest a user-uploaded PDF into the knowledge base.  
**Headers**
```
X-API-Key: your-secret-key-here
```  
**Request body**
`multipart/form-data` with a single field `file` containing the PDF.  
**Response**
```json
{
"status": "ok",
"chunks_indexed": 7
}
```  
---

### `POST /chat`

Ask a question against the knowledge base.  
**Headers**
```
X-API-Key: your-secret-key-here
Content-Type: application/json
```  
**Request body**
```json
{
"question": "What are Newton's laws of motion?"
}
```  
**Response**
```json
{
"answer": "Newton's Laws of Motion are fundamental principles...",
"sources": [
"Netwons Laws of motion",
"Newton laws motion",
"Newtons Laws of motion"
]
}
```  
The `sources` array lists the note titles whose chunks were retrieved to generate the answer. If the knowledge base doesn't contain relevant information, the model says so rather than hallucinating.  
---

### AI Exam Notes Generator

The primary integration. The knowledge base (`exam_notes_generator` collection in Qdrant) is seeded from all notes stored in the project's MongoDB database via a one-time backfill script (`scripts/backfill_from_mongo.py`). Going forward, new notes are auto-ingested by the Express backend calling `POST /ingest/note` after each generation.  
**Currently indexed:** 30 notes, 168 chunks  
---

## Adding a new project

This service is built to be reusable. One deployed instance can serve multiple completely isolated knowledge bases — each project's data lives in its own Qdrant collection and is never mixed with others.  
To add a new project:  
1. Generate a new random API key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```  
2. Add it to `API_KEYS_JSON` in Render's environment variables:
```json
{
"existing-key": "exam_notes_generator",
"new-project-key": "your_new_project_id"
}
```  
3. The new project's Qdrant collection is created automatically on the first `/ingest/note` or `/ingest/upload` call — no manual setup needed.  
4. If the new project has a different MongoDB schema, flatten the content into plain text in the calling backend before sending to `/ingest/note`. The service itself is schema-agnostic.  
---

## Local setup

```bash
git clone https://github.com/Shivansh0047/rag-chatbot-service
cd rag-chatbot-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # fill in real values
uvicorn app.main:app --reload
```  
Visit `http://localhost:8000/docs` for interactive API docs.

### Required environment variables

| Variable | Description |
|---|---|
| `QDRANT_URL` | Qdrant Cloud cluster URL |
| `QDRANT_API_KEY` | Qdrant Cloud API key |
| `GOOGLE_API_TOKEN` | Google API token (for embeddings + LLM) |
| `MONGO_URI` | MongoDB connection string (for backfill) |
| `MONGO_DB_NAME` | MongoDB database name |
| `MONGO_NOTES_COLLECTION` | MongoDB collection name |
| `API_KEYS_JSON` | JSON map of `{"api_key": "project_id"}` |

### Seeding the knowledge base (one-time)

```bash
python -m scripts.backfill_from_mongo
```  
---

## Project structure

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
│   ├── embeddings.py     # HuggingFace remote embeddings
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
