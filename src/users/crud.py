from typing import Optional

from sqlalchemy import insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User


async def get_user(user_id: int, session: AsyncSession) -> Optional[User]:
    """
    Adds a new user to the database.
    """
    user = await session.execute(select(User).where(User.user_id == user_id))
    return user.scalar_one_or_none()


async def add_user(user_id: int, session: AsyncSession) -> None:
    """
    Adds a new user to the database.
    """
    await session.execute(insert(User).values(user_id=user_id))
    await session.commit()


async def block_user(user_id: int, session: AsyncSession) -> None:
    """
    Changes user column "is_blocked" to True
    """
    await session.execute(update(User).where(User.user_id == user_id).values(is_blocked=True))
    await session.commit()


async def is_blocked(user_id: int, session: AsyncSession) -> Optional[bool]:
    """
    Gets boolean value of a user's "is_blocked" column
    """
    is_blocked_column = await session.execute(select(User.is_blocked).where(User.user_id == user_id))
    return is_blocked_column.scalar_one_or_none()
