from aiogram import Router
from aiogram.filters import BaseFilter, Command
from aiogram.types import Message
from config_data.config import load_config

config = load_config()

admin_list: list[int] = config.tg_bot.admin_ids

class IsAdmin(BaseFilter):
    def __init__(self, admin_list: list[int]) -> None:
        self.admin_list = admin_list
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_list

router: Router = Router()
router.message.filter(IsAdmin(admin_list))

@router.message(Command('stats'))
async def admin_stats(message: Message):
    await message.answer('Вы - админ, благодаря IsAdmin вы сможете ' \
                         'использовать дополнительные команды')