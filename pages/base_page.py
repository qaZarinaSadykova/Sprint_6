import allure

from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(MainPageLocators):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем появление локатора')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получаем текст элемент')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Водим текст в элементы')
    def set_text_in_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Скролим до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текущей url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переходим на другую вкладку')
    def switch_to_another_window(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 20).until(expected_conditions.url_contains(url))
