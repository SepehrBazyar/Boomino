from fastapi import HTTPException, status
from core.configs import settings
from core.security import verify_password
from core.database import get_mongodb

async def cache(a: int, b: int) -> int:
    """
    Sample Cache Input
    """

    result = a + b
    db = await get_mongodb()
    db.insert_one({'total':result})
    return result

async def authenticate(username: str, password: str):
    """
    Authenticated Admin by Check the Username & Password
    """

    if not(settings.USERNAME == username and verify_password(password)):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Username or Password is Wrong."
        )
