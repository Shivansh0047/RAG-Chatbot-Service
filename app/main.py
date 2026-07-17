from fastapi import FastAPI
from app.config import settings
from app.routes import ingest, chat

app = FastAPI(title="rag-chatbot-service") # Creates the main FastAPI application instance

# Registers the routes
app.include_router(ingest.router)
app.include_router(chat.router)

@app.get("/health")
def health():
    return {"status": "ok", "environment": settings.environment}