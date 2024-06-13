from typing import Optional

from sqlalchemy import insert, select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.news.models import News
from src.news.schemas import NewsSchema


async def add_news(news: NewsSchema, session: AsyncSession) -> None:
    """
    Adds new news to the database.
    """
    await session.execute(insert(News).values(**news.model_dump()))
    await session.commit()


async def get_news(session: AsyncSession, **filters) -> Optional[News]:
    """
    Gets news from the database.
    """
    conditions = [getattr(News, key) == value for key, value in filters.items()]
    news = await session.execute(select(News).where(and_(*conditions)))
    return news.scalar_one_or_none()
