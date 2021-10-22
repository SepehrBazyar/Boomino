from fastapi import HTTPException, status
from typing import Literal, Union
from core.configs import settings
from core.security import verify_password
from core.database import get_mongodb

async def cache(a: int, b: int) -> int:
    """
    Cache Data Input Sum of a & b in Total & Objects in History
    """

    result = a + b
    db = await get_mongodb()
    doc = await db.find_one()
    if doc is None:
        await db.insert_one({
            'total': result,
            'history': [{
                'a': a,
                'b': b
            }]
        })
    else:
        await db.update_one({
            '_id': doc['_id']
        },{
            '$inc': {
                'total': result
            },
            '$push': {
                'history': {
                    'a': a,
                    'b': b
                }
            }
        })
    return result

async def authenticate(username: str, password: str):
    """
    Authenticated Admin by Check the Username & Password
    """

    if not(settings.ADMIN_USERNAME == username and verify_password(password)):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Username or Password is Wrong."
        )

async def total_history(keyword: Literal['total', 'history']) -> Union[int, list]:
    """
    Read Data Cached from MongoDB & if not in First Time Returned Default Values
    """

    db = await get_mongodb()
    doc = await db.find_one()
    if doc is None:
        return 0 if keyword == 'total' else []
    else:
        return doc.get(keyword)
