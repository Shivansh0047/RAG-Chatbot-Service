from functools import lru_cache
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from app.config import settings
from app.rag.embeddings import get_embeddings

# No need for async calls, as it is called onlt once
@lru_cache(maxsize=1)  # one client for the whole app lifetime, call and cache it
def get_qdrant_client() -> QdrantClient:
    return QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)


def _ensure_collection(client: QdrantClient, collection_name: str) -> None: # Function to ensure connection (internal, do not call from outside), it creates it if dosnt exits
    if client.collection_exists(collection_name):
        return
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),  # 384 = all-MiniLM-L6-v2 dimension, hardcoded for now
    )

def get_vectorstore(project_id: str) -> QdrantVectorStore:
    client = get_qdrant_client()
    _ensure_collection(client, project_id)  # creates collection only if it doesn't exist yet
    return QdrantVectorStore(
        client=client,
        collection_name=project_id,  # each project gets its own isolated collection
        embedding=get_embeddings(),
    )