import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import admin_handlers, user_handlers, survey

async def main():
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher(storage=survey.storage)

    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(survey.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
