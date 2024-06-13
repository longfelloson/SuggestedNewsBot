from aiogram.types import BotCommand

from src import database
from src.app.commands.router import router as command_router
from src.app.loader import bot, dp
from src.app.middlewares import Middleware
from src.errors.router import router as error_router
from src.news.routers.call import router as news_call_router
from src.news.routers.message import router as news_message_router


async def set_commands() -> None:
    """
    Установка команд по умолчанию
    """
    commands = [
        BotCommand(command="/start", description="Запуск бота"),
        BotCommand(command="/config", description="Настройки бота")
    ]
    await bot.set_my_commands(commands)


async def startup() -> None:
    """
    Запуск основных процессов для бота
    """
    dp.include_routers(command_router, news_message_router, news_call_router, error_router)
    dp.message.outer_middleware.register(Middleware())
    dp.callback_query.outer_middleware.register(Middleware())

    await database.create_tables()
    await set_commands()
    await dp.start_polling(bot)
