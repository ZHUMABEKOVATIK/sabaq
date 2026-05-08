from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from src.db.base import IDMix
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .orders import Order

class User(IDMix):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str | None] = mapped_column(String, nullable=True)
    is_delete: Mapped[bool] = mapped_column(Boolean, default=False)

    orders: Mapped[list["Order"]] = relationship(back_populates="user")