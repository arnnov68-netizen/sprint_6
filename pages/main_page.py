# pages/main_page.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    # Локаторы
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    HEADER = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        self.open_page(self.URL)
        # Ожидаем загрузки страницы
        self.wait_for_element_visible(self.HEADER, timeout=15)

    @allure.step("Кликнуть на кнопку заказа (верхняя)")
    def click_order_button_top(self):
        """Кликнуть на верхнюю кнопку заказа"""
        self.click_element(self.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на кнопку заказа (нижняя)")
    def click_order_button_bottom(self):
        """Кликнуть на нижнюю кнопку заказа"""
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        """Кликнуть на логотип Самоката"""
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса и переключиться на новое окно")
    def click_yandex_logo_and_switch_to_new_window(self):
        """Кликнуть на логотип Яндекса и переключиться на новое окно"""
        # Запоминаем текущее окно
        main_window = self.get_current_window_handle()
        initial_window_count = self.get_window_handles_count()

        # Кликаем на логотип
        self.click_element(self.YANDEX_LOGO)

        # Ожидаем появления нового окна
        self.wait_for_new_window(initial_window_count, timeout=15)

        # Получаем новое окно
        new_window = self.get_new_window_handle(main_window)

        if new_window is None:
            raise Exception("Новое окно не найдено")

        # Переключаемся на новое окно
        self.switch_to_window(new_window)

        # Ожидаем загрузки Дзена
        self.wait_for_url_contains("dzen.ru", timeout=20)

    @allure.step("Кликнуть на вопрос по индексу: {index}")
    def click_question_by_index(self, index):
        """Кликнуть на вопрос по его порядковому номеру"""
        locator = (By.XPATH, f"(//div[contains(@class, 'accordion__heading')])[{index}]")

        # Прокручиваем к вопросу
        self.scroll_to_element(locator)

        # Ожидаем, что элемент станет кликабельным
        self.wait_for_element_clickable(locator)

        # Кликаем на вопрос
        self.click_element(locator)

        # Ожидаем появления ответа
        answer_locator = (By.XPATH, f"(//div[contains(@class, 'accordion__panel')])[{index}]")
        self.wait_for_element_visible(answer_locator)

    @allure.step("Получить ответ по индексу: {index}")
    def get_answer_by_index(self, index):
        """Получить текст ответа по порядковому номеру вопроса"""
        locator = (By.XPATH, f"(//div[contains(@class, 'accordion__panel')])[{index}]")
        # Ожидаем, что ответ видим
        self.wait_for_element_visible(locator)
        return self.get_element_text(locator)

    @allure.step("Прокрутить к вопросу по индексу: {index}")
    def scroll_to_question(self, index):
        """Прокрутить к вопросу по индексу"""
        locator = (By.XPATH, f"(//div[contains(@class, 'accordion__heading')])[{index}]")
        self.scroll_to_element(locator)
