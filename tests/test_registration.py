from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import TestLocators
from helpers import generate_password, generate_email
from urls import get_login_url, get_registration_url, get_forgot_password_page_url, get_main_page_url, get_profile_page_url


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(get_registration_url())
        driver.find_element(*TestLocators.NAME).send_keys("Анна")
        driver.find_element(*TestLocators.EMAIL).send_keys(generate_email())
        driver.find_element(*TestLocators.PASSWORD).send_keys(generate_password())
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((TestLocators.TEXT_ENTER)))
        assert driver.current_url == get_registration_url()

    def test_failed_registration_with_wrong_password(self, driver):
        driver.get(get_registration_url())

        driver.find_element(*TestLocators.NAME).send_keys("Анна")
        driver.find_element(*TestLocators.EMAIL).send_keys(generate_email())
        driver.find_element(*TestLocators.PASSWORD).send_keys('123')  # Неправильный пароль
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        error_message_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (TestLocators.WRONG_PASSWORD))
        )
        print("Сообщение об ошибке найдено:", error_message_element.text)
        assert error_message_element.is_displayed()




