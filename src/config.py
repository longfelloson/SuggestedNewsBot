import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMINS_IDS = [int(ADMIN_ID) for ADMIN_ID in os.getenv('ADMINS_IDS').split()] if os.getenv('ADMINS_IDS') else []
CHAT_ID = int(os.getenv('CHAT_ID')) if os.getenv('CHAT_ID') else None

DATABASE_URL = os.getenv('DATABASE_URL')
