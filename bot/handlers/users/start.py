from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.api import create_user, get_user, update_promo_code, check_promo_code, create_order
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import get_book_category_btn, menu_btn, phone_btn
from keyboards.inline.inline_btn import build_keyboard, change_promo_code
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.product import python_book
from data.config import ADMINS

async def send_yillik_tarif(message: types.Message, user_id):
    txt =  "Narxi 1 yil uchun: 2 459 000 so'm\n"
    txt += """
    Batafsil:
- Platformadan foydalanish muddati - 1 yil
- 10 dan ortiq zamonaviy kasblarni o'rganish
uchun maxsus kurslar
- Kurslardan tashqari taniqli sport ustalaridan
maxsus sog'ligingizni tanangizni yaxshilash
uchun videodarsliklar
- Yopiq chat va ekspertlar bilan doimiy
muloqot
- Ishga joylashish yoki freelancer sifatida
faoliyat yuritish uchun ko'mak
- SERTIFIKAT
- 1 yil davomida kurslarga kirish imkoniyati"""
    user = get_user(user_id)
    # print(user)
    if user['data']['promo_code']:
        promo_code = user['data']['promo_code']
    else:
        promo_code = None
        
    await message.answer(txt, reply_markup=build_keyboard("course", promo_code))


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state=FSMContext):
    user = get_user(message.from_user.id)
    if user['status_code'] != 200:
        await message.answer(f"""Assalomu alaykum, {message.from_user.full_name}!""")
        await message.answer("Botda to'liq foydalanish uchun ro'yxatdan o'tishingiz kerak!")
        await message.answer("Ism Familiyangizni kiriting: ", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state("name")
    else:
        await message.answer(f"""Assalomu alaykum, {message.from_user.full_name}!""", reply_markup=menu_btn)
        await send_yillik_tarif(message, message.from_user.id)
            
@dp.message_handler(state="name")
async def input_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(f"Telefon raqamingizni +9989******** ko'rinishida yuboring yoki Telefon raqamni yuborish tugmasini bosing 👇", reply_markup=phone_btn)
    await state.set_state("phone")
    
@dp.message_handler(state="phone" , content_types=types.ContentTypes.CONTACT)
async def input_phone(message: types.Message, state: FSMContext):
    telegram_phone_number = message.contact.phone_number
    data = await state.get_data()
    telegram_full_name = data.get("name")
    telegram_username = message.from_user.username or ''
    telegram_id = message.from_user.id
    
    s = create_user(
        telegram_id=int(telegram_id),
        telegram_full_name=telegram_full_name,
        telegram_username=telegram_username,
        telegram_phone_number=telegram_phone_number
        
    )
    await message.answer(f"Obuna EDU'ning rasmiy botiga xush kelibsiz!", reply_markup=menu_btn)
    await send_yillik_tarif(message, telegram_id)
    await state.finish()
    
@dp.message_handler(state="phone")
async def input_phone(message: types.Message, state: FSMContext):
    phone = message.text.replace("+", "").strip()
    if phone.isdigit() and len(phone) == 12:
        telegram_phone_number = phone
        data = await state.get_data()
        telegram_full_name = data.get("name")
        telegram_username = message.from_user.username or ''
        telegram_id = message.from_user.id
        s = create_user(
            telegram_id=int(telegram_id),
            telegram_full_name=telegram_full_name,
            telegram_username=telegram_username,
            telegram_phone_number=telegram_phone_number
            
        )
        await message.answer(f"Obuna EDU'ning rasmiy botiga xush kelibsiz!", reply_markup=menu_btn)
        await send_yillik_tarif(message, telegram_id)
        await state.finish()
    else:
        
        await message.answer(f"Telefon raqamingizni yuboring 👇", reply_markup=phone_btn)
        await state.set_state("phone")
    
@dp.callback_query_handler(text="price:yillik")
async def process_callback_price(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await send_yillik_tarif(call.message, call.from_user.id)
    
@dp.callback_query_handler(text="price:oylik")
async def process_callback_price(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.message.answer("Oylik bo'lib to'lash hozircha mavjud emas!", reply_markup=menu_btn)
    


@dp.callback_query_handler(text="promocode")
async def course_promo(call: CallbackQuery, state=FSMContext):
    await call.message.delete()
    await call.message.answer("Promo kodni kiriting:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("promo")
    
@dp.message_handler(state="promo")
async def input_promo(message: types.Message, state: FSMContext):
    promo_code = message.text
    # user = get_user(message.from_user.id)
    promo = check_promo_code(promo_code)
    if promo['status_code'] == 200:
        update_promo_code(message.from_user.id, promo_code)
        await message.answer("Promokod aktivlashtirildi ✅")
        await message.answer(f"Chegirma miqdori: {promo['data']['discount']} so'm.")
    else:
        await message.answer("Promo kod noto'g'ri ❌")
        update_promo_code(message.from_user.id, "")
        
    await state.finish()
    await send_yillik_tarif(message, message.from_user.id)


@dp.callback_query_handler(lambda call: call.data.startswith("promocode:"))
async def process_callback_promo_code(call: CallbackQuery):
    code = call.data.split(":")[-1]
    promo = check_promo_code(code)
    await call.answer()
    await call.message.delete()
    await call.message.answer(f"Siz ishlatayotgan promo kod: <b>{code}</b> \nChegirma miqdori: {promo['data']['discount']} so'm", reply_markup=change_promo_code)

@dp.callback_query_handler(text="back") 
async def process_callback_back(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await send_yillik_tarif(call.message, call.from_user.id)


@dp.callback_query_handler(text="product:course")
async def process_callback_product(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    invoice_data = python_book.generate_invoice()  # Product obyekti bilan to'lov ma'lumotlari
    # promo_code = await check_promo_code_validity(call.from_user.id)  # Promo kodni tekshirish
    user = get_user(call.from_user.id)
    code = user['data']['promo_code']
    # print(code)
    if code:
        promo_code = check_promo_code(code)
        if promo_code['data']['discount']:
            invoice_data['prices'][1]["amount"]= -promo_code['data']['discount'] * 100
            invoice_data['prices'][1]["label"] = f"Promo Code: [ {promo_code['data']['promo_code']} ]"
    await bot.send_invoice(chat_id=call.from_user.id, **invoice_data, payload=f"Yillik ta'rif | {code}")
    await call.answer()


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    # print(pre_checkout_query)
    s = create_order(
        check_id=pre_checkout_query.id,
        telegram_id=pre_checkout_query.from_user.id,
        full_name=pre_checkout_query.order_info.name,
        phone_number=pre_checkout_query.order_info.phone_number,
        email=pre_checkout_query.order_info.email,
        total_price=2459000,
        promo_code=pre_checkout_query.invoice_payload.split(' | ')[1],
        is_paid=True
    )
    # print(s)
    if s in [201, 200]:
        user = pre_checkout_query.from_user
        await bot.send_message(chat_id=user.id,
                           text="Xaridingiz uchun rahmat!", reply_markup=menu_btn)
        await bot.send_message(chat_id=ADMINS[0],
                           text=f"ID: {pre_checkout_query.id}\n"
                                f"Tarif: {pre_checkout_query.invoice_payload.split(' | ')[0]}\n"
                                f"Promo Code: {pre_checkout_query.invoice_payload.split(' | ')[1]}\n"
                                f"To'lov miqdori: {int(pre_checkout_query.total_amount)/100} so'm\n"
                                f"Telegram user:  <a href='tg://user?id={user.id}'>{user.full_name}</a>\n"                                
                                f"Username: @{user.username or ''}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, \nTel: {pre_checkout_query.order_info.phone_number}\n"
                                f"Email: {pre_checkout_query.order_info.email}\n",
                                reply_markup=menu_btn, 
                                parse_mode="HTML"                                
                                )
    else:
        await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring!", reply_markup=menu_btn)



