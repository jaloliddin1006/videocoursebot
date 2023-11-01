from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.api import *
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import get_book_category_btn, menu_btn
from keyboards.inline.inline_btn import build_keyboard
import requests
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.product import python_book
from data import config
from data.product import REGULAR_SHIPPING, FAST_SHIPPING, PICKUP_SHIPPING
from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user
    username = user.username if user.username else " "
    first_name = user.first_name if user.first_name else " "
    last_name = user.last_name if user.last_name else " "
    is_active = True
    create_user(telegram_id=message.from_user.id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                is_active = True)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=menu_btn)
    

@dp.message_handler(text = "✍️ Xabar yozish")
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer("Xabar yuboring", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("feedback")
    

@dp.message_handler(state="feedback")
async def input_password(message: types.Message, state: FSMContext):
    feedback(message.from_user.id, message.text)
    await message.answer("Xabaringiz qabul qilindi", reply_markup=menu_btn)
    await state.finish()
    
@dp.message_handler(Command("mahsulotlar"))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_book.generate_invoice(),
                           payload="123456")
    
    
    
@dp.message_handler(Command("kitob"))
async def show_invoices(message: types.Message):
    caption = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n\n"
    caption += "Ushbu kitob bugungi kunda dasturlash asoslariga oid o’zbek tilidagi mukammal tuzilgan qo’llanmalardan biridir.\n\n"
    caption += "Qo’lingizdagi kitobning o’ziga xos jihati shundaki, uning har bir bo’limi uchun tayyorlangan qo'shimcha onlayn"
    caption += "materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg’ulotlar va vazifalarning kodlari e’tiboringizga havola etilgan.\n\n"
    caption += "O’quvchilar bu materiallarni maxsus QR kod yordamida o’z komputerlariga yuklab olib, ulardan unumli foydalanishi mumkin.\n\n"
    caption += "Narxi: <b>50000 so'm</b>"
    await message.answer_photo(photo="https://i.imgur.com/0IvPPun.jpg",
                         caption=caption, reply_markup=build_keyboard("book"))


@dp.callback_query_handler(text="product:book")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_book.generate_invoice(),
                           payload="payload:kitob")
    await call.answer()
    
    
    
@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    # if query.shipping_address.country_code != "UZ":
    #     await bot.answer_shipping_query(shipping_query_id=query.id,
    #                                     ok=False,
                                        # error_message="Chet elga yetkazib bera olmaymiz")
    # elif query.shipping_address.city.lower() == "tashkent":
    #     await bot.answer_shipping_query(shipping_query_id=query.id,
    #                                     shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
    #                                     ok=True)
    # else:
    await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[],
                                        ok=True)



@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")