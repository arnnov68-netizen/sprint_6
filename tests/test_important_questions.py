import allure
import pytest
from locators.main_page_locators import MainPageLocators


@allure.feature("Вопросы о важном")
class TestImportantQuestions:
    """Тесты для проверки выпадающего списка 'Вопросы о важном'"""

    @allure.title("Проверка ответа на вопрос: {question_text}")
    @pytest.mark.parametrize("question_text, expected_answer",
                             MainPageLocators.QUESTIONS
                             )
    def test_question_answer_by_text(self, main_page, question_text, expected_answer):
        """
        Проверка, что при клике на вопрос открывается правильный ответ
        Используем стабильный способ - поиск по тексту вопроса
        """
        main_page.open()

        # Кликаем на вопрос по его тексту
        main_page.click_question_by_text(question_text)

        # Получаем ответ по тексту вопроса
        actual_answer = main_page.get_answer_by_question_text(question_text)

        assert actual_answer, f"Ответ на вопрос '{question_text}' пустой"
        assert actual_answer == expected_answer, \
            f"Текст ответа на вопрос '{question_text}' не совпадает\n" \
            f"Ожидалось: {expected_answer}\n" \
            f"Получено: {actual_answer}"

    @allure.title("Проверка ответа на вопрос #{index}")
    @pytest.mark.parametrize("index, question_text, expected_answer",
                             [(i + 1, q, a) for i, (q, a) in enumerate(MainPageLocators.QUESTIONS)]
                             )
    def test_question_answer_by_index(self, main_page, index, question_text, expected_answer):
        """
        Проверка, что при клике на вопрос открывается правильный ответ
        Используем стабильный способ - поиск по позиции
        """
        main_page.open()

        # Кликаем на вопрос по его позиции
        main_page.click_question_by_index(index)

        # Получаем ответ по позиции
        actual_answer = main_page.get_answer_by_index(index)

        assert actual_answer, f"Ответ на вопрос {index} пустой"
        assert actual_answer == expected_answer, \
            f"Текст ответа на вопрос {index} не совпадает\n" \
            f"Ожидалось: {expected_answer}\n" \
            f"Получено: {actual_answer}"