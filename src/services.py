import requests
import config
from src.schemas import User


async def get_user_from_service(tg_user_id: int) -> User | None:
    url = config.backend_url + '/user/{}'.format(tg_user_id)
    response = requests.get(url)
    if response.status_code == 200:
        return User(**response.json())


async def send_message_for_admin(message: str):
    bot = config.bot
    await bot.send_message(378630510, message)
