from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "DEV"
    SECRET_KEY: str = "jwtsecret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    CHAIN_NAME: str = "ProcureChain"
    RPC_USER: str = "multichainrpc"
    RPC_PASSWORD: str = "J3rCTwf1fUoCFPN6v6KnPDRS8AvtY5aJuS7iDVqDAg5J"
    RPC_HOST: str = "127.0.0.1"
    RPC_PORT: str = "2772"


settings = Settings()
