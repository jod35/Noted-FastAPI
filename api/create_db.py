from models import Base
from db import engine
import asyncio


async def create_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    await engine.dispose()


asyncio.run(create_db())
