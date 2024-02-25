import allure
from conftest import driver
from pages.main_page import MainPage


class TestLogoRedirect:

    @allure.title('Проверка перехода на "https://qa-scooter.praktikum-services.ru/" при клике на логотип Самокат')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_header()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert "https://qa-scooter.praktikum-services.ru/" in current_url

    @allure.title('Проверка перехода на "https://dzen.ru/" при клике на логотип Яндекс')
    def test_logo_redirect_to_dzen_frame_success(self, driver, url="https://dzen.ru/"):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        main_page.switch_to_another_window(url)
        current_url = main_page.get_current_url()
        assert "https://dzen.ru/" in current_url
