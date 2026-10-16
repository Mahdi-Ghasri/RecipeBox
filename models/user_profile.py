from sqlalchemy import BigInteger, ForeignKey, String, Text
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database.connection import Base
if TYPE_CHECKING:
    from models.user import User

class UserProfile(Base):
    __tablename__ = "user_profiles"

    user_id: Mapped[int] = mapped_column(
    BigInteger,
    ForeignKey("users.id"),
    primary_key=True,
    )

    full_name: Mapped[str] = mapped_column(
    String(150),
    nullable=False,
    )

    avatar_url: Mapped[str | None] = mapped_column(
    String(500),
    nullable=True,
    )

    bio: Mapped[str | None] = mapped_column(
    Text,
    nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile",
    )

    def __repr__(self) -> str:
        return (
            f"UserProfile(user_id={self.user_id}, "
            f"full_name={self.full_name!r})"
    )