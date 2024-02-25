from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from schemas import UserModel

async def get_user_by_email(email: str, db: Session) -> User:
    """
    Get a user by email from the database.

    Args:
        email (str): Email address of the user.
        db (Session): Database session.

    Returns:
        User: User object if found, None otherwise.
    """
    return db.query(User).filter(User.email == email).first()

async def create_user(body: UserModel, db: Session) -> User:
    """
    Create a new user in the database.

    Args:
        body (UserModel): User data.
        db (Session): Database session.

    Returns:
        User: Newly created user object.
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    Update the refresh token for a user.

    Args:
        user (User): User object.
        token (str | None): New refresh token or None.
        db (Session): Database session.
    """
    user.refresh_token = token
    db.commit()

async def confirmed_email(email: str, db: Session) -> None:
    """
    Mark the user's email as confirmed.

    Args:
        email (str): Email address to confirm.
        db (Session): Database session.
    """
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()

async def update_avatar(email, url: str, db: Session) -> User:
    """
    Update the avatar URL for a user.

    Args:
        email (str): Email address of the user.
        url (str): New avatar URL.
        db (Session): Database session.

    Returns:
        User: User object with updated avatar URL.
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user
