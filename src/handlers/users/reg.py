import requests
import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types

import config
from config import dp
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from src.schemas import User
from src.services import is_admin

logger = logging.getLogger(__name__)


class RegState(StatesGroup):
    user = State()


@dp.message_handler(Command('reg'))
async def request_user(message: types.Message):
    if not await is_admin(message.from_user.id):
        await message.answer('Нет доступа к данной команде')
    await RegState.user.set()
    await message.answer('Ожидаю данные пользователя для регистрации')


@dp.message_handler(state=RegState.user, content_types=types.ContentType.TEXT)
async def reg_user(message: types.Message, state: FSMContext):
    parse_text_answer = message.text.split(',')

    user = User(
        full_name=parse_text_answer[0],
        tg_id=int(parse_text_answer[1]),
        btrx_id=int(parse_text_answer[2]),
        is_admin=False
    )

    logger.debug(user)
    if await _send_req_to_create_user(user):
        await config.bot.send_message(user.tg_id, 'Вы зарегистрированы!')
        await message.answer('Пользователь зарегистрирован')

    await state.finish()


async def _send_req_to_create_user(user: User) -> bool:
    url = config.backend_url + '/user/'
    payloads = user.__dict__
    del payloads['id']
    logger.debug(payloads)
    response = requests.post(url, json=payloads)

    if response.status_code != 201:
        return False

    return True
