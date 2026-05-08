from src.db.base import IDMix
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, ForeignKey, String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User

class Order(IDMix):
    __tablename__ = "orders"

    user_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    user: Mapped["User"] = relationship(back_populates="orders")