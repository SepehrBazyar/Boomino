from fastapi import HTTPException, status
from core.configs import settings
from core.security import verify_password
history, total = [], 0

async def cache(a: int, b: int) -> int:
    """
    Sample Cache Input
    """

    global total
    result = a + b
    history.append({
        'a': a,
        'b': b,
    })
    total += result
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
