from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from fastapi_limiter.depends import RateLimiter
from .utils import *

router = APIRouter()

@router.get(
    "/sum/",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(RateLimiter(times=100, hours=1))]
)
async def sum_view(
    a: int,
    b: int
):
    """
    Public Route Get Request Sum Two Query String Params
    """

    result = await cache(a, b)
    return {
        'result': result
    }
