# tests/test_order_flow.py
import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Оформление заказа")
class TestOrderFlow:
    """Тесты для проверки оформления заказа"""

    ORDER_DATA = [
        {
            "name": "Иван",
            "surname": "Петров",
            "address": "ул. Ленина, д. 10",
            "metro": "Черкизовская",
            "phone": "+79123456789",
            "delivery_date": "25.12.2026",
            "rental_period": "сутки",
            "color": "black",
            "comment": "Позвонить за 30 минут"
        },
        {
            "name": "Анна",
            "surname": "Иванова",
            "address": "пр. Мира, д. 25",
            "metro": "Сокольники",
            "phone": "+79998887766",
            "delivery_date": "26.12.2026",
            "rental_period": "двое суток",
            "color": "grey",
            "comment": "Домофон не работает"
        }
    ]

    @allure.title("Успешное оформление заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_successful_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_button_top()

        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )

        order_page.fill_second_form(
            order_data["delivery_date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )

        assert order_page.check_order_success(), "Заказ не был оформлен"

    @allure.title("Успешное оформление заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_successful_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_order_button_bottom()

        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )

        order_page.fill_second_form(
            order_data["delivery_date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )

        assert order_page.check_order_success(), "Заказ не был оформлен"
