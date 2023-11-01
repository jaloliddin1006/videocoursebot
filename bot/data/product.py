from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


python_book = Product(
    title="Pythonda Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Umumiy kurs narxi',
            amount=5600000 * 100,  
        ),
       
         LabeledPrice(
            label='Promo Code:',
            amount=250000 * 100, 
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://i.imgur.com/0IvPPun.jpg',
    photo_width=851,
    photo_height=1280,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 100),
        LabeledPrice(
            '3 ish kunida yetkazish', 100),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 100),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -100)
                                       ])