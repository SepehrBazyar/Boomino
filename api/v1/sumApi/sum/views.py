from fastapi import (
    APIRouter,
    Depends,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
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


@router.get(
    "/history/"
)
async def history_view(

):
    """
    
    """

    pass


@router.get(
    "/total/"
)
async def total_view(
    admin: OAuth2PasswordRequestForm = Depends()
):
    """
    Show Result of Total Sum All a & b Just Admin

    * If not Authenticated Raised 403 HTTPException
    """

    await authenticate(admin.username, admin.password)
    return {
        'total': total
    }
