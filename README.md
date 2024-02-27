Sprint_6
Автотест для проекта  - сервис аренды самокатов - https://qa-scooter.praktikum-services.ru
Сервис аренды самокатов предоставлет возможность заказать самокат с доставкой в любою точку Москвы на любой срок

```
1. Создание проекта для автоматизированного тестирования сервиса

Создать в IDE новый проект
Развернуть тестовое окуржение
Установить  GeckoDriver для браузера -  Mozilla Firefox
Создать в проекте дериторию test_page_object  - в ней создавать все необходимые папки и файлы
В корне дериктории добавить файл .gitignore - (JetBrains,Python), чтобы в проект не попало ничего лишнего
В корне дериктории создать папку tests - в ней заводить файлы с тестами в разрезе функционала
В корне дериктории создать папку pages - в ней заводить файлы c методами в разрезе страниц и base_page  - общие методы
В корне дериктории создать папку с локаторами - в ней заводить файлы с тестами в разрезе страниц
В корне дериктории создать файл data.py - для хранения тестовых данных
В корне дериктории создать README.md c описанием функционала и структуры проекта
В корне дериктории созадть файл requirments.txt :
    (версии могут отличатся)
    allure-pytest==2.13.2 
    pytest==8.0.1
    selenium==4.18.1
В корне дериктории созадть файл conftest - Настроить в conftest запуск браузера для каждого метода в тесте
После каждого метода закрывать браузер

```
```
2. Как добавить новый тест

- Создать новый файл теста в директории `tests` с префиксом `test_`:
test_new_feature.py
Написать класс TestSomeFeature():
Все методы начинать с префиксом `test_`
В конце каждого метода добпавлять assert
```
```
4. Импорты:
# locators
from selenium.webdriver.common.by import By

# conftest 
from selenium import webdriver
import pytest

# data
from test_page_object.locators.main_page_locators import MainPageLocators

# data - обязательные импорты
import allure
from test_page_object.locators.main_page_locators import MainPageLocators

# в каждый тестовый файл - обязательные импорты
import allure
соответсвующие pages и другие файлы
```
```
Запустить тесты и убедиться, что все проходят успешно:

Команда для запуска всех тестов: pytest -v
Команда дляь запуска тестов c формированием отчетов: pytest -v  --alluredir=allure_results
Команда для просмотра html отчета в браузере: allure serve allure_results


# Как внести изменения

1. Создать отдельную ветку для разработки:
```
```
git checkout -b feature/new_feature
```
```
2. Внести необходимые изменения в тесты.

3. Запустить тесты и убедиться, что все проходят успешно:
```
```
4. Закоммитить изменения:
git commit -m "Add new feature"
```
```
5. Запушить изменения в репозиторий:

git push origin feature/new_feature
```
```
6. Создать Pull Request на GitHub и ожидать ревью. 

### Структура файлов проекта

в папке tests:
    файл [test_main_page.py]
    test_text_of_questions - Проверка соответствия текста в вопросах
    test_answer_to_questions - Проверка соответствия ответа на вопрос
    
    файл [test_order_page.py]
    test_order_in_header_success - Создание заказа в хедере
    test_order_down_button_success - Создание заказа внизу страницы
    
    файл [test_logo_redirect.py]
    test_logo_redirect_to_main_page_success - Переход на главную страницу при клике на лого Самокат
    test_logo_redirect_to_dzen_frame_success - Переход на окно Дзен
    
в папке pages:
    файл [base_page.py] - базовые методы для всех тестов и страниц
    файл [main_page.py] - методы для главной страницы
    файл [order_page.py] - методы и флоу для заказа самоката
    
в папке locators:
    файл [main_page_locators.py] - локаторы на главной странице
    файл [order_page_locators.py] - локаторы для флоу заказа самоката    
    