from sqlalchemy import select
from sqlalchemy.orm import Session

from models.recipe import Recipe

def create_recipe(
    session: Session,
    user_id: int,
    category_id: int,
    title: str,
    instructions: str,
    prep_time_minutes: int,
) -> Recipe:
    recipe = Recipe(
    user_id=user_id,
    category_id=category_id,
    title=title,
    instructions=instructions,
    prep_time_minutes=prep_time_minutes,
)

    session.add(recipe)
    session.flush()
    return recipe

def get_recipe(
    session: Session,
    recipe_id: int,
) -> Recipe | None:
    return session.get(Recipe, recipe_id)

def list_recipes(session: Session) -> list[Recipe]:
    statement = select(Recipe).order_by(Recipe.id)
    return list(session.scalars(statement).all())

def get_recipes_by_user(
    session: Session,
    user_id: int,
) -> list[Recipe]:
    statement = (
        select(Recipe)
        .where(Recipe.user_id == user_id)
        .order_by(Recipe.id)
)

    return list(session.scalars(statement).all())

def get_recipes_by_category(
    session: Session,
    category_id: int,
) -> list[Recipe]:
    statement = (
        select(Recipe)
        .where(Recipe.category_id == category_id)
        .order_by(Recipe.id)
)

    return list(session.scalars(statement).all())

def update_recipe(
    session: Session,
    recipe_id: int,
    title: str,
    instructions: str,
    prep_time_minutes: int,
) -> Recipe | None:
    recipe = get_recipe(session, recipe_id)

    if recipe is None:
        return None

    recipe.title = title
    recipe.instructions = instructions
    recipe.prep_time_minutes = prep_time_minutes

    session.flush()
    return recipe

def delete_recipe(
    session: Session,
    recipe_id: int,
) -> bool:
    recipe = get_recipe(session, recipe_id)

    if recipe is None:
        return False

    session.delete(recipe)
    session.flush()
    return True