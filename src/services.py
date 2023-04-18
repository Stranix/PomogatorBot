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
    await bot.send_message(config.tg_admin_id, message)


async def is_admin(tg_id: int) -> bool:
    if tg_id != config.tg_admin_id:
        return False
    return True
