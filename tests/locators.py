from selenium.webdriver.common.by import By

class TestLocators:
    NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input" #Имя в форме регистрации
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" #почта в форме регистрации
    PASSWORD = By.XPATH, "//label[text()='Пароль']/following-sibling::input" #пароль в форме регистрации
    BUTTON_REGISTRATION = By.XPATH, "//button[text()='Зарегистрироваться']" #кнопка Зарегистрироваться в форме регистрации
    TEXT_ENTER = (By.XPATH, "//h2[contains(text(), 'Вход')]") #заголовок Вход в форме входа
    WRONG_PASSWORD = By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']"#текст некорректного пароля
    BUTTON_ENTER = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"#кнопка войти в аккаунт
    BUTTON_PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']" #кнопка оформить заказ
    PERSONAL_ACCOUNT= By.XPATH, "//a/p[text()='Личный Кабинет']" # кнопка Личный кабинет
    BUTTON_ENTRANCE = By.XPATH, "//button[text()='Войти']"# кнопка войти
    BUTTON_LOGIN = By.XPATH, "//a[contains(text(), 'Войти')]"# кнопка войти
    TEXT_IN_PERSONAL_ACCOUNT = By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default' and contains(text(), 'В этом разделе вы можете изменить свои персональные данные')]"
    CONSTRUCTOR = By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and .//p[contains(text(), 'Конструктор')]]"#конструктор
    ASSEMBLE_BURGER = By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and contains(text(), 'Соберите бургер')]"#текст соберите бургер
    LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a"#логотип сайти
    EXIT = By.XPATH, "//button[contains(@class, 'Account_button__14Yp3')]"#кнопка выйти
    BUTTON_LOGIN1 = By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти')]"#кнопка войти
    BUTTON_BUNS = By.XPATH, "//span[text()='Булки']"#переключатель булки
    BUTTON_SAUCES = By.XPATH, "//span[text()='Соусы']"#переключатель соусы
    BUTTON_STUFFING = "//span[text()='Начинки']"#переключатель начинки
    SECTION_BUNS = By.XPATH, "//h2[text()='Булки']"#раздел булки
    SECTION_SAUCES = By.XPATH, "//h2[text()='Соусы']"#раздел соусы
    SECTION_STUFFING = By.XPATH, "//h2[text()='Начинки']"#раздел начинки
