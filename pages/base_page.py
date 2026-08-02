# pages/base_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL")
    def open_page(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        """Кликнуть на элемент"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator, timeout=10):
        """Проверить, что элемент видим"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
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
