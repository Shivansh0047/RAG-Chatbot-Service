from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.rag.chain import answer_question

router = APIRouter(prefix="/chat", tags=["chat"]) # create a router with prefix /chat


class ChatRequest(BaseModel): # Pydantic chatrequent model
    project_id: str
    question: str


@router.post("")
def chat(payload: ChatRequest):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question is empty")
    return answer_question(payload.project_id, payload.question) # Call RAG chain