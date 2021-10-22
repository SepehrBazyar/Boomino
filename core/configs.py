from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Settings(BaseSettings):
    """
    Base Setting Variables in ENV File
    """

    class Config:
        env_file = ".env"

    SECRET_KEY: str
    ALLOWED_HOSTS: str
    ALGORITHM: str
    DEBUG: bool    

    # databases
    REDIS_URL: str
    MONGODB_URL: str
    COLLECTION_NAME: str

    # authenticate
    USERNAME: str
    PASSWORD: str

    # rate limiting per hour
    LIMIT_RATE: int


settings = Settings()
