import config
import src.handlers

from aiogram import executor


def main():
    executor.start_polling(config.dp)


if __name__ == '__main__':
    main()
