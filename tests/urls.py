BASE_URL = 'https://stellarburgers.nomoreparties.site/'

def get_login_url():
    return f'{BASE_URL}login'

def get_registration_url():
    return f'{BASE_URL}register'

def get_main_page_url():
    return f'{BASE_URL}'

def get_profile_page_url():
    return f'https://stellarburgers.nomoreparties.site/account/profile'

def get_forgot_password_page_url():
    return f'{BASE_URL}forgot-password'
