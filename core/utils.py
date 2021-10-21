from fastapi_limiter import FastAPILimiter
from aioredis import from_url
from .configs import settings

async def startup():
    redis = await from_url(settings.REDIS_URL, encoding='utf-8', decode_responses=True)
    await FastAPILimiter.init(redis)
