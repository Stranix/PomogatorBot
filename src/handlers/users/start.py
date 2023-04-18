import aiogram.utils.markdown as md

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from config import dp
from src.services import get_user_from_service
from src.services import send_message_for_admin


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    """
    Для начала проверяю регистрацию.
    Если пользователя нет в системе, приветствую и отправляю данные на проверку
    Если пользователь есть, говорю что я его знаю и может быть даю справку по боту

    :param message:
    :return:
    """
    user = await get_user_from_service(message.from_user.id)
    if user:
        message_for_send = md.text('Приветствую {}'.format(user.full_name))
        await message.answer(message_for_send)
        return

    message_for_send = md.text(
        'Приветствую, я бот отдела R&D!\n'
        'Мы с вами не знакомы, поэтому отправил ваши данные на проверку '
        'Константину.\n'
        'Для того чтобы продолжить пользоваться ботом, дождитесь '
        'сообщения о успешной регистрации!')

    await send_message_for_admin(
        md.text('Запрос на регистрацию:\n') +
        md.hcode(message.from_user)
    )

    await message.answer(message_for_send)
