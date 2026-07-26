import allure
import pytest


@allure.feature("Навигация")
class TestNavigation:
    """Тесты для проверки навигации по логотипам"""

    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, main_page):
        """
        Проверка, что клик на логотип Самоката ведет на главную страницу
        """
        main_page.open()
        main_page.click_order_button_top()

        main_page.click_scooter_logo()

        assert "qa-scooter" in main_page.get_current_url(), \
            "Клик на логотип Самоката не привел на главную страницу"

    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, main_page):
        """
        Проверка, что клик на логотип Яндекса открывает Дзен в новом окне
        """
        main_page.open()

        initial_windows = len(main_page.driver.window_handles)

        main_page.click_yandex_logo()

        current_windows = len(main_page.driver.window_handles)
        assert current_windows > initial_windows, \
            "Клик на логотип Яндекса не открыл новое окно"

        assert "dzen" in main_page.get_current_url() or "yandex" in main_page.get_current_url(), \
            f"В новом окне открылся не Дзен, а {main_page.get_current_url()}"