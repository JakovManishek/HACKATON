from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import db_functions
import text
from math import ceil

    

def inline_category() -> InlineKeyboardMarkup:


    kb = [
        [InlineKeyboardButton(text="Продукты", callback_data="products")],
        [InlineKeyboardButton(text="Медицина", callback_data="medic")],
        [InlineKeyboardButton(text="Топливо", callback_data="fuel")],
        [InlineKeyboardButton(text="Вещи", callback_data="clothing")],
        [InlineKeyboardButton(text="Образование", callback_data="education")],
        [InlineKeyboardButton(text="Косметика", callback_data="cosmetics")],
        [InlineKeyboardButton(text="Электроника", callback_data="electronics")],
        [InlineKeyboardButton(text="Развлечения", callback_data="entertaiments")],
        [InlineKeyboardButton(text="Рестораны", callback_data="restaraunt")],
        [InlineKeyboardButton(text="Транспорт", callback_data="transport")],
        [InlineKeyboardButton(text="Спорт", callback_data="sport")],
        [InlineKeyboardButton(text="Такси", callback_data="taxi")],
        [InlineKeyboardButton(text="Путешествия", callback_data="travels")]
  ]

    
    return InlineKeyboardMarkup(inline_keyboard=kb, resize_keyboard=True, row_width=1)




def add_card() -> InlineKeyboardMarkup:

    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="добавить карту", callback_data="add")]],
                               resize_keyboard=True,
                               row_width=1,
                               input_field_placeholder=text.choose_private_kb)




def reply_off_add_kb() -> ReplyKeyboardMarkup:
    kb = [[KeyboardButton(text="Завершить добавление")]]

    return ReplyKeyboardMarkup(keyboard=kb,
                               resize_keyboard=True,
                               row_width=1,
                               input_field_placeholder=text.choose_private_kb)

