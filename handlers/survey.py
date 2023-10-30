from aiogram import Router, Bot
from aiogram.filters import StateFilter
from aiogram.filters import Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove as Rep_Rem
from keyboards import keyboards as kbs
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config

config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token)
storage: MemoryStorage = MemoryStorage()
router: Router = Router()

class data(StatesGroup):
    fio = State()
    nickname = State()
    bio = State()
    course = State()
    survey_text = State()
# вместо покупки курса в данный момент мы сначала
# заполним анкету, а потом выберем курс и в конце покажем,
# что и как

@router.callback_query(Text('buy_pressed'), StateFilter(default_state))
async def survey(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text='Сейчас вы заполните анкету, которая будет ' \
                                  'отправлена преподу выбранного вами курса. ')
    await callback.message.answer(text='Введите ваше ФИО, например \nИванов Иван Иванович')
    await state.set_state(data.fio)

@router.message(StateFilter(data.fio))
async def survey_get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer('Теперь введите свой никнейм в Телеграм в формате\n' \
                         '@abcdeshka')
    await state.set_state(data.nickname)

@router.message(StateFilter(data.nickname))
async def survey_get_nick(message: Message, state: FSMContext):
    await state.update_data(nick=message.text)
    await message.answer('Последнее - расскажите немного о себе, нам важно знать, ' \
                         'с кем мы работаем :)')
    await state.set_state(data.bio)

@router.message(StateFilter(data.bio))
async def survey_get_bio(message: Message, state: FSMContext):
    await state.update_data(bio=message.text)
    await message.answer(
        text='Выберите курс, который хотите приобрести',
        reply_markup=kbs.buy_course_kd
    )
    await state.set_state(data.course)

@router.message(StateFilter(data.course))
async def survey_get_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    surv: dict[str, str | int | bool] = await state.get_data()
    await message.answer(text='Отлично!', reply_markup=Rep_Rem())
    # await state.clear()
    await message.answer('Вот твоя анкета, которая отправится преподу:')
    survey_text = f'Меня зовут {surv["fio"]}. \n'
    survey_text += f'Мой ник {surv["nick"]}. \n'
    survey_text += f'О себе: \n{surv["bio"]} \n'
    survey_text += f'Выбранный мною курс {surv["course"]}.'
    await state.update_data(survey_text=survey_text)
    await message.answer(text=survey_text + '\nОтправляем преподу?', 
                         reply_markup=kbs.yes_no)

@router.callback_query(Text('yes_but_pressed'))
async def send_survey_to_tutor(callback: CallbackQuery, state: FSMContext):
    await callback.answer('(типа отправлено преподу, все ок)')
    # здесь нужен бот для того, чтобы отослать сообщение в группу
    surv: dict[str, str | int | bool] = await state.get_data()
    # print(surv["survey_text"])
    await bot.send_message(config.tg_bot.group_id, surv["survey_text"])
    await callback.message.answer(text='Отлично, если нужно, ознакомьтесь ' \
                                  'с информацией о курсах',
        reply_markup=kbs.main_kd)
    