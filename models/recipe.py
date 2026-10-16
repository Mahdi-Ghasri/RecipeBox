from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
BigInteger,
DateTime,
ForeignKey,
Identity,
Integer,
String,
Text,
func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.connection import Base

if TYPE_CHECKING:
    from models.user import User
from models.category import Category

class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(),
        primary_key=True,
        )

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False,
        )

    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
        )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        )

    instructions: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        )

    prep_time_minutes: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False,
        )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="recipes",
        )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="recipes",
        )

def __repr__(self) -> str:
        return f"Recipe(id={self.id}, title={self.title!r})"