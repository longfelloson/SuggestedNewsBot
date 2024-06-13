from aiogram.filters import Filter
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from src import config
from src.news import crud
from src.news.exceptions import UserIsAdmin, ChannelTypeError
from src.users import crud as users_crud


class NotAdminFilter(Filter):
    async def __call__(self, message: Message):
        """
        Filter that checks if a user is not an administrator to get possibility to send news
        """
        if message.from_user.id not in config.ADMINS_IDS:
            return True
        raise UserIsAdmin("Вы - администратор 🤷‍♂️")


class BlockedUserFilter(Filter):
    async def __call__(self, message: Message, session: AsyncSession):
        """
        Filter that checks if a user is blocked from sending news
        """
        user = await users_crud.get_user(message.from_user.id, session)
        if not user or user.is_blocked:
            return True
        raise UserIsAdmin("Вы заблокированы в боте ⛔️")


class NewsFilter(Filter):
    async def __call__(self, message: Message, session: AsyncSession):
        """
        Check chat
        """
        news = await crud.get_news(
            session,
            from_channel_id=message.forward_from_chat.id,
            from_channel_message_id=message.forward_from_message_id
        )
        if news:
            raise ChannelTypeError("Эту новость уже присылали в бота ⚠️")

        if not message.forward_from_chat:
            raise ChannelTypeError("Сообщение должно быть переслано из канала ⚠️")

        conditions = [
            message.chat.id != config.CHAT_ID,
            not message.media_group_id,
            message.forward_from_chat.type == "channel"
        ]
        return all(conditions)
