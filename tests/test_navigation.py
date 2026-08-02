# tests/test_navigation.py
import allure
import pytest
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Запоминаем текущее окно
        main_window = driver.current_window_handle

        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()

        # Переключаемся на новое окно
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Ожидаем загрузки Дзена
        WebDriverWait(driver, 10).until(
            EC.url_contains("dzen.ru")
        )

        # Проверяем URL
        assert "dzen.ru" in driver.current_url, \
            f"Открылся не Дзен. Текущий URL: {driver.current_url}"
