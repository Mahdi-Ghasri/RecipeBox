from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user_profile import UserProfile

def create_user_profile(
    session: Session,
    user_id: int,
    full_name: str,
    avatar_url: str | None = None,
    bio: str | None = None,
) -> UserProfile:
    profile = UserProfile(
    user_id=user_id,
    full_name=full_name,
    avatar_url=avatar_url,
    bio=bio,
            )

    session.add(profile)
    session.flush()
    return profile

def get_user_profile(
    session: Session,
    user_id: int,
) -> UserProfile | None:
    return session.get(UserProfile, user_id)

def list_user_profiles(
    session: Session,
) -> list[UserProfile]:


    statement = select(UserProfile).order_by(
UserProfile.user_id
)

    return list(session.scalars(statement).all())

def update_user_profile(
    session: Session,
    user_id: int,
    full_name: str,
    avatar_url: str | None = None,
    bio: str | None = None,
) -> UserProfile | None:
    profile = get_user_profile(session, user_id)

    if profile is None:
        return None

    profile.full_name = full_name
    profile.avatar_url = avatar_url
    profile.bio = bio

    session.flush()
    return profile

def delete_user_profile(
    session: Session,
    user_id: int,
) -> bool:
    profile = get_user_profile(session, user_id)

    if profile is None:
        return False

    session.delete(profile)
    session.flush()
    return True