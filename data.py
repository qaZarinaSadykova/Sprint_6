from locators.main_page_locators import MainPageLocators


class Questions:
    first: str = "Сколько это стоит? И как оплатить?"

    second: str = "Хочу сразу несколько самокатов! Так можно?"

    third: str = "Как рассчитывается время аренды?"

    fourth: str = "Можно ли заказать самокат прямо на сегодня?"

    fifth: str = "Можно ли продлить заказ или вернуть самокат раньше?"

    sixth: str = "Вы привозите зарядку вместе с самокатом?"

    seventh: str = "Можно ли отменить заказ?"

    eighth: str = "Я жизу за МКАДом, привезёте?"


class Answers:
    first: str = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    second: str = ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                   "можете просто сделать несколько заказов — один за другим.")

    third: str = ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени "
                  "аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в "
                  "20:30, суточная аренда закончится 9 мая в 20:30.")

    fourth: str = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    fifth: str = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    sixth: str = ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься"
                  " без передышек и во сне. Зарядка не понадобится.")

    seventh: str = ("Да, пока самокат не привезли. Штрафа не будет, "
                    "объяснительной записки тоже не попросим. Все же свои.")

    eighth: str = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class AnswersToQuestions:
    data_a_q = (
        [MainPageLocators.QUESTION_1, Questions.first, MainPageLocators.ANSWER_1, Answers.first],
        [MainPageLocators.QUESTION_2, Questions.second, MainPageLocators.ANSWER_2, Answers.second],
        [MainPageLocators.QUESTION_3, Questions.third, MainPageLocators.ANSWER_3, Answers.third],
        [MainPageLocators.QUESTION_4, Questions.fourth, MainPageLocators.ANSWER_4, Answers.fourth],
        [MainPageLocators.QUESTION_5, Questions.fifth, MainPageLocators.ANSWER_5, Answers.fifth],
        [MainPageLocators.QUESTION_6, Questions.sixth, MainPageLocators.ANSWER_6, Answers.sixth],
        [MainPageLocators.QUESTION_7, Questions.seventh, MainPageLocators.ANSWER_7, Answers.seventh],
        [MainPageLocators.QUESTION_8, Questions.eighth, MainPageLocators.ANSWER_8, Answers.eighth]
    )


class UserData:
    user_data_1 = {
        'name': 'Зарина',
        'surname': 'Садыкова',
        'address': 'ул.Тест, дом 30',
        'phone': '+865432245688',
        'text': 'звонить с 12:00 до 20:00'
    }

    user_data_2 = {
        'name': 'Урун',
        'surname': 'Ахмедов',
        'address': 'ул.Тесттест, дом 45, кв 15',
        'phone': '+86543278657899',
        'text': 'Осторожно, во дворе злая собака!'
    }
