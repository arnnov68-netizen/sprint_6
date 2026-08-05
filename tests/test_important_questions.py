# tests/test_important_questions.py
import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature("Главная страница")
@allure.story("FAQ")
class TestFAQ:

    @allure.title("Проверка ответов на все вопросы в разделе FAQ")
    def test_all_questions_and_answers(self, driver):
        """Проверка, что при клике на вопрос открывается правильный ответ"""
        main_page = MainPage(driver)
        main_page.open()

        questions_and_answers = MainPageLocators.QUESTIONS

        for index, (question_text, expected_answer) in enumerate(questions_and_answers, 1):
            with allure.step(f"Проверка вопроса №{index}: '{question_text}'"):
                # Прокручиваем к вопросу
                main_page.scroll_to_question(index)

                # Кликаем на вопрос
                main_page.click_question_by_index(index)

                # Получаем ответ
                actual_answer = main_page.get_answer_by_index(index)

                assert actual_answer == expected_answer, \
                    f"Для вопроса '{question_text}' ожидался ответ '{expected_answer}', получен '{actual_answer}'"
