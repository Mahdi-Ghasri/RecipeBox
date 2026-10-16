from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User

def create_user(session: Session, email: str) -> User:
    user = User(email=email)

    session.add(user)
    session.flush()

    return user

def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)

def get_user_by_email(
    session: Session,
    email: str,
) -> User | None:
    statement = select(User).where(User.email == email)

    return session.scalars(statement).first()

def list_users(session: Session) -> list[User]:
    statement = select(User).order_by(User.id)

    return list(session.scalars(statement).all())

def update_user_email(
    session: Session,
    user_id: int,
    new_email: str,
) -> User | None:
    user = session.get(User, user_id)

    if user is None:
        return None

    user.email = new_email
    session.flush()

    return user

def delete_user(session: Session, user_id: int) -> bool:
    user = session.get(User, user_id)

    if user is None:
        return False

    session.delete(user)
    session.flush()

    return True