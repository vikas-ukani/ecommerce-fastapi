from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_ignore_empty=True, extra='ignore')

    APP_NAME: str = "Fast Commerce"
    DEBUG: bool = True
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    MONGO_URL: str = "mongodb://localhost:27017/fast-commmerce"

    ACCESS_TOKEN_EXPIRES_IN: int = 15
    REFRESH_TOKEN_EXPIRES_IN: int = 60
    JWT_ALGORITHM: str = "HS256"

    JWT_SECRET_KEY: str = "jwtsecret key"
    JWT_PRIVATE_KEY: str = "jwtprivatekey"
    JWT_PUBLIC_KEY: str = "jwtpublickey"

    CLIENT_ORIGIN: str = "http://localhost:3000"


settings = Settings()
