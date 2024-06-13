from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from src import config
from src.app.loader import bot
from src.news import crud

router = Router()


@router.callback_query(F.data.regexp("hide_keyboard"))
async def hide_keyboard(call: CallbackQuery, session: AsyncSession):
    """
    Hide keyboard buttons
    """
    news = await crud.get_news(session, id_=call.data.split("*")[1])

    await bot.answer_callback_query(call.id)
    await bot.delete_message(config.CHAT_ID, news.chat_message_id)
    await call.message.delete()


@router.callback_query(F.data.regexp("block_user"))
async def block_user(call: CallbackQuery, session: AsyncSession):
    """
    Block user
    """
    user_for_block_id = call.data.split("*")[1]

    await bot.answer_callback_query(call.id)
    await users_crud.change_user(user_for_block_id, session)
