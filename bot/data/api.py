import requests
import json

BASE_URL = "http://127.0.0.1:8000"

######## createuser ############
def create_user(telegram_id, telegram_full_name, telegram_username, telegram_phone_number):
    context =  {
                "telegram_id": telegram_id,
                "telegram_full_name":telegram_full_name,
                "telegram_username":telegram_username,
                "telegram_phone_number":telegram_phone_number,
                "promo_code":None,
                "is_active": True
                }
    response = requests.post(f"{BASE_URL}/api/botuser/", data = context)
    return response.status_code

def get_user(telegram_id):
    response = requests.get(f"{BASE_URL}/api/botuser/{telegram_id}/")
    data = json.loads(response.text)
    return data

def get_all_users():
    response = requests.get(f"{BASE_URL}/api/botuser/")
    data = json.loads(response.text)
    return data

def update_promo_code(telegram_id, promo_code):
    context = {
                "telegram_id": telegram_id,
                "promo_code": promo_code
    }
    response = requests.patch(f"{BASE_URL}/api/botuser/{telegram_id}/", data = context)
    # print(response.text)
    data = json.loads(response.text)
    return data

def check_promo_code(promo_code):
    response = requests.get(f"{BASE_URL}/api/promo/{promo_code}/")
    data = json.loads(response.text)
    return data
    
def create_order(telegram_id, full_name, phone_number, email, total_price, is_paid):
    context =  {
                "telegram_id": telegram_id,
                "full_name":full_name,
                "phone_number":phone_number,
                "email":email,
                "total_price":total_price,
                "is_paid": is_paid
                }
    
    response = requests.post(f"{BASE_URL}/api/botuser/", data = context)
    return response.status_code

# def check_promo_code()
#### create user complate
# s = create_user(234234234,"newuserrrrrr","usename", "99995523255")
# print(s)

# #### get user test is complate success
# n = get_user(234234234)
# print(n)

## get all users success
# all = get_all_users()
# print(all)

### promo code update success
# promo = update_promo_code(234234234, '')
# print(promo)


#### check promo code is success
# promo = check_promo_code("baxa")
# print(promo)