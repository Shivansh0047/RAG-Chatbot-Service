from langchain_huggingface import HuggingFaceEmbeddings
from functools import lru_cache

@lru_cache(maxsize=1)  # loads the model once, reuses it on every subsequent call by chaching itfrom functools import lru_cache
def get_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )