from sqlalchemy import BigInteger, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    recipe_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("recipes.id"),
        primary_key=True,
        )

    ingredient_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("ingredients.id"),
        primary_key=True,
        )

    quantity: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        )

    unit: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        )

def __repr__(self) -> str:
        return (
            f"RecipeIngredient(recipe_id={self.recipe_id}, "
            f"ingredient_id={self.ingredient_id})"
            )