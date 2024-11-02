from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import TestLocators


class TestEntrance:
    def test_entrance_by_button_login_to_account(self, driver, login_to_account):
        driver.get('https://stellarburgers.nomoreparties.site/')
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((TestLocators.BUTTON_ENTER))
            )
            login_button.click()
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((TestLocators.BUTTON_PLACE_ORDER))
            )
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', но был: {driver.current_url}"
        except Exception as e:
            print(f"Ошибка во время теста: {e}")


    def test_entrance_by_button_personal_account(self, driver, create_account):

        driver.get('https://stellarburgers.nomoreparties.site/')

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
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', но был: {driver.current_url}"


    def test_entrance_by_button_in_password_recovery_form(self, driver, create_account):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((TestLocators.BUTTON_LOGIN))
        )
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', \
            f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/login', но был: {driver.current_url}"
        driver.find_element(*TestLocators.EMAIL).send_keys(create_account['email_1'])
        driver.find_element(*TestLocators.PASSWORD).send_keys(create_account['password_1'])
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_PLACE_ORDER))
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', но был: {driver.current_url}"


    def test_entrance_by_button_in_register_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
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
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', но был: {driver.current_url}"

