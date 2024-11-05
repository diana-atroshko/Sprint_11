from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import TestLocators
from urls import get_login_url, get_registration_url, get_forgot_password_page_url, get_main_page_url, get_profile_page_url


class TestLogout:
    def test_logout_by_button_Logout_in_personal_account(self, driver, create_account, login_to_account):
        driver.get(get_main_page_url())
        personal_account_button = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT)))
        personal_account_button.click()

        butt = WebDriverWait(driver, 25).until(EC.visibility_of_element_located((TestLocators.EXIT)))
        butt.click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((TestLocators.BUTTON_LOGIN1))
        )
        assert driver.current_url == get_login_url(), f"Ожидался URL: {get_login_url()}, но был: {driver.current_url}"

