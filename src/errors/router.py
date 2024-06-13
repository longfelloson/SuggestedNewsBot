from aiogram import Router
from aiogram.types import ErrorEvent

router = Router(name="Errors")


@router.errors()
async def errors_handler(error: ErrorEvent) -> None:
    """
    Обработка всех ошибок
    """
    exception_text = str(error.exception)

    if not exception_text:
        exception_text = "Возникла непредвиденная ошибка в работе бота ⚠️"

    if error.update.callback_query:
        await error.update.callback_query.message.reply(exception_text)
    else:
        await error.update.message.reply(exception_text)
