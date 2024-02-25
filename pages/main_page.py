import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage, MainPageLocators):

    @allure.step('Кликаем по кнопке "Заказать" в хедер')
    def click_order_button_header(self):
        self.click_on_element(self.UP_ORDER_BUTTON)

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_order_button_down(self):
        self.scroll_to_element(self.DOWN_ORDER_BUTTON)
        self.click_on_element(self.DOWN_ORDER_BUTTON)

    @allure.step('Кликаем по лого самоката')
    def click_scooter_logo(self):
        self.click_on_element(self.LOGO_SCOOTER)

    @allure.step('Кликаем по лого яндекса')
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
