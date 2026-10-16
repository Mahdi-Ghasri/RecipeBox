from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import BigInteger, DateTime, Identity, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.connection import Base
if TYPE_CHECKING:
    from models.user_profile import UserProfile
from models.recipe import Recipe


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
    BigInteger,
    Identity(),
    primary_key=True,
        )

    email: Mapped[str] = mapped_column(
    String(255),
    nullable=False,
        )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.current_timestamp(),
    nullable=False,
        )

    profile: Mapped["UserProfile | None"] = relationship(
      "UserProfile", back_populates = "user", 
      uselist=False,
    )

    recipes: Mapped[list["Recipe"]] = relationship(
      "Recipe", back_populates = "user", 
    )
    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email!r})"