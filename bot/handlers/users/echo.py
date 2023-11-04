from aiogram import types

from loader import dp
from keyboards.default.defoult_btn import menu_btn

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Noto'g'ri buyruq", reply_markup=menu_btn)
