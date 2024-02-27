from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Поле ввод имени
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')

    # Поле ввод фамилии
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')

    # Поле ввод адреса
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')

    # Поле ввода станции
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')

    # Метро Аэропорт в списке
    STATION_AIRPORT = (By.XPATH, f'//div[text()= "Аэропорт"]')

    # Поле ввода телефона
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    # Кнопка Далее
    NEXT_BUTTON = (By.XPATH, '//button[text()= "Далее"]')

    # Поле выбора даты доставки
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')

    # Сегодня
    TODAY = (By.CSS_SELECTOR, '.react-datepicker__day--today')

    # Поле выбора периода аренды
    PERIOD_OF_RENT = (By.CLASS_NAME, 'Dropdown-placeholder')

    # Время аренды
    DAY_IN_DROPDOWN = (By.XPATH, '//div[text()="сутки"]')

    # Чекбокс "Серая безисходность"
    GREY_CHECKBOX = (By.ID, 'grey')

    # Поле для ввода комментария для курьера
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')

    # Кнопка Заказать
    ORDER_BUTTON = (By.XPATH, '(//button[text()= "Заказать"])[2]')

    # Кнопка Да
    YES_BUTTON = (By.XPATH, '//button[text()= "Да"]')

    # Окно об успешном заказе
    WINDOW_STATUS = (By.XPATH, "//div[@class = 'Order_Text__2broi']")
