from functools import lru_cache
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct 
from app.config import settings
from app.rag.embeddings import get_embeddings
import uuid

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

def add_documents(project_id: str, documents: list, note_id: str) -> int:
    """
    Upsert documents using deterministic IDs based on note_id + chunk index.
    Same note_id always produces same point IDs — safe to call multiple times
    without creating duplicates.
    """
    if not documents:
        return 0

    client = get_qdrant_client()
    _ensure_collection(client, project_id)
    embeddings = get_embeddings()

    # embed all chunks
    texts = [doc.page_content for doc in documents]
    vectors = embeddings.embed_documents(texts)

    # build points with deterministic IDs
    # note_id:chunk_index gives a unique, stable ID per chunk per note
    points = []
    for i, (doc, vector) in enumerate(zip(documents, vectors)):
        # Qdrant requires UUID format for string IDs — we generate one
        # deterministically from note_id + chunk index using uuid5
        point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{note_id}:{i}"))
        points.append(
            PointStruct(
                id=point_id,
                vector=vector,
                payload={
                    "page_content": doc.page_content,
                    **doc.metadata
                }
            )
        )

    client.upsert(collection_name=project_id, points=points)
    return len(points)


def get_retriever(project_id: str):
    return get_vectorstore(project_id).as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )