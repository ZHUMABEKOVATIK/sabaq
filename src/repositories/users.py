from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.db.sessions import async_session
from src.models import User

class UserRepo:
    async def create(self, name: str, phone: str | None = None) -> User:
        async with async_session() as session:
            try:
                user = User(name=name, phone=phone)
                session.add(user)
                await session.commit()
                return user
            except Exception as err:
                await session.rollback()
                raise

    async def get_all(self) -> list[User]:
        async with async_session() as session:
            return (await session.execute(
                    select(User)
                )
            ).scalars().all()
    
    async def get_by_id(self, id: int) -> User | None:
        async with async_session() as session:
            return (await session.execute(
                select(User)
                .where(User.id == id)
                .options(
                    selectinload(User.orders)
                )
            )).scalar_one_or_none()

    async def update(self, id: int, *, name: str | None = None, phone: str | None = None) -> User:
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

    async def delete_data(self, id: int) -> None:
        async with async_session() as session:
            data = (await session.execute(
                select(User)
                .where(User.id == id)
            )).scalar_one_or_none()

            if data is None:
                raise Exception("Bunday id g'a ten' user joq")
            
            await session.delete(data)