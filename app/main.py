from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="rag-chatbot-service")

@app.get("/health")
def health():
    return {"status":"ok", "enviroment":settings.environment}
