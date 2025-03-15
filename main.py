import h_kb
import config
import asyncio
import h_db_func
import h_text



import os
import h_admin


from math import ceil
from time import sleep
from aiogram import Bot, Dispatcher, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession


# session = AiohttpSession(proxy='http://proxy.server:3128')
# bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML), session=session)
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class OrderAdd(StatesGroup):
    # folder_name = State()
    folder_mode = State()

    new_card = State()
    new_group_vertices = State()
    create_group_vertex = State()
    add_group_folder = State()

    set_head_text = State()


async def check_user_in_table(message: Message) -> None:
    user_id = message.chat.id

    name = message.chat.username

    if not h_db_func.is_user_in_table(user_id):
        h_db_func.create_user(user_id, name)
        await message.answer(text="Напишите карту по типу", reply_markup=h_kb.add_card())
    else:
        await message.answer(text="Выбирите категорию", reply_markup=h_kb.inline_category())
        



@dp.message(CommandStart())
async def start(message: Message):

    await check_user_in_table(message)





@dp.callback_query(F.data)
async def inline_callback(callback: CallbackQuery, state: FSMContext):
    
    await state.clear()
    user_id = callback.message.chat.id
    call = str(callback.data)


    match call:

        case 'add':
            await callback.answer()

            await state.set_state(OrderAdd.new_card)
            await callback.message.answer(text="напишите название карты, кешбек по категориям такого типа:", reply_markup=h_kb.reply_off_add_kb())
        case _:
            lst = h_db_func.get_value_db(table="Cards", id=user_id)
            # print(lst)
            [[line[2], line[4]] for line in lst if line[3] == call]
            print()

            await callback.answer(f"вы выбрали {call}")

            




@dp.message(F.text, OrderAdd.new_card)
async def folder_name_chosen(message: Message, state: FSMContext):
    user_id = message.chat.id
    text = message.text

    if text == "Завершить добавление":
        await state.clear()
        await message.answer("карты добавлены. нажмите \start")
        return
    else:
        lst = text.split('\n')
        name = lst[0]
        dct = {elem.split()[0]: float(elem.split()[1]) for elem in lst[1:]}
        # print(name, "\n", dct)
        for key in dct:
            h_db_func.create_card(user_id, name, key, dct[key])





@dp.message(F.text)
async def other_text(message: Message):
    chat_type = message.chat.type
    if chat_type == "private":
        await message.answer(text=h_text.incorrectly_text_error)




    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    os.remove("database_hackaton.db")
    h_admin.create_db()
    asyncio.run(main())
