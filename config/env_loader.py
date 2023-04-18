import os

from dotenv import load_dotenv


load_dotenv()

tg_bot_token = os.environ['TG_BOT_TOKEN']
backend_url = os.environ['BACKEND_URL']
