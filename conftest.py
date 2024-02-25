from selenium import webdriver
import pytest
from locators.main_page_locators import MainPageLocators


@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument("--incognito")
    # Открываем драйвер перед каждым тестом
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    # Закрываем драйвер после выполнения каждого метода
    driver.quit()


@pytest.fixture
def accept_cookie(driver):
    driver.find_element(*MainPageLocators.COOKIE_ACCEPT).click()
