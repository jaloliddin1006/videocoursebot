import requests
import json

BASE_URL = "http://127.0.0.1:8000"

######## createuser ############
def create_user(telegram_id, username, first_name, last_name, is_active):
    context =  {
                "user_id": telegram_id,
                "username":username,
                "first_name":first_name,
                "last_name":last_name,
                "is_active":is_active
                }
    response = requests.post(f"{BASE_URL}/api/botuser/", data = context)
    return response.status_code

def get_all_users():
    response = requests.get(f"{BASE_URL}/api/botuser/")
    data = json.loads(response.text)
    return data
######### feedback ###########
def feedback(user_id, feedback):
    response = requests.post(f"{BASE_URL}/api/feedback/", data = {"user__user_id":user_id, "feedback": feedback})
    return response.status_code
