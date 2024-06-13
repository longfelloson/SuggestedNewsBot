import random

from aiogram.types import Message


def get_sender_info(message: Message) -> str:
    """
    Gets sender info from a message
    """
    return f'От <a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>'


def get_random_integer() -> int:
    """
    Gets random integer
    """
    return random.randint(1111111111, 9999999999)
