# pages/base_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15  # Увеличенный таймаут для Firefox

    @allure.step("Открыть страницу по URL")
    def open_page(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=None):
        """Кликнуть на элемент"""
        if timeout is None:
            timeout = self.default_timeout
        element = self.find_element(locator, timeout)
        # Прокручиваем к элементу
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        # Ожидаем, что элемент станет кликабельным
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        # Для Firefox иногда нужно немного подождать
        import time
        time.sleep(0.5)
        element.click()

    def enter_text(self, locator, text, timeout=None):
        """Ввести текст в поле"""
        if timeout is None:
            timeout = self.default_timeout
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=None):
        """Проверить, что элемент видим"""
        if timeout is None:
            timeout = self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def is_element_clickable(self, locator, timeout=None):
        """Проверить, что элемент кликабелен"""
        if timeout is None:
            timeout = self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def get_window_handles_count(self):
        """Получить количество открытых окон"""
        return len(self.driver.window_handles)

    def get_window_handles(self):
        """Получить список всех окон"""
        return self.driver.window_handles

    def switch_to_window(self, window_handle):
        """Переключиться на окно по handle"""
        self.driver.switch_to.window(window_handle)

    def get_current_window_handle(self):
        """Получить handle текущего окна"""
        return self.driver.current_window_handle

    def wait_for_new_window(self, initial_window_count, timeout=None):
        """Ожидать появления нового окна"""
        if timeout is None:
            timeout = self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > initial_window_count
        )

    def get_new_window_handle(self, main_window_handle):
        """Получить handle нового окна"""
        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                return handle
        return None

    def wait_for_url_contains(self, url_part, timeout=None):
        """Ожидать, что URL содержит указанную часть"""
        if timeout is None:
            timeout = self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            lambda d: url_part in d.current_url
        )

    def wait_for_element_text(self, locator, expected_text, timeout=None):
        """Ожидать, что текст элемента содержит ожидаемый текст"""
        if timeout is None:
            timeout = self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )
