from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3"
    CHUNK_SIZE: int = 2500
    CHUNK_OVERLAP: int = 200
    OUTPUT_DIR: str = "stories"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    IMAGE_GENERATION_API_URL: str
    IMAGE_GENERATION_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()