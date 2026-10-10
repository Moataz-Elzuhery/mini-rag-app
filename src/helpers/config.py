from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# .env في فولدر src (جنب main.py). عدّل لو مكانه مختلف
ENV_PATH = Path(__file__).resolve().parents[1] / ".env"

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    model_config = SettingsConfigDict(env_file=ENV_PATH, env_file_encoding="utf-8")


def get_settings():
    return Settings()