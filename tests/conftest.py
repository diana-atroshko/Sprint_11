import random
import pytest
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators



@pytest.fixture(scope="session")
def generate_password():
    lst = string.ascii_letters + string.digits
    password = ''.join(random.choice(lst) for _ in range(6))
    return password

@pytest.fixture(scope="session")
def generate_email():
    email= f'diana_atroshko_15_{random.randint(100, 999)}@yandex.ru'
    return email


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def create_account(driver, generate_email, generate_password):
    email_1 = generate_email
    password_1 = generate_password
    name = "Диана"
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*TestLocators.NAME).send_keys(name)
    driver.find_element(*TestLocators.EMAIL).send_keys(email_1)
    driver.find_element(*TestLocators.PASSWORD).send_keys(password_1)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    WebDriverWait(driver, 15).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    return {
        'name': name,
        'email_1': email_1,
        'password_1': password_1
    }

@pytest.fixture
def login_to_account(driver,create_account):
    email = create_account['email_1']
    password = create_account['password_1']

    WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))

    driver.find_element(*TestLocators.EMAIL).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
    WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
