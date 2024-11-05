import random
import string

def generate_password():
    lst = string.ascii_letters + string.digits
    password = ''.join(random.choice(lst) for _ in range(6))
    return password

def generate_email():
    email= f'diana_atroshko_15_{random.randint(100, 999)}@yandex.ru'
    return email