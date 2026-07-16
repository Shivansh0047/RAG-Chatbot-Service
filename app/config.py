from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    environment: str = "development"  # reads ENVIRONMENT from .env, if not gound, default is development

    qdrant_url: str        # no default — app should fail to start if this is missing
    qdrant_api_key: str  

    class Config:
        env_file = ".env"  # load values from root-level .env file


settings = Settings()  # single shared instance, import this elsewhere