from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.auth import get_project_id
from app.rag.chain import answer_question


router = APIRouter(prefix="/chat", tags=["chat"]) # create a router with prefix /chat


class ChatRequest(BaseModel): # Pydantic chatrequent model
    question: str


@router.post("")
def chat(payload: ChatRequest, project_id: str = Depends(get_project_id)):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question is empty")
    return answer_question(project_id, payload.question) # Call RAG chain