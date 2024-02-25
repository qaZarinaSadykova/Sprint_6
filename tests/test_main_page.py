import allure
import pytest
import data
from conftest import driver
from pages.base_page import BasePage


class TestMainPage:
    @allure.title('Проверка соответствия текста в вопросах')
    @pytest.mark.parametrize('question, question_text, answer, result', [*data.AnswersToQuestions.data_a_q])
    def test_text_of_questions(self, driver, question, question_text, answer, result):
        base_page = BasePage(driver)
        base_page.scroll_to_element(question)
        base_page.click_on_element(question)
        text_in_question_button = base_page.find_element_with_wait(question)
        assert text_in_question_button.text == question_text

    @allure.title('Проверка соответствия ответа на вопрос')
    @pytest.mark.parametrize('question, question_text, answer, result', [*data.AnswersToQuestions.data_a_q])
    def test_answer_to_questions(self, driver, question, question_text, answer, result):
        base_page = BasePage(driver)
        base_page.scroll_to_element(question)
        base_page.click_on_element(question)
        text_in_answer_button = base_page.find_element_with_wait(answer)
        assert text_in_answer_button.text == result
