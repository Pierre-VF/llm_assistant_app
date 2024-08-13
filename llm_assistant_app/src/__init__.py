import os

from pydantic_settings import BaseSettings, SettingsConfigDict

# To ensure that the right .env file is used, its path is computed from this file
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_env_file_path = os.path.join(_parent_dir, ".env")


class Settings(BaseSettings):
    # LLM API keys
    anthropic_api_key: str
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=_env_file_path,
        env_file_encoding="utf-8",
    )


# Usage
settings = Settings()
