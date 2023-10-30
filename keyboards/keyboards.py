from aiogram.types import InlineKeyboardButton as Inl_B, \
                          InlineKeyboardMarkup as Inl_Markup
from aiogram.types import KeyboardButton as Key_B, ReplyKeyboardMarkup as Rep_Markup
# keyboard = kd, kbd, keybd

start_button: Inl_B = Inl_B(
    text='Нажми, чтобы узнать, чем я могу помочь',
    callback_data='start_pressed'
)

go_to_main_kd: Inl_B = Inl_B(
    text='Назад',
    callback_data='start_pressed'
)

buy_course: Inl_B = Inl_B(
    text='Купить курс или связку',
    callback_data='buy_pressed'
)

course_info: Inl_B = Inl_B(
    text='Получить информацию о всех курсах',
    callback_data='info_pressed'
)

course_1: Inl_B = Inl_B(
    text='Все о курсе 1',
    callback_data='course_1_pressed'
)

course_2: Inl_B = Inl_B(
    text='Все о курсе 2',
    callback_data='course_2_pressed'
)

course_3: Inl_B = Inl_B(
    text='Все о курсе 3',
    callback_data='course_3_pressed'
)

course_4: Inl_B = Inl_B(
    text='Все о курсе 4',
    callback_data='course_4_pressed'
)

buy_c_1: Key_B = Key_B(
    text='математика',
    callback_data='buy_c_1_pressed'
)

buy_c_2: Key_B = Key_B(
    text='физика',
    callback_data='buy_c_2_pressed'
)

buy_c_3: Key_B = Key_B(
    text='русский язык',
    callback_data='buy_c_3_pressed'
)

buy_c_4: Key_B = Key_B(
    text='биология',
    callback_data='buy_c_4_pressed'
)

yes_but: Inl_B = Inl_B(
    text='Да',
    callback_data='yes_but_pressed'
)

no_but: Inl_B = Inl_B(
    text='Нет, переделаем',
    callback_data='buy_pressed'
)

start_kd: Inl_Markup = Inl_Markup(
    inline_keyboard=[
        [start_button],
        [buy_course]
    ]
)

main_kd: Inl_Markup = Inl_Markup(
    inline_keyboard=[
        [course_info],
        [buy_course]
    ]
)

info_about_courses: Inl_Markup = Inl_Markup(
    inline_keyboard=[
        [course_1],
        [course_2],
        [course_3],
        [course_4],
        [go_to_main_kd]
    ]
)

buy_course_kd: Rep_Markup = Rep_Markup(
    keyboard=[
        [buy_c_1],
        [buy_c_2],
        [buy_c_3],
        [buy_c_4],
    ]
)

yes_no: Inl_Markup = Inl_Markup(
    inline_keyboard=[
        [yes_but, no_but]
    ]
)