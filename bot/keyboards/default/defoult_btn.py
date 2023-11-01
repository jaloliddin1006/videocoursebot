from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Online darslar"),
        ],
        [
            KeyboardButton(text="✍️ Xabar yozish"),
        ]
        
        ],
    resize_keyboard=True, input_field_placeholder="Menu")

def get_book_category_btn(books_category, page):

    books_category_btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, input_field_placeholder=f"Bo'limlardan birini tanlang:// {page}")
    
    for i in books_category['results']:
        books_category_btn.insert(KeyboardButton(text=f"{i['name']}"))
        
    if books_category['count'] > 8:
        if books_category['previous'] and books_category['previous'].split('/')[-1].startswith("?page"):
            books_category_btn.add(KeyboardButton(text=f"⏮ previous : {books_category['previous'].split('?')[-1]}"))
        else:
            books_category_btn.add(KeyboardButton(text='⏮ previous : page=1'))
        books_category_btn.insert(KeyboardButton(text=f"⏭ next : {books_category['next'].split('?')[-1] if books_category['next'] else page}"))
    books_category_btn.add(KeyboardButton(text=f"🔙 Menu"))
    
    return books_category_btn


