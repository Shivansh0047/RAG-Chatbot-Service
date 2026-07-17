from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.rag.splitter import split_text
from app.rag.vectorstore import get_vectorstore
from app.auth import get_project_id

router = APIRouter(prefix="/ingest", tags=["ingest"]) #  create router with prefix /ingest

class NoteRequest(BaseModel): # Pydantic Notes Model
    note_id: str
    owner_id: str
    title: str
    text: str

@router.post("/note")
def ingest_note(payload: NoteRequest, project_id: str = Depends(get_project_id)): # payload is automatically populated by FastAPI from the request JSON body, validated against NoteRequest
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Note text is empty")
    
    docs = split_text(payload.text, { # Split text into chunks
        "note_id": payload.note_id,
        "owner_id": payload.owner_id,
        "note_title":payload.title,
    })

    get_vectorstore(project_id).add_documents(docs)  # add cunks
    return {"status": "ok", "chunks_indexed": len(docs)}

@router.post("/upload")
async def ingest_upload(file: UploadFile = File(...), project_id: str = Depends(get_project_id)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDFs supported")
    from pypdf import PdfReader
    from io import BytesIO

    file_bytes = await file.read() # Read bytes form pdf
    reader = PdfReader(BytesIO(file_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    if not text.strip():
        raise HTTPException(status_code=400, detail="Note text is empty") 
    
    docs = split_text(text, {"note_title": file.filename, "source_type": "uploaded"})

    get_vectorstore(project_id).add_documents(docs)
    return {"status": "ok", "chunks_indexed": len(docs)}