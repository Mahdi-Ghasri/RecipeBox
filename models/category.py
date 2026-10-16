from sqlalchemy import Identity, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from database.connection import Base
if TYPE_CHECKING:
    from models.recipe import Recipe


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
    Integer,
    Identity(),
    primary_key=True,
    )

    name: Mapped[str] = mapped_column(
    String(100),
    nullable=False,
    )

    recipes: Mapped[list["Recipe"]] = relationship(
      "Recipe", back_populates = "category", 
    )
    def __repr__(self) -> str:
        return f"Category(id={self.id}, name={self.name!r})"