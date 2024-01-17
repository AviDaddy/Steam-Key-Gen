import random
import requests

def generate_steam_key():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    key = ''.join(random.choice(chars) for _ in range(5))
    return key

def validate_steam_key(key):
    response = requests.post('https://store.steampowered.com/login/dologin/', data={'version': '1', 'domain': 'store.steampowered.com', 'sessionid': '1234567890abcdef1234567890abcdef', 'password': key, 'email': ''})
    if 'Invalid Password' in response.text:
        return False
    elif 'Invalid Login' in response.text:
        return False
    else:
        return True

def find_valid_steam_key():
    while True:
        key = generate_steam_key()
        if validate_steam_key(key):
            return key

valid_key = find_valid_steam_key()
print("Valid Steam key:", valid_key)
