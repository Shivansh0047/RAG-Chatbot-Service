from functools import lru_cache
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import settings


@lru_cache(maxsize=1)  # loads once, reused on every request by caching
def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=settings.GOOGLE_API_TOKEN,
        temperature=0,
    )