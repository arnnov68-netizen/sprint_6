# locators/order_locators.py
from selenium.webdriver.common.by import By


class OrderLocators:
    # Модальное окно подтверждения
    SUCCESS_HEADER = (By.XPATH,
                      "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(@class, 'Order_ModalText')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]/following-sibling::div")

    # Кнопки
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_CloseButton')]")
