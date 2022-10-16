import asyncio
from utils.secrets import read_secrets
from aiogram import Bot, Dispatcher, types

secrets = read_secrets()

BOT_TOKEN = secrets["TELEGRAM_BOT_TOKEN"]
FRONTEND_URL = secrets["FRONTEND_URL"]


async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )


async def echo_handler(event: types.Message):
    await event.answer(event.text)


async def main():
    bot = Bot(token=BOT_TOKEN)

    web_app_info = types.WebAppInfo(url=FRONTEND_URL)
    menu_button = types.MenuButtonWebApp("text", web_app_info)
    await bot.set_chat_menu_button(None, menu_button)

    try:
        dispatcher = Dispatcher(bot=bot)

        dispatcher.register_message_handler(start_handler, commands={"start", "restart"})
        dispatcher.register_message_handler(echo_handler)

        await dispatcher.start_polling()
    finally:
        await bot.close()


asyncio.run(main())
