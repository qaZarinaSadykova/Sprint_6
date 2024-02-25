import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import UserData


class OrderPage(BasePage, OrderPageLocators):

    @allure.step('Заполняем поле - имя')
    def input_name(self, name):
        self.set_text_in_element(self.NAME_INPUT, name)

    @allure.step('Заполняем поле - фамилия')
    def input_surname(self, surname):
        self.set_text_in_element(self.SURNAME_INPUT, surname)

    @allure.step('Заполняем поле - фамилия')
    def input_address(self, address):
        self.set_text_in_element(self.ADDRESS_INPUT, address)

    @allure.step('Кликаем по списку "метро"')
    def click_metro_station(self):
        self.click_on_element(self.METRO_STATION_INPUT)

    @allure.step('Кликаем по станции "Аэропорт"')
    def click_station_airport(self):
        self.click_on_element(self.STATION_AIRPORT)

    @allure.step('Заполняем поле - телефон')
    def input_phone(self, phone):
        self.set_text_in_element(self.PHONE_INPUT, phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(self.NEXT_BUTTON)

    @allure.step('Кликаем по календарю')
    def click_calendar(self):
        self.click_on_element(self.DATE_INPUT)

    @allure.step('Кликаем на текущую дату')
    def click_today(self):
        self.click_on_element(self.TODAY)

    @allure.step('Кликаем на срок аренды')
    def click_period_of_rent(self):
        self.click_on_element(self.PERIOD_OF_RENT)

    @allure.step('Выбираем "сутки" в выпадающем списке')
    def choose_day_in_dropdown(self):
        self.click_on_element(self.DAY_IN_DROPDOWN)

    @allure.step('Выбираем серый цвет')
    def click_grey_checkbox(self):
        self.click_on_element(self.GREY_CHECKBOX)

    @allure.step('Вводим комментарий для курьера')
    def input_comment(self, text):
        self.set_text_in_element(self.COMMENT_INPUT, text)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(self.ORDER_BUTTON)

    @allure.step('Кликаем на кнопку "Да"')
    def click_yes_button(self):
        self.click_on_element(self.YES_BUTTON)

    @allure.step('Получаем текст заказа')
    def get_text_status(self):
        return self.get_text_from_element(self.WINDOW_STATUS)

    @allure.step('Проходим флоу заказа самоката')
    def order_flow(self):
        self.input_name(UserData.user_data_1['name'])
        self.input_surname(UserData.user_data_1['surname'])
        self.input_address(UserData.user_data_1['address'])
        self.click_metro_station()
        self.click_station_airport()
        self.input_phone(UserData.user_data_1['phone'])
        self.click_next_button()
        self.click_calendar()
        self.click_today()
        self.click_period_of_rent()
        self.choose_day_in_dropdown()
        self.click_grey_checkbox()
        self.input_comment(UserData.user_data_1['text'])
        self.click_order_button()
        self.click_yes_button()
