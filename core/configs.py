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
    DATABASE_NAME: str
    COLLECTION_NAME: str

    # authenticate
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    # rate limiting per hour
    LIMIT_RATE: int


settings = Settings()
