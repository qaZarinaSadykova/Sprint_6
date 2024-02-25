from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локатор куки
    COOKIE_ACCEPT = (By.ID, 'rcc-confirm-button')
    # Заголовок вопросов
    TITLE_QUESTIONS = (By.XPATH, '//div(text() = "Вопросы о важном"')
    # Локаторы с вопросами и ответами
    QUESTION_1 = (By.ID, 'accordion__heading-0')
    ANSWER_1 = (By.ID, 'accordion__panel-0')
    QUESTION_2 = (By.ID, 'accordion__heading-1')
    ANSWER_2 = (By.ID, 'accordion__panel-1')
    QUESTION_3 = (By.ID, 'accordion__heading-2')
    ANSWER_3 = (By.ID, 'accordion__panel-2')
    QUESTION_4 = (By.ID, 'accordion__heading-3')
    ANSWER_4 = (By.ID, 'accordion__panel-3')
    QUESTION_5 = (By.ID, 'accordion__heading-4')
    ANSWER_5 = (By.ID, 'accordion__panel-4')
    QUESTION_6 = (By.ID, 'accordion__heading-5')
    ANSWER_6 = (By.ID, 'accordion__panel-5')
    QUESTION_7 = (By.ID, 'accordion__heading-6')
    ANSWER_7 = (By.ID, 'accordion__panel-6')
    QUESTION_8 = (By.ID, 'accordion__heading-7')
    ANSWER_8 = (By.ID, 'accordion__panel-7')

    # Локатор входа верхний
    UP_ORDER_BUTTON = (By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']")

    # Локатор входа нижний
    DOWN_ORDER_BUTTON = (By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']")

    # Логотип самокат
    LOGO_SCOOTER = [By.XPATH, '//img[@alt="Scooter"]']

    # Логотип яндекс
    LOGO_YANDEX = [By.XPATH, '//img[@alt="Yandex"]']
