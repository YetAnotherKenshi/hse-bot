from aiogram import types
import numpy as np
import os
from bot import bot
from bot import dp
from math_module import remove_file, determinant, inverse, power, solve, check_matrix_issquare
from db import db_service
from utils import save_feedback
import markup as nav
from states import States
from colors import color_schemes

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Хэндлер команды start"""
    cid = str(message["from"]["id"])
    db_service.add_user(cid)
    await message.answer("Привет! Меня зовут Лин-А\nЯ — телеграм-бот, который немного разбирается в линейной алгебре.", reply_markup=nav.greeting)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """Хэндлер команды help"""
    await message.answer("""
Основные функции

Этот бот позволяет пользователю производить некоторые операции из линейной алгебры:

— Вычислить определитель матрицы
— Найти обратную матрицу
— Возвести матрицу в степень
— Решить систему линейных уравнений

Как вводить данные

Чтобы ввести матрицу используйте пробелы, чтобы разделить числа, и точку с запятой в окончании каждого ряда.

Например, вот так может выглядеть квадратная матрица 3x3:
1 4 3; 0 0 4; 3 6 5

А вот так 3x2:
4 3; -4  1; 9 -1

Также вы можете выбрать одну из предложенных цветовых тем для отрисовки результата.""")

@dp.callback_query_handler()
async def change_msg(callback: types.CallbackQuery):
    """Хэндлер callback функции"""
    text = ""
    markup = ""
    cid = str(callback.message["chat"]["id"])

    # Вызов главного меню
    if callback.data in ["menu_open", "back"]:
        text = "Могу помочь тебе с некоторыми задачками. Вот, что я умею:"
        markup = nav.menu
        db_service.update_user_state(cid, States.MAIN_MENU)
        db_service.update_user_storage(cid, [])
        await callback.message.edit_text(text, reply_markup=markup)

    # Вызов меню функции нахождения определителя матрицы
    if callback.data == "det":
        text = 'Введите квадратную матрицу, разделяя строки знаком ;\nНапример, "1 2; 3 4"'
        markup = nav.back
        db_service.update_user_state(cid, States.DET)
        await callback.message.edit_text(text, reply_markup=markup)

    # Вызов меню функции нахождения обратной матрицы
    if callback.data == "inv":
        text = 'Введите квадратную матрицу, разделяя строки знаком ;\nНапример, "1 2; 3 4"'
        markup = nav.back
        db_service.update_user_state(cid, States.INV)
        await callback.message.edit_text(text, reply_markup=markup)

    # Вызов меню функции возведения матрицы в степень
    if callback.data == "pow":
        text = 'Введите квадратную матрицу, разделяя строки знаком ;\nНапример, "1 2; 3 4"'
        markup = nav.back
        db_service.update_user_state(cid, States.POWER)
        await callback.message.edit_text(text, reply_markup=markup)

    # Вызов меню функции возведения матрицы в степень
    if callback.data == "solve":
        text = 'Введите квадратную матрицу, разделяя строки знаком ;\nНапример, "1 2; 3 4"'
        markup = nav.back
        db_service.update_user_state(cid, States.SOLVE)
        await callback.message.edit_text(text, reply_markup=markup)

    # Вызов меню настроек
    if callback.data == "settings":
        photo = types.InputFile("images/themes.png")
        text = "Здесь ты можешь поменять стиль изображения.\nВсе доступные стили ты можешь увидеть выше"
        markup = nav.schemes
        db_service.update_user_state(cid, States.SETTINGS)
        await bot.send_photo(cid, photo)
        await bot.send_message(cid, text, reply_markup=markup)

    # Вызов меню обратной связи
    if callback.data == "feedback":
        text = 'Если у тебя есть предложение, что здесь можно улучшить, мой разработчик с радостью прислушается к твоему мнению!\nОставь сообщение ниже:'
        markup = nav.back
        db_service.update_user_state(cid, States.FEEDBACK)
        await callback.message.edit_text(text, reply_markup=markup)

    # Обработка смены цветовой схемы
    if "scheme" in callback.data:
        text = 'Успешно выполнено!'
        markup = nav.menu
        db_service.update_user_color(cid, color_schemes[callback.data[-1]])
        db_service.update_user_state(cid, States.MAIN_MENU)
        await callback.message.edit_text(text, reply_markup=markup)

@dp.message_handler()
async def send_message(message: types.Message):
    """Хэндлер сообщений"""

    cid = str(message["from"]["id"])
    state = db_service.get_user_state(cid)
    storage = db_service.get_user_storage(cid)
    color = db_service.get_user_color(cid)
    message_text = message.text
    images_path = "images"

    # Обработка сообщения с изначальным состоянием
    if state == States.MAIN_MENU:
        await bot.send_message(cid, "Я не знаю, чего ты хочешь. Сначала выбери функцию, и я с радостью тебе помогу", reply_markup=nav.menu)
    
    # Обработка функции нахождения определителя матрицы
    elif state == States.DET:
        try:
            storage.append(message_text)
            photo_id = determinant(*storage, color, cid) 
            matrix = open(os.path.join(images_path, f'{photo_id}.png'), 'rb')
            await bot.send_photo(message.chat.id, matrix)
            remove_file(photo_id, images_path)
            storage = []
            db_service.update_user_storage(cid, storage)
            db_service.update_user_state(cid, States.MAIN_MENU)
            await bot.send_message(cid, "Что делаем дальше?", reply_markup=nav.menu)
        except np.linalg.LinAlgError:
            await bot.send_message(cid, "Вы ввели не квадратную матрицу!", reply_markup=nav.back)
        except ValueError:
            await bot.send_message(cid, "Вы ввели неправильную матрицу!", reply_markup=nav.back)
    
    # Обработка функции нахождения обратной матрицы
    elif state == States.INV:
        try:
            storage.append(message_text)
            photo_id = inverse(*storage, color, cid) 
            matrix = open(os.path.join(images_path, f'{photo_id}.png'), 'rb')
            await bot.send_photo(message.chat.id, matrix)
            remove_file(photo_id, images_path)
            storage = []
            db_service.update_user_storage(cid, storage)
            db_service.update_user_state(cid, States.MAIN_MENU)
            await bot.send_message(cid, "Что делаем дальше?", reply_markup=nav.menu)
        except np.linalg.LinAlgError:
            await bot.send_message(cid, "Вы ввели не квадратную матрицу!", reply_markup=nav.back)
        except ValueError:
            await bot.send_message(cid, "Вы ввели неправильную матрицу!", reply_markup=nav.back)
    
    # Обработка 1 этапа функции возведения матрицы в степень
    elif state == States.POWER:
        try:
            check_matrix_issquare(message_text)
            storage.append(message_text)
            await bot.send_message(cid, "В какую степень возводим?", reply_markup=nav.back)
            db_service.update_user_state(cid, States.POWER_WAIT)
            db_service.update_user_storage(cid, storage)
        except np.linalg.LinAlgError:
            await bot.send_message(cid, "Вы ввели не квадратную матрицу!", reply_markup=nav.back)
        except ValueError:
            await bot.send_message(cid, "Вы ввели неправильную матрицу!", reply_markup=nav.back)
    
    # Обработка 2 этапа функции возведения матрицы в степень
    elif state == States.POWER_WAIT:
        try:
            storage.append(int(message_text))
            photo_id = power(*storage, color, cid) 
            matrix = open(os.path.join(images_path, f'{photo_id}.png'), 'rb')
            await bot.send_photo(message.chat.id, matrix)
            remove_file(photo_id, images_path)
            storage = []
            db_service.update_user_state(cid, States.MAIN_MENU)
            db_service.update_user_storage(cid, storage)
            await bot.send_message(cid, "Что делаем дальше?", reply_markup=nav.menu)
        except ValueError:
            await bot.send_message(cid, "Вы ввели не число!", reply_markup=nav.back)
    
    # Обработка 1 этапа функции решения системы линейных уравнений
    elif state == States.SOLVE:
        try:
            check_matrix_issquare(message_text)
            storage.append(message_text)
            await bot.send_message(cid, "Введите вектор", reply_markup=nav.back)
            db_service.update_user_state(cid, States.SOLVE_WAIT)
            db_service.update_user_storage(cid, storage)
        except np.linalg.LinAlgError:
            await bot.send_message(cid, "Вы ввели не квадратную матрицу!", reply_markup=nav.back)
        except ValueError:
            await bot.send_message(cid, "Вы ввели неправильную матрицу!", reply_markup=nav.back)
    
    # Обработка 1 этапа функции решения системы линейных уравнений
    elif state == States.SOLVE_WAIT:
        try:
            storage.append(message_text)
            photo_id = solve(*storage, color, cid) 
            matrix = open(os.path.join(images_path, f'{photo_id}.png'), 'rb')
            await bot.send_photo(message.chat.id, matrix)
            remove_file(photo_id, images_path)
            storage = []
            db_service.update_user_state(cid, States.MAIN_MENU)
            db_service.update_user_storage(cid, storage)
            await bot.send_message(cid, "Что делаем дальше?", reply_markup=nav.menu)
        except ValueError:
            await bot.send_message(cid, "Вектор неправильной длины!", reply_markup=nav.back)
    elif state == States.FEEDBACK:
        result = save_feedback(cid, message_text)
        if result != None:
            await bot.send_message(cid, "Спасибо за обратную связь!", reply_markup=nav.menu)
        else:
            await bot.send_message(cid, "Упс! Что-то пошло не так... Попробуй ещё раз.", reply_markup=nav.menu)
