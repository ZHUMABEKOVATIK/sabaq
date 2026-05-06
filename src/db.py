from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    AsyncSession
)
from .base import Base
from .models import User
from .config import DB_URL

engine = create_async_engine(DB_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def async_main():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
