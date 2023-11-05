import requests
import json

BASE_URL = "https://obunaedu.mamatmusayev.uz"

######## createuser ############
def create_user(telegram_id, telegram_full_name, telegram_username, telegram_phone_number):
    context =  {
                "telegram_id": telegram_id,
                "telegram_full_name":telegram_full_name,
                "telegram_username":telegram_username,
                "telegram_phone_number":telegram_phone_number,
                "promo_code":'',
                "is_active": True
                }
    response = requests.post(f"{BASE_URL}/api/botuser/", data = context)
    # print(response.text)
    return response.status_code

def get_user(telegram_id):
    response = requests.get(f"{BASE_URL}/api/botuser/{telegram_id}/")
    data = json.loads(response.text)
    return {"data": data, "status_code": response.status_code}

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
    return {"data": data, "status_code": response.status_code}

    
def create_order(check_id, telegram_id, full_name, phone_number, email, total_price, promo_code, is_paid):
    context =  {
                "check_id": check_id,
                "user": telegram_id,
                "full_name":full_name,
                "phone_number":phone_number,
                "email":email,
                "total_price":total_price,
                "promo_code":promo_code,
                "is_paid": is_paid
              
                }
    
    response = requests.post(f"{BASE_URL}/api/order/create/", data = context)
    return response.status_code

### create user complate
# s = create_user(2079362883, "jaloliddin", "usename", "+99995523255")
# print(s)
# s = create_user(
#     telegram_id=973108256,
#     telegram_full_name="jaloliddin",
#     telegram_username="usename",
#     telegram_phone_number="+99995523255"
    
# )
# print(s)
# #### get user test is complate success
# n = get_user(973108256)
# if n['status_code'] != 200:
#     print("not working")
# else:
#     print(n)

## get all users success
# all = get_all_users()
# print(all)

### promo code update success
# promo = update_promo_code(234234234, '')
# print(promo)


#### check promo code is success
# promo = check_promo_code("baxa")
# print(promo)


## create order 
# order = create_order("8930795580093228429", 973108256, "jaloliddin", "+99995523255", "email@gmail.com", 10000000, "baxa", True)
# print(order)