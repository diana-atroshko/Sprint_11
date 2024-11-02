from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import TestLocators


class TestTransition:
    def test_transition_to_personal_account_by_clicking(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL).send_keys('anna_13_1234@ya.ru')
        driver.find_element(*TestLocators.PASSWORD).send_keys('finfin')
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        personal_account_button = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT))
        )
        personal_account_button.click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.TEXT_IN_PERSONAL_ACCOUNT))
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/account/profile', но был: {driver.current_url}"

    def test_transition_from_personal_account_to_constructor_by_clicking_on_constructor(self, driver,login_to_account):
        driver.get('https://stellarburgers.nomoreparties.site/')
        personal_account_button = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT)))
        personal_account_button.click()

        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.ASSEMBLE_BURGER))
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', но был: {driver.current_url}"

    def test_transition_from_personal_account_to_constructor_by_clicking_on_Stellar_Burgers_logo(self, driver,login_to_account):
        driver.get('https://stellarburgers.nomoreparties.site/')
        personal_account_button = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT))
        )
        personal_account_button.click()

        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.ASSEMBLE_BURGER))
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/', но был: {driver.current_url}"
