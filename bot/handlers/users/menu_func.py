from aiogram import types
from loader import dp, Bot
from data.api import get_user, update_promo_code, check_promo_code
from keyboards.inline.inline_btn import our_courses_btn


@dp.message_handler(text="📊 Obuna")
async def obuna_func(message: types.Message):
    await message.answer("Sizning obunangiz haqida")

@dp.message_handler(text="☎️ To'lov bo'yicha bog'lanish")
async def contact_func(message: types.Message):
    await message.answer("To'lov bo'yicha bog'lanish\n+998932977419")
    
@dp.message_handler(text="ℹ️ Biz haqimizda")
async def about_func(message: types.Message):
    await message.answer("Biz haqimizda\n\nBizning kanalimiz: @uzbkitoblar\nBizning botimiz: @uzbkitoblarbot\nKurslarimiz haqida batafsil", reply_markup=our_courses_btn)
