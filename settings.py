from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "DEV"
    SECRET_KEY: str = "jwtsecret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 3


settings = Settings()
