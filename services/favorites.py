from sqlalchemy import select
from sqlalchemy.orm import Session
from models.favorite import Favorite


def add_favorite(
    session: Session,
    user_id: int,
    recipe_id: int,
) -> Favorite:
    favorite = Favorite(
        user_id=user_id,
        recipe_id=recipe_id,
)

    session.add(favorite)
    session.flush()
    return favorite

def get_favorite(
    session: Session,
    user_id: int,
    recipe_id: int,
) -> Favorite | None:
    return session.get(
        Favorite,
        (user_id, recipe_id),
)

def list_user_favorites(
    session: Session,
    user_id: int,
) -> list[Favorite]:
    statement = (
        select(Favorite)
        .where(Favorite.user_id == user_id)
        .order_by(Favorite.recipe_id)
)

    return list(session.scalars(statement).all())

def list_recipe_favorites(
    session: Session,
    recipe_id: int,
) -> list[Favorite]:
    statement = (
        select(Favorite)
        .where(Favorite.recipe_id == recipe_id)
        .order_by(Favorite.user_id)
)

    return list(session.scalars(statement).all())

def delete_favorite(
    session: Session,
    user_id: int,
    recipe_id: int,
) -> bool:
    favorite = get_favorite(
        session,
        user_id,
        recipe_id,
)

    if favorite is None:
        return False

    session.delete(favorite)
    session.flush()
    return True