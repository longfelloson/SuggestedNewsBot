from aiogram.types import InlineKeyboardMarkup as InlineKeyboard, InlineKeyboardButton as InlineButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder as InlineBuilder

from src.news.models import News


def news_keyboard(news: News, message: Message) -> InlineKeyboard:
    """
    Keyboard with news actions buttons
    """
    builder = InlineBuilder().row(
        InlineButton(text="Просмотрено ✅", callback_data=f"hide_keyboard*{news.id_}"),
        InlineButton(text="Заблокировать ⛔️", callback_data=f"block_user*{message.from_user.id}"),
    )
    return builder.as_markup()
