from sqlalchemy import select
from sqlalchemy.orm import Session

from models.ingredient import Ingredient

def create_ingredient(session: Session, name: str) -> Ingredient:
    ingredient = Ingredient(name=name)
    session.add(ingredient)
    session.flush()
    return ingredient

def get_ingredient(
    session: Session,
    ingredient_id: int,
) -> Ingredient | None:
    return session.get(Ingredient, ingredient_id)

def get_ingredient_by_name(
    session: Session,
    name: str,
) -> Ingredient | None:
    statement = select(Ingredient).where(
        Ingredient.name == name
)
    return session.scalars(statement).first()

def list_ingredients(session: Session) -> list[Ingredient]:
    statement = select(Ingredient).order_by(Ingredient.id)
    return list(session.scalars(statement).all())

def update_ingredient(
    session: Session,
    ingredient_id: int,
    new_name: str,
) -> Ingredient | None:
    ingredient = get_ingredient(session, ingredient_id)

    if ingredient is None:
        return None

    ingredient.name = new_name
    session.flush()
    return ingredient

def delete_ingredient(
    session: Session,
    ingredient_id: int,
) -> bool:
    ingredient = get_ingredient(session, ingredient_id)

    if ingredient is None:
        return False

    session.delete(ingredient)
    session.flush()
    return True