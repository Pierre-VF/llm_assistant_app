from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # LLM API keys
    anthropic_api_key: str
    debug: bool = False

    model_config = SettingsConfigDict(env_file_encoding="utf-8")


# Usage
settings = Settings()
