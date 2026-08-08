from functools import lru_cache
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from app.config import settings

'''
@lru_cache(maxsize=1)  # loads once, reused on every request by caching
def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=settings.GOOGLE_API_TOKEN,
        temperature=0,
    )
'''

@lru_cache(maxsize=1)  # loads once, reused on every request by caching
def get_llm() -> ChatHuggingFace:
    endpoint = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        huggingfacehub_api_token=settings.hf_token,
    )
    return ChatHuggingFace(llm=endpoint)  # wraps endpoint into chat interface LangChain expects