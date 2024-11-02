from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import TestLocators

class TestLogout:
    def test_logout_by_button_Logout_in_personal_account(self, driver, create_account, login_to_account):
        driver.get('https://stellarburgers.nomoreparties.site')
        personal_account_button = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT)))
        personal_account_button.click()

        butt = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((TestLocators.EXIT)))
        butt.click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_LOGIN1))
        )
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', f"Ожидался URL: 'https://stellarburgers.nomoreparties.site/login', но был: {driver.current_url}"

