import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import allure
import os


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера Firefox"""
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    # Увеличиваем таймауты
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    yield driver

    # Закрываем драйвер
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    """Фикстура для страницы заказа"""
    from pages.order_page import OrderPage
    return OrderPage(driver)


# Хук для снятия скриншота при падении теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)