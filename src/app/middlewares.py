from typing import Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from src.database import get_async_session


class Middleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: Dict[str, Any]) -> Any:
        async for session in get_async_session():
            data['session'] = session
            return await handler(event, data)
