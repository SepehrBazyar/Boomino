from fastapi import APIRouter
from .sum.views import router as sum_router

api_router = APIRouter()

api_router.include_router(sum_router, prefix="/sum", tags=["sum"])
