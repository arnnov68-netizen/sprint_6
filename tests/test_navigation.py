# tests/test_navigation.py
import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        # Кликаем на логотип и переключаемся на новое окно
        main_page.click_yandex_logo_and_switch_to_new_window()

        # Проверяем URL
        assert "dzen.ru" in main_page.get_current_url(), \
            f"Открылся не Дзен. Текущий URL: {main_page.get_current_url()}"
