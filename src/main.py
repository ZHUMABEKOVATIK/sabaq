from .db import async_session
from .models import User

async def create(name: str, phone: str | None = None) -> User:
    async with async_session() as session:
        try:
            user = User(name=name, phone=phone)
            session.add(user)
            await session.commit()
            return user
        except Exception as err:
            await session.rollback()
            raise
    
import asyncio

asyncio.run(create("Bob", "21212121"))