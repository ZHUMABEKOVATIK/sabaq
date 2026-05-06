from .db import async_session
from .models import User

from sqlalchemy import select, update, text

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

async def get_all() -> list[User]:
    async with async_session() as session:
        return (await session.execute(select(User))).scalars().all()
    
async def get_by_id(id: int) -> User | None:
    async with async_session() as session:
        return (await session.execute(
            select(User)
            .where(User.id == id)
        )).scalar_one_or_none()

# Update 1
async def update_data(id: int, name: str, phone: str) -> bool:
    async with async_session() as session:
        data = await session.execute(update(User).values(name=name, phone=phone).where(User.id == id))
        await session.commit()
        return data.rowcount > 0

# Update 2
async def update_db(id: int, *, name: str | None = None, phone: str | None = None) -> User:
    async with async_session() as session:
        data = (await session.execute(
            select(User)
            .where(User.id == id)
        )).scalar_one_or_none()

        if data is None:
            raise Exception("Bunday id g'a ten' user joq")

        if name is not None:
            data.name = name

        if phone is not None:
            data.phone = phone

        await session.commit()
        return data

async def delete_data(id: int) -> None:
    async with async_session() as session:
        data = (await session.execute(
            select(User)
            .where(User.id == id)
        )).scalar_one_or_none()

        if data is None:
            raise Exception("Bunday id g'a ten' user joq")
        
        await session.delete(data)


async def main():
    data = await update_db(2, name="Bob", phone="65465465")
    print(data.id, data.name, data.phone)











import asyncio
asyncio.run(main())