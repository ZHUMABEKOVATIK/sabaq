from src.models import Order
from src.db.sessions import async_session

from sqlalchemy import select
from sqlalchemy.orm import selectinload


class OrdersRepo:
    async def create(self, user_id: int, name: str) -> Order:
        async with async_session() as session:
            order = Order(
                user_id=user_id,
                name=name
            )
            session.add(order)
            await session.commit()
        
    async def get_all(self) -> list[Order]:
        async with async_session() as session:
            return (await session.execute(
                select(Order)
                .options(
                    selectinload(Order.user)
                )
            )).scalars().all()
        