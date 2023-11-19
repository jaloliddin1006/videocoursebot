from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def build_keyboard(product, promo_code=None):
    if promo_code:
        keys = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Yillik obuna  2 459 000 so'm", callback_data=f"product:{product}"),
            ],
             [
                InlineKeyboardButton(text="PromoCode Active ✅", callback_data=f"promocode:{promo_code}"),
            ],
        ])
    else:
        keys = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Yillik obuna  2 459 000 so'm", callback_data=f"product:{product}"),
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
                InlineKeyboardButton(text="Kurslar haqida ma'lumot olish", web_app=WebAppInfo(url="https://azbo.uz/")),
            ]
        ])


tarif_btn = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Yillik obunani rasmiylashtirish", callback_data=f"price:yillik"),
            ],
            [
                InlineKeyboardButton(text="Oylik bo'lib to'lash", callback_data=f"price:oylik"),
            ],
           
        ])