from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.news.filters import BlockedUserFilter
from src.users import crud as users_crud

router = Router()


@router.message(CommandStart(), BlockedUserFilter())
async def start_command_handler(message: Message, session: AsyncSession):
    """

    """
    if not await users_crud.get_user(message.from_user.id, session):
        await users_crud.add_user(message.from_user.id, session)

    await message.reply("Приветствуем!")
