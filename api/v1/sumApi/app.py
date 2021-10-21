from fastapi import FastAPI
from .router import api_router

sumApi = FastAPI()

sumApi.include_router(api_router)
