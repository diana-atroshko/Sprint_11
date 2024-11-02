from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.locators import TestLocators


class TestRegistration:
    def test_successful_registration(self, driver, generate_email, generate_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.NAME).send_keys("Анна")
        driver.find_element(*TestLocators.EMAIL).send_keys(generate_email)
        driver.find_element(*TestLocators.PASSWORD).send_keys(generate_password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((TestLocators.TEXT_ENTER)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_failed_registration_with_wrong_password(self, driver, generate_email, generate_password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.NAME).send_keys("Анна")
        driver.find_element(*TestLocators.EMAIL).send_keys(generate_email)
        driver.find_element(*TestLocators.PASSWORD).send_keys('123')  # Неправильный пароль
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        try:
            error_message_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (TestLocators.WRONG_PASSWORD))
            )
            print("Сообщение об ошибке найдено:", error_message_element.text)
            assert error_message_element.is_displayed()
        except Exception as e:
            print("Ошибка при ожидании сообщения:", str(e))

