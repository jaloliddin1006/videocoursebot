from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


python_book = Product(
    title="Online Course dan barchasi 1 ta narxda",
    description="Ushbu tarif uchun to'lovni amalga oshirmoqchi bo'lsangiz, quyidagi tugmani bosing va to'lovni amalga oshiring.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='Umumiy kurs narxi',
            amount=179000 * 100,  
        ),
       
         LabeledPrice(
            label='Promo Code:',
            amount=0, 
        ),
    ],
    start_parameter="create_invoice_courses",
    photo_url='https://school.rajaawasthi.com/uploads/thumbnails/course_thumbnails/course_thumbnail_default_5.jpg',
    photo_width=1280,
    photo_height=1280,
    need_name=True,
    need_phone_number=True,
    need_email=True,
    send_email_to_provider = True,
    need_shipping_address=False,
    is_flexible=False,
    # promo_code="PROMO123",  # Promo kod
    # discount_amount=1000,  # Chegirma miqdori
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