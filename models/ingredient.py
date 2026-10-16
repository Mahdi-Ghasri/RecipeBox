from sqlalchemy import Identity, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(
    Integer,
    Identity(),
    primary_key=True,
    )

    name: Mapped[str] = mapped_column(
    String(150),
    nullable=False,
    )

    def __repr__(self) -> str:
        return f"Ingredient(id={self.id}, name={self.name!r})"