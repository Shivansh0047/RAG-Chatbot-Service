from pydantic_settings import BaseSettings 
import json

class Settings(BaseSettings):
    environment: str = "development"  # reads ENVIRONMENT from .env, if not gound, default is development

    qdrant_url: str        # no default — app should fail to start if this is missing
    qdrant_api_key: str  

    hf_token: str = ""

    class Config:
        env_file = ".env"  # load values from root-level .env file
    
    api_keys_json: str = "{}"  # maps api_key -> project_id

    @property # raw JSON string into an actual Python dict on demand, so everywhere else in the app calls settings.api_keys and gets back a real {"sk-abc": "exam_notes_generator"}
    def api_keys(self) -> dict:
        return json.loads(self.api_keys_json)

settings = Settings()  # single shared instance, import this elsewhere