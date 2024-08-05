import urllib
import asyncio
import logging
import sys
import json

from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


config = dotenv_values("./.env")


TOKEN = config["BOT_TOKEN"]
WEB_APP_ENDPOINT = 'http://localhost:80/api/v1'


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!"
        f"\n\n/messages - go get all messages"
        f"\n/delete - to delete all messages (dev)"
        "\n\nAny `text` messages will be sent (created)"
    )


@dp.message(Command('messages'))
async def get_messages(message: Message) -> None:
    """ Returns created messages (n_messages=20)
    """
    result = ""
    messages = json.load(
        urllib.request.urlopen(f"{WEB_APP_ENDPOINT}/messages/")
    )
    for msg in messages:
        result += f"✅ {msg}\n"
    await message.reply(
        text=result if result else "No messages"
    )


@dp.message(Command('delete'))
async def get_messages(message: Message) -> None:
    """ Deletes all messages
    """
    resp = urllib.request.urlopen(
        urllib.request.Request(
            f"{WEB_APP_ENDPOINT}/messages/",
            method="DELETE"
        )
    ).getcode()
    await message.reply(
        text="❌ Fail" if resp != 200 else "✅ Deleted"
    )


@dp.message(F.text)
async def create_message(message: Message) -> None:
    """ Creates a message
    """
    data = urllib.parse.urlencode({
        "message": message.text
    })
    resp = urllib.request.urlopen(
        urllib.request.Request(
            f"{WEB_APP_ENDPOINT}/message/?{data}",
            method="POST"
        )
    ).getcode()
    await message.reply(
        text="❌ Fail" if resp != 200 else "✅ Sent"
    )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
