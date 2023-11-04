from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def build_keyboard(product, promo_code=None):
    if promo_code:
        keys = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Yillik obuna  242.000 so'm", callback_data=f"product:{product}"),
            ],
             [
                InlineKeyboardButton(text="PromoCode Active ✅", callback_data=f"promocode:{promo_code}"),
            ],
        ])
    else:
        keys = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Yillik obuna  242.000 so'm", callback_data=f"product:{product}"),
            ],
            [
                InlineKeyboardButton(text="PromoCode bormi?", callback_data=f"promocode"),
            ],
        ])
    return keys



change_promo_code = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="🔄 PromoCode ni almashtirasizmi? ", callback_data=f"promocode"),
            ],
            [
                InlineKeyboardButton(text="⬅️ Ortga", callback_data=f"back"),
            ],
        ])

our_courses_btn = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Kurslar haqida ma'lumot olish", web_app=WebAppInfo(url="https://uzum.uz/uz/")),
            ]
        ])