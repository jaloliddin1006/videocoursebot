from aiogram import types
from loader import dp, Bot
from data.api import get_user, update_promo_code, check_promo_code
from keyboards.inline.inline_btn import our_courses_btn, tarif_btn
from keyboards.default.defoult_btn import menu_btn


@dp.message_handler(text="🌐 Ta'riflar")
async def send_tariflar(message: types.Message):
    await message.answer("Ta'riflar", reply_markup=tarif_btn)

@dp.message_handler(text="📊 Obuna")
async def obuna_func(message: types.Message):
    await message.answer("Sizning obunangiz haqida")

@dp.message_handler(text="☎️ To'lov bo'yicha bog'lanish")
async def contact_func(message: types.Message):
    await message.answer("To'lov bo'yicha bog'lanish\n+998932977419")
    
@dp.message_handler(text="ℹ️ Biz haqimizda")
async def about_func(message: types.Message):
    txt = "ObunaEdu.uz - platformasi orqali istalgan zamonaviy kurslarni bir vaqtning o'zida atigi birgina to'lov evaziga, mukammal tarzda, "
    txt +="sifatli darajada o'rganishingiz mumkin. Osiyo va O'zbekistondagi TOP mutaxassislarning bilimini jamlagan holda, "
    txt += "ulardan to'gridan to'gri mukammal bilimni olishingiz mumkin. Platformada Targeting, SMM, Graphic design, SEO, Digital marketing, "
    txt += "Nocoding website and TG bot, E'commerce, InfoBiznes, Reelsmaker, body transformation va boshqa kurslar mavjud. Birgina to'lov "
    txt += "evaziga 1500 ga yaqin videodarsliklar!"
    await message.answer(txt, reply_markup=our_courses_btn)


@dp.message_handler(text="❓ Ko'p beriladigan savollar")
async def savollar_func(message: types.Message):
    await message.answer("Savollar")
    