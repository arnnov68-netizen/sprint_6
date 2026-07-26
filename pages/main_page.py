import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage):
    """Главная страница"""

    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        self.open_page(self.URL)
        self.accept_cookies()
        return self

    @allure.step("Принять куки")
    def accept_cookies(self):
        """Принять куки, если они есть"""
        try:
            accept_button = self.find_element(self.locators.COOKIE_BUTTON, timeout=3)
            if accept_button:
                accept_button.click()
                time.sleep(0.5)
        except:
            pass
        return self

    @allure.step("Кликнуть на вопрос по тексту: {question_text}")
    def click_question_by_text(self, question_text):
        """Кликнуть на вопрос по его тексту (стабильный способ)"""
        # Используем XPATH с текстом вопроса
        question_locator = (By.XPATH,
                            f"//div[contains(@class, 'accordion__button') and contains(text(), '{question_text}')]")
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        time.sleep(0.5)
        return question_locator

    @allure.step("Кликнуть на вопрос по индексу #{index}")
    def click_question_by_index(self, index):
        """Кликнуть на вопрос по его позиции (1-based)"""
        question_locator = (By.XPATH, f"(//div[contains(@class, 'accordion__button')])[{index}]")
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        time.sleep(0.5)
        return question_locator

    @allure.step("Кликнуть на вопрос #{question_index} (устаревший способ)")
    def click_question(self, question_index):
        """Кликнуть на вопрос по индексу (для обратной совместимости)"""
        # Используем стабильный способ - по позиции
        return self.click_question_by_index(question_index + 1)

    @allure.step("Получить текст ответа по тексту вопроса")
    def get_answer_by_question_text(self, question_text):
        """Получить ответ на вопрос по его тексту"""
        answer_locator = (By.XPATH,
                          f"//div[contains(@class, 'accordion__button') and contains(text(), '{question_text}')]/following-sibling::div[contains(@class, 'accordion__panel')]")
        time.sleep(0.5)
        return self.get_text(answer_locator)

    @allure.step("Получить текст ответа по индексу #{index}")
    def get_answer_by_index(self, index):
        """Получить ответ на вопрос по его позиции (1-based)"""
        answer_locator = (By.XPATH, f"(//div[contains(@class, 'accordion__panel')])[{index}]")
        time.sleep(0.5)
        return self.get_text(answer_locator)

    @allure.step("Получить текст ответа на вопрос #{question_index} (устаревший способ)")
    def get_answer_text(self, question_index):
        """Получить текст ответа на вопрос по индексу (для обратной совместимости)"""
        return self.get_answer_by_index(question_index + 1)

    @allure.step("Кликнуть на кнопку заказа вверху страницы")
    def click_order_button_top(self):
        """Кликнуть на кнопку заказа вверху страницы"""
        self.click_element(self.locators.ORDER_BUTTON_TOP)
        time.sleep(0.5)

    @allure.step("Кликнуть на кнопку заказа внизу страницы")
    def click_order_button_bottom(self):
        """Кликнуть на кнопку заказа внизу страницы"""
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        time.sleep(0.5)
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)
        time.sleep(0.5)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        """Кликнуть на логотип Самоката"""
        self.click_element(self.locators.SCOOTER_LOGO)
        time.sleep(1)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекса"""
        self.click_element(self.locators.YANDEX_LOGO)
        time.sleep(2)
        self.switch_to_new_window()