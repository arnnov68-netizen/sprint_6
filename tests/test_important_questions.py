# tests/test_important_questions.py
import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature("Главная страница")
@allure.story("FAQ")
class TestFAQ:

    @allure.title("Проверка ответа на вопрос №{index}: '{question_text}'")
    @pytest.mark.parametrize("index, question_text, expected_answer", [
        (index, question, answer)
        for index, (question, answer) in enumerate(MainPageLocators.QUESTIONS, 1)
    ])
    def test_faq_question(self, driver, index, question_text, expected_answer):
        """Проверка, что при клике на вопрос открывается правильный ответ"""
        main_page = MainPage(driver)
        main_page.open()

        with allure.step(f"Проверка вопроса №{index}: '{question_text}'"):
            # Прокручиваем к вопросу
            main_page.scroll_to_question(index)

            # Кликаем на вопрос
            main_page.click_question_by_index(index)

            # Получаем ответ
            actual_answer = main_page.get_answer_by_index(index)

            assert actual_answer == expected_answer, \
                f"Для вопроса '{question_text}' ожидался ответ '{expected_answer}', получен '{actual_answer}'"
