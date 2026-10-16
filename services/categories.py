from sqlalchemy import select
from sqlalchemy.orm import Session

from models.category import Category

def create_category(session: Session, name: str) -> Category:
    category = Category(name=name)
    session.add(category)
    session.flush()
    return category

def get_category(session: Session, category_id: int) -> Category | None:
    return session.get(Category, category_id)

def get_category_by_name(session: Session, name: str) -> Category | None:
    statement = select(Category).where(Category.name == name)
    return session.scalars(statement).first()

def list_categories(session: Session) -> list[Category]:
    statement = select(Category).order_by(Category.id)
    return list(session.scalars(statement).all())

def update_category(
    session: Session,
    category_id: int,
    new_name: str,
) -> Category | None:
    category = get_category(session, category_id)

    if category is None:
        return None

    category.name = new_name
    session.flush()
    return category

def delete_category(session: Session, category_id: int) -> bool:
    category = get_category(session, category_id)

    if category is None:
        return False

    session.delete(category)
    session.flush()
    return True