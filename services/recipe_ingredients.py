from decimal import Decimal
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.recipe_ingredient import RecipeIngredient

def add_recipe_ingredient(
    session: Session,
    recipe_id: int,
    ingredient_id: int,
    quantity: Decimal,
    unit: str,
) -> RecipeIngredient:
    recipe_ingredient = RecipeIngredient(
    recipe_id=recipe_id,
    ingredient_id=ingredient_id,
    quantity=quantity,
    unit=unit,
    )

    session.add(recipe_ingredient)
    session.flush()
    return recipe_ingredient

def get_recipe_ingredient(
    session: Session,
    recipe_id: int,
    ingredient_id: int,
) -> RecipeIngredient | None:
    return session.get(
        RecipeIngredient,
        (recipe_id, ingredient_id),
    )

def list_recipe_ingredients(
    session: Session,
    recipe_id: int,
) -> list[RecipeIngredient]:
    statement = (
        select(RecipeIngredient)
        .where(RecipeIngredient.recipe_id == recipe_id)
        .order_by(RecipeIngredient.ingredient_id)
)

    return list(session.scalars(statement).all())

def update_recipe_ingredient(
    session: Session,
    recipe_id: int,
    ingredient_id: int,
    quantity: Decimal,
    unit: str,
) -> RecipeIngredient | None:
    recipe_ingredient = get_recipe_ingredient(
    session,
    recipe_id,
    ingredient_id,
    )

    if recipe_ingredient is None:
        return None

    recipe_ingredient.quantity = quantity
    recipe_ingredient.unit = unit

    session.flush()
    return recipe_ingredient

def delete_recipe_ingredient(
    session: Session,
    recipe_id: int,
    ingredient_id: int,
) -> bool:
    recipe_ingredient = get_recipe_ingredient(
    session,
    recipe_id,
    ingredient_id,
    )

    if recipe_ingredient is None:
        return False

    session.delete(recipe_ingredient)
    session.flush()
    return True