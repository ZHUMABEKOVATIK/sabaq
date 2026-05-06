from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String
from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger, 
        primary_key=True, 
        autoincrement=True,
        index=True
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str | None] = mapped_column(String, nullable=True)