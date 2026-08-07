# pages/base_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15  # Увеличенный таймаут для Firefox

    @allure.step("Открыть страницу по URL: {url}")
    def open_page(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator, timeout=None):
        """Кликнуть на элемент"""
        if timeout is None:
            timeout = self.default_timeout

        # Прокручиваем к элементу
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Ожидаем, что элемент станет кликабельным
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

        # Кликаем по элементу
        element.click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def enter_text(self, locator, text, timeout=None):
        """Ввести текст в поле"""
        if timeout is None:
            timeout = self.default_timeout
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator, timeout=None):
        """Проверить, что элемент видим"""
        if timeout is None:
            timeout = self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить кликабельность элемента: {locator}")
    def is_element_clickable(self, locator, timeout=None):
        """Проверить, что элемент кликабелен"""
        if timeout is None:
            timeout = self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    @allure.step("Получить количество открытых окон")
    def get_window_handles_count(self):
        """Получить количество открытых окон"""
        return len(self.driver.window_handles)

    @allure.step("Получить список всех окон")
    def get_window_handles(self):
        """Получить список всех окон"""
        return self.driver.window_handles

    @allure.step("Переключиться на окно: {window_handle}")
    def switch_to_window(self, window_handle):
        """Переключиться на окно по handle"""
        self.driver.switch_to.window(window_handle)

    @allure.step("Получить handle текущего окна")
    def get_current_window_handle(self):
        """Получить handle текущего окна"""
        return self.driver.current_window_handle

    @allure.step("Ожидать появления нового окна")
    def wait_for_new_window(self, initial_window_count, timeout=None):
        """Ожидать появления нового окна"""
        if timeout is None:
            timeout = self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > initial_window_count
        )

    @allure.step("Получить handle нового окна")
    def get_new_window_handle(self, main_window_handle):
        """Получить handle нового окна"""
        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                return handle
        return None

    @allure.step("Ожидать, что URL содержит: {url_part}")
    def wait_for_url_contains(self, url_part, timeout=None):
        """Ожидать, что URL содержит указанную часть"""
        if timeout is None:
            timeout = self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part in d.current_url
        )

    @allure.step("Ожидать, что элемент видим: {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        """Ожидать, что элемент станет видимым"""
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать, что элемент кликабелен: {locator}")
    def wait_for_element_clickable(self, locator, timeout=None):
        """Ожидать, что элемент станет кликабельным"""
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Получить текст элемента: {locator}")
    def get_element_text(self, locator, timeout=None):
        """Получить текст элемента"""
        if timeout is None:
            timeout = self.default_timeout
        element = self.find_element(locator, timeout)
        return element.text

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to_element(self, locator, timeout=None):
        """Прокрутить к элементу"""
        if timeout is None:
            timeout = self.default_timeout
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
