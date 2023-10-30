from aiogram import Router
from aiogram.filters import Text, Command
from aiogram.types import Message, CallbackQuery
from keyboards import keyboards as kbs
router: Router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        'Привет, друг, это бот, с помощью которого ты узнаешь \
все о наших курсах, а также сможешь их здесь купить!',
        reply_markup=kbs.start_kd
    )

@router.callback_query(Text('start_pressed'))
async def process_start(callback: CallbackQuery):
    await callback.message.answer(
        text='Здесь будет текст про то, что умеет бот',
        reply_markup=kbs.main_kd
    )
    await callback.answer()

# @router.callback_query(Text('buy_pressed'))
# async def process_buy(callback: CallbackQuery):
#     await callback.message.answer(
#         text='Покупаем курс здесь',
#         reply_markup=kbs.buy_course_kd
#     )
#     await callback.answer()

@router.callback_query(Text('info_pressed'))
async def process_info(callback: CallbackQuery):
    await callback.message.answer(
        text='Вот наши курсы: \n\
1) математика \n\
2) физика \n\
3) русский язык \n\
4) биология',
        reply_markup=kbs.info_about_courses
    )
    await callback.answer()

@router.callback_query(Text('course_1_pressed'))
async def info1(callback: CallbackQuery):
    await callback.message.answer(
        text='Рассказываю обо всем про курс 1'
        # reply_markup=kbs.main_kd
    )
    await callback.answer()

@router.callback_query(Text('course_2_pressed'))
async def info2(callback: CallbackQuery):
    await callback.message.answer(
        text='Рассказываю обо всем про курс 2'
        # reply_markup=kbs.main_kd
    )
    await callback.answer()

@router.callback_query(Text('course_3_pressed'))
async def info3(callback: CallbackQuery):
    await callback.message.answer(
        text='Рассказываю обо всем про курс 3'
        # reply_markup=kbs.main_kd
    )
    await callback.answer()

@router.callback_query(Text('course_4_pressed'))
async def info4(callback: CallbackQuery):
    await callback.message.answer(
        text='Рассказываю обо всем про курс 4'
        # reply_markup=kbs.main_kd
    )
    await callback.answer()
