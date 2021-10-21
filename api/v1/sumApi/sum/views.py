from fastapi import (
    APIRouter,
    HTTPException,
    status
)
from .utils import *

router = APIRouter()

@router.get(
    "/sum/",
    status_code=status.HTTP_200_OK
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
