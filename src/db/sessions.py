from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    AsyncSession
)
from src.db.base import Base
from src.models.users import User
from src.models.orders import Order
from ..config import DB_URL

engine = create_async_engine(DB_URL, echo=False)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def async_main():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
