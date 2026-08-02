# pages/main_page.py
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    # Локаторы
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    # Локаторы для FAQ - используем стабильные локаторы
    FAQ_CONTAINER = (By.XPATH, "//div[contains(@class, 'Home_FAQ__3uVm4')]")

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        self.open_page(self.URL)

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

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекса"""
        self.click_element(self.YANDEX_LOGO)

    @allure.step("Кликнуть на вопрос по индексу")
    def click_question_by_index(self, index):
        """Кликнуть на вопрос по его порядковому номеру"""
        # Используем позицию внутри контейнера
        locator = (By.XPATH, f"(//div[contains(@class, 'accordion__heading')])[{index}]")
        self.click_element(locator)

    @allure.step("Получить ответ по индексу")
    def get_answer_by_index(self, index):
        """Получить текст ответа по порядковому номеру вопроса"""
        # Используем позицию внутри контейнера
        locator = (By.XPATH, f"(//div[contains(@class, 'accordion__panel')])[{index}]")
        element = self.find_element(locator)
        return element.text

    @allure.step("Кликнуть на вопрос по тексту")
    def click_question_by_text(self, question_text):
        """Кликнуть на вопрос по его тексту"""
        locator = (By.XPATH, f"//div[contains(@class, 'accordion__heading')]//div[contains(text(), '{question_text}')]")
        self.click_element(locator)

    @allure.step("Получить ответ по тексту вопроса")
    def get_answer_by_question_text(self, question_text):
        """Получить ответ по тексту вопроса"""
        # Находим родительский элемент вопроса
        question_locator = (By.XPATH,
                            f"//div[contains(@class, 'accordion__heading') and contains(., '{question_text}')]")
        question_element = self.find_element(question_locator)

        # Находим соответствующий ответ (соседний элемент)
        answer_locator = (By.XPATH,
                          f"//div[contains(@class, 'accordion__heading') and contains(., '{question_text}')]/following-sibling::div[contains(@class, 'accordion__panel')]")
        answer_element = self.find_element(answer_locator)
        return answer_element.text

    @allure.step("Прокрутить к вопросу по индексу")
    def scroll_to_question(self, index):
        """Прокрутить к вопросу по индексу"""
        locator = (By.XPATH, f"(//div[contains(@class, 'accordion__heading')])[{index}]")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
