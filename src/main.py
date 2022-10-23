import asyncio

from src.callback_handler import process_callback
from src.routing import Routing
from src.services.start.start_service import start_handler
from utils.secrets import read_secrets
from aiogram import Bot, Dispatcher, types

secrets = read_secrets()

BOT_TOKEN = secrets["TELEGRAM_BOT_TOKEN"]
FRONTEND_URL = secrets["FRONTEND_URL"]


async def setup_bot_frontend(bot: Bot):
    web_app_info = types.WebAppInfo(url=FRONTEND_URL)
    menu_button = types.MenuButtonWebApp("text", web_app_info)
    await bot.set_chat_menu_button(None, menu_button)


def map_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(start_handler, commands={Routing.START_ROUTE})
    dispatcher.register_callback_query_handler(process_callback)


async def main():
    bot = Bot(token=BOT_TOKEN)

    await setup_bot_frontend(bot)

    try:
        dispatcher = Dispatcher(bot=bot)

        map_handlers(dispatcher)

        await dispatcher.start_polling()
    finally:
        await bot.close()


asyncio.run(main())
