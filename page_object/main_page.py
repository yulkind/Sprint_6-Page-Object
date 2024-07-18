import allure

from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получение текста ответа')
    def get_answer_text(self, number):
        self.wait_for_element(MainPageLocators.SCOOTER_LOGO_HEADER)
        self.scroll_and_click_on_element(MainPageLocators.COOKIE)
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)
        question = self.format_locators(MainPageLocators.FAQ_QUESTION, number)
        answer = self.format_locators(MainPageLocators.FAQ_ANSWER, number)
        self.click_on_element(question)
        answer_text = self.get_text(answer)
        return answer_text
