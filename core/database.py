from motor.motor_asyncio import AsyncIOMotorClient
from .configs import settings

class AsyncMongoDB:
    """
    Async Driver Connection Mongo DataBase
    """

    client = None
    db = None


mongodb = AsyncMongoDB()

async def get_mongodb():
    """
    Dependencies to Get MongoDB in Views
    """

    return mongodb.db

async def connect_mongodb():
    """
    Connection to Mongo DataBase in Startup Event Handler
    """

    mongodb.client = AsyncIOMotorClient(
        settings.MONGODB_URL
    )
    mongodb.db = mongodb.client[settings.COLLECTION_NAME]

async def close_mongodb():
    """
    Close Connection Mongo DataBase in Shutdown Event Handler
    """

    await mongodb.client.close()
