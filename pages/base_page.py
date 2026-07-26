from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import allure
import time


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        """Открыть страницу по URL"""
        try:
            self.driver.get(url)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=10):
        """Найти элемент"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    @allure.step("Найти все элементы")
    def find_elements(self, locator, timeout=10):
        """Найти все элементы"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    @allure.step("Кликнуть на элемент с повторными попытками")
    def click_element(self, locator, timeout=10, retries=3):
        """Кликнуть на элемент с повторными попытками при перехвате"""
        for attempt in range(retries):
            try:
                element = self.find_element(locator, timeout)
                if element:
                    # Прокрутка к элементу
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    time.sleep(0.3)
                    # Попытка клика через JavaScript если обычный клик не работает
                    try:
                        element.click()
                    except ElementClickInterceptedException:
                        self.driver.execute_script("arguments[0].click();", element)
                    return element
            except Exception as e:
                if attempt == retries - 1:
                    allure.attach(self.driver.get_screenshot_as_png(), name="click_error",
                                  attachment_type=allure.attachment_type.PNG)
                    raise e
                time.sleep(0.5)
        return None

    @allure.step("Ввести текст '{text}' в поле")
    def input_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            return element
        return None

    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text if element else ""

    @allure.step("Проверить, что элемент видим")
    def is_element_visible(self, locator, timeout=10):
        """Проверить, что элемент видим"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator):
        """Прокрутить к элементу"""
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.3)
            return element
        return None

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        """Переключиться на новое окно"""
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Подождать {seconds} секунд")
    def wait_seconds(self, seconds):
        """Ожидание в секундах"""
        time.sleep(seconds)