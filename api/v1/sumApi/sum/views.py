from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
# from fastapi_limiter.depends import RateLimiter
from slowapi import Limiter
from slowapi.util import get_remote_address
from core.configs import settings
from .utils import *

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.get(
    "/sum/",
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(RateLimiter(times=settings.LIMIT_RATE, hours=1))]
)
@limiter.limit(f"{settings.LIMIT_RATE}/hour")
async def sum_view(
    a: int,
    b: int,
    request: Request,
    response: Response
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
    admin: OAuth2PasswordRequestForm = Depends()
):
    """
    Show Result of History List All a & b Just Admin

    * If not Authenticated Raised 403 HTTPException
    """

    await authenticate(admin.username, admin.password)
    return {
        'history': await total_history('history')
    }


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
        'total': await total_history('total')
    }
