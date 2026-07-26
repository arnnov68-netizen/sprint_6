import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
import time


class OrderPage(BasePage):
    """Страница заказа"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro_station, phone):
        """Заполнить первую форму заказа (Для кого самокат)"""
        self.input_text(self.locators.NAME_INPUT, name)
        self.input_text(self.locators.SURNAME_INPUT, surname)
        self.input_text(self.locators.ADDRESS_INPUT, address)

        # Выбор станции метро
        self.click_element(self.locators.METRO_STATION_INPUT)
        self.input_text(self.locators.METRO_STATION_INPUT, metro_station)
        time.sleep(1)

        # Находим и кликаем на нужную станцию
        metro_options = self.find_elements(self.locators.METRO_OPTIONS)
        for option in metro_options:
            if metro_station in option.text:
                option.click()
                break

        self.input_text(self.locators.PHONE_INPUT, phone)
        self.click_element(self.locators.NEXT_BUTTON)
        time.sleep(0.5)
        return self

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, delivery_date, rental_period, color, comment=""):
        """Заполнить вторую форму заказа (Про аренду)"""
        # Дата доставки
        self.click_element(self.locators.DELIVERY_DATE_INPUT)
        self.input_text(self.locators.DELIVERY_DATE_INPUT, delivery_date)
        time.sleep(0.5)

        # Кликаем на выбранную дату в календаре
        day = delivery_date.split('.')[0]
        date_element = self.find_element(
            (By.XPATH,
             f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month')) and text()='{day}']"),
            timeout=5
        )
        if date_element:
            date_element.click()

        # Период аренды
        self.click_element(self.locators.RENTAL_PERIOD_DROPDOWN)
        time.sleep(0.5)

        rental_options = self.find_elements(self.locators.RENTAL_PERIOD_OPTIONS)
        for option in rental_options:
            if rental_period in option.text:
                option.click()
                break

        # Цвет самоката
        if color == "black":
            self.click_element(self.locators.COLOR_CHECKBOX_BLACK)
        elif color == "grey":
            self.click_element(self.locators.COLOR_CHECKBOX_GREY)

        # Комментарий
        if comment:
            self.input_text(self.locators.COMMENT_INPUT, comment)

        self.click_element(self.locators.ORDER_BUTTON)
        time.sleep(0.5)
        return self

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """Подтвердить заказ в диалоговом окне"""
        # Ждем появления кнопки подтверждения
        time.sleep(0.5)
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)
        time.sleep(1)
        return self

    @allure.step("Проверить, что заказ успешно создан")
    def check_order_success(self):
        """Проверить, что заказ успешно создан"""
        # Ищем сообщение об успешном заказе
        success_locator = (By.XPATH,
                           "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
        return self.is_element_visible(success_locator, timeout=15)