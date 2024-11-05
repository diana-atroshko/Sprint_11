from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators
from helpers import generate_password, generate_email
from urls import get_login_url, get_registration_url, get_forgot_password_page_url, get_main_page_url, get_profile_page_url

class TestEntrance:
    def test_entrance_by_button_login_to_account(self, driver):
        driver.get(get_main_page_url())
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((TestLocators.BUTTON_ENTER))
        )
        login_button.click()
        driver.find_element(*TestLocators.EMAIL).send_keys('anna_13_1234@ya.ru')
        driver.find_element(*TestLocators.PASSWORD).send_keys('finfin')
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_PLACE_ORDER))
        )
        assert driver.current_url == get_main_page_url(), f"Ожидался URL: {get_main_page_url()}, но был: {driver.current_url}"

    def test_entrance_by_button_personal_account(self, driver, create_account):

        driver.get(get_main_page_url())

        personal_account_button = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT))
        )
        personal_account_button.click()

        driver.find_element(*TestLocators.EMAIL).send_keys(create_account['email_1'])
        driver.find_element(*TestLocators.PASSWORD).send_keys(create_account['password_1'])
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_PLACE_ORDER))
        )
        assert driver.current_url == get_main_page_url(), f"Ожидался URL: {get_main_page_url()}, но был: {driver.current_url}"


    def test_entrance_by_button_in_password_recovery_form(self, driver):
        driver.get(get_forgot_password_page_url())
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((TestLocators.BUTTON_LOGIN))
        )
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        assert driver.current_url == get_login_url(), \
            f"Ожидался URL: {get_login_url()}, но был: {driver.current_url}"
        driver.find_element(*TestLocators.EMAIL).send_keys('anna_13_1234@ya.ru')
        driver.find_element(*TestLocators.PASSWORD).send_keys('finfin')
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_PLACE_ORDER))
        )
        assert driver.current_url == get_main_page_url(), f"Ожидался URL: {get_main_page_url()}, но был: {driver.current_url}"

    def test_entrance_by_button_in_register_form(self, driver):
        driver.get(get_registration_url())
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((TestLocators.BUTTON_LOGIN))
        )
        button.click()
        driver.find_element(*TestLocators.EMAIL).send_keys('anna_13_1234@ya.ru')
        driver.find_element(*TestLocators.PASSWORD).send_keys('finfin')
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_PLACE_ORDER))
        )
        assert driver.current_url == get_main_page_url(), f"Ожидался URL: {get_main_page_url()}, но был: {driver.current_url}"
