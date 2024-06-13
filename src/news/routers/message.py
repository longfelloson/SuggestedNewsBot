from aiogram import Router
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from src import config
from src.news import crud
from src.news.filters import NotAdminFilter, NewsFilter
from src.news.keyboards import news_keyboard
from src.news.schemas import NewsSchema
from src.news.utils import get_sender_info, get_random_integer

router = Router()


@router.message(NewsFilter(), NotAdminFilter())
async def react_for_suggested_news(message: Message, session: AsyncSession):
    """
    Reacts to suggested news messages
    """
    forwarded_message = await message.forward(config.CHAT_ID)
    news_schema = NewsSchema(
        id_=get_random_integer(),
        from_user_id=forwarded_message.from_user.id,
        from_channel_id=forwarded_message.forward_from_chat.id,
        from_channel_message_id=forwarded_message.forward_from_message_id,
        chat_message_id=forwarded_message.message_id,
    )

    await crud.add_news(news_schema, session)
    await forwarded_message.reply(
        text=f"{get_sender_info(message)}, выберите действие ниже ⤵️",
        reply_markup=news_keyboard(news_schema, message),
        parse_mode="HTML"
    )
    await message.reply("Ваша новость передана на модерацию 🛠")
