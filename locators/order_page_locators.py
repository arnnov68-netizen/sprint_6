from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы заказа"""

    # Первая форма - Для кого самокат
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTIONS = (By.XPATH, "//div[contains(@class, 'select-search__option')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма - Про аренду
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
    RENTAL_PERIOD_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Всплывающее окно с успешным заказом
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]")