from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.locators import TestLocators


class TestConstructorSections:
    def test_jumps_to_section_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        buns_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((TestLocators.BUTTON_BUNS))
        )
        element = driver.find_element(*TestLocators.SECTION_BUNS)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((TestLocators.SECTION_BUNS))), "Заголовок раздела 'Булки' не виден в области просмотра"

    def test_jumps_to_section_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        souces_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((TestLocators.BUTTON_SAUCES))
        )
        souces_element.click()
        element = driver.find_element(*TestLocators.SECTION_SAUCES)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((TestLocators.SECTION_SAUCES))), "Заголовок раздела 'Соусы' не виден в области просмотра"

    def test_jumps_to_section_stuffing(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        stuffing_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((TestLocators.BUTTON_STUFFING)))
        stuffing_element.click()

        element = driver.find_element(*TestLocators.SECTION_STUFFING)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((TestLocators.SECTION_STUFFING))), "Заголовок раздела 'Начинки' не виден в области просмотра"

