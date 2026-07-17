from fastapi import Header, HTTPException, status
from app.config import settings\

async def get_project_id(x_api_key: str = Header(..., alias="X-API_KEY")) -> str:  # ... means it is required, tells FastAPI to look for a request header called X-API-Key
    project_id = settings.api_keys.get(x_api_key)  # looks up key in API_KEYS_JSON map
    if project_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )
    return project_id