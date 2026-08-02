# pages/order_page.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    # Локаторы для первой формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй формы
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    COLOR_CHECKBOX_BLACK = (By.XPATH, "//input[@id='black']")
    COLOR_CHECKBOX_GREY = (By.XPATH, "//input[@id='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Локатор успешного заказа
    ORDER_SUCCESS = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        """Заполнение первой формы заказа"""
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.SURNAME_INPUT, surname)
        self.enter_text(self.ADDRESS_INPUT, address)
        self.enter_text(self.METRO_INPUT, metro)
        # Выбираем станцию из списка
        metro_option = (By.XPATH, f"//div[contains(text(), '{metro}')]")
        self.click_element(metro_option)
        self.enter_text(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, delivery_date, rental_period, color, comment):
        """Заполнение второй формы заказа"""
        # Вводим дату и нажимаем Enter, чтобы закрыть календарь
        date_input = self.find_element(self.DELIVERY_DATE_INPUT)
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

        # Кликаем на выпадающий список
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)

        # Выбираем период аренды
        rental_option = (By.XPATH, f"//div[text()='{rental_period}']")
        self.click_element(rental_option)

        # Выбираем цвет
        if color == "black":
            self.click_element(self.COLOR_CHECKBOX_BLACK)
        elif color == "grey":
            self.click_element(self.COLOR_CHECKBOX_GREY)

        self.enter_text(self.COMMENT_INPUT, comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Проверить успешность заказа")
    def check_order_success(self):
        """Проверка, что заказ успешно создан"""
        return self.is_element_visible(self.ORDER_SUCCESS, timeout=15)
