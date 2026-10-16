from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class Favorite(Base):
    __tablename__ = "favorites"

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id"),
        primary_key=True,
        )

    recipe_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("recipes.id"),
        primary_key=True,
        )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False,
        )

def __repr__(self) -> str:
        return (
            f"Favorite(user_id={self.user_id}, "
            f"recipe_id={self.recipe_id})"
        )