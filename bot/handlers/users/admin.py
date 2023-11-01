from aiogram import types
from data.api import * 
from data.config import ADMINS
from loader import dp,  bot
from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import menu_btn

@dp.message_handler(commands=["allusers"], user_id=ADMINS)
async def reklama(message: types.Message, state=FSMContext):
    users = get_all_users()
    await message.answer(f"Foydalanuvchilar soni: {len(users)}")
    
@dp.message_handler(commands=["reklama"], user_id=ADMINS)
async def reklama(message: types.Message, state=FSMContext):
    await message.answer("Xabar yozing", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("reklama")

@dp.message_handler(state="reklama")
async def reklmana(message: types.Message, state=FSMContext):
    users = get_all_users()
    xabar = message.text
    for user in users:
        try:
            await bot.send_message(chat_id=user['user_id'], text=xabar)
        except:
            pass
    await message.answer("xabaringiz yetkazildi ✅", reply_markup=menu_btn)
    