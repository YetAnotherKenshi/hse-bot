from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


greeting = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Погнали!", callback_data='menu_open'),
        ]
    ],
)
menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Вычислить определитель матрицы", callback_data='det'),
        ],
        [
            InlineKeyboardButton(text="Найти обратную матрицу", callback_data='inv')
        ],
        [
            InlineKeyboardButton(text="Возвести матрицу в степень", callback_data='pow'),
        ],
        [
            InlineKeyboardButton(text="Решить систему линейных уравнений", callback_data='solve'),
        ],
        [
            InlineKeyboardButton(text="Выбрать цветовую схему", callback_data='settings'),
        ],
        [
            InlineKeyboardButton(text="Обратная связь", callback_data='feedback'),
        ],
    ],
)
back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='back'),
        ]
    ],
)

schemes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Стиль 1", callback_data='scheme1'),
        ],
        [
            InlineKeyboardButton(text="Стиль 2", callback_data='scheme2'),
        ],
        [
            InlineKeyboardButton(text="Стиль 3", callback_data='scheme3'),
        ],
        [
            InlineKeyboardButton(text="Стиль 4", callback_data='scheme4'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back'),
        ]
    ],
)