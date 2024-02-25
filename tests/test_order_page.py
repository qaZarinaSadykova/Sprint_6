from conftest import driver
import allure

from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrder:

    @allure.title('Создание заказа в хедере')
    @allure.description('Позитивный сценарий - успешный заказ в хедере')
    def test_order_in_header_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_header()
        order_page.order_flow()
        order = order_page.get_text_status()
        assert 'Номер заказа:' in order

    @allure.title('Создание заказа внизу страницы')
    @allure.description('Позитивный сценарий - успешный заказ внизу страницы')
    def test_order_down_button_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_down()
        order_page.order_flow()
        order = order_page.get_text_status()
        assert 'Номер заказа:' in order
