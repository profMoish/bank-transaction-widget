from tests.test_generators import transactions_3

# Виджет, который показывает несколько последних успешных банковских операций клиента.

## Основные функции

### Функция маскировки номера карты и счета

```python
from src import widget

widget.mask_account_card('Visa Platinum 7000792289606361')
widget.mask_account_card('Счет 73654108430135874305')
```

### Функция филтрации списока словарей по ключю state
```python
from src import processing

processing.filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
])
```

### Функция для сортировки транзакций по дате
```python
from src import processing

processing.sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
])
```

### Функция для филтрации по задоной валюте
```python
from src.generators import filter_by_currency

transactions = ...

usd_transactions = filter_by_currency(transactions, 'USD')
next(usd_transactions)
```

### Фунация для вывода описания транзакций
```python
from src.generators import transaction_descriptions

transactions = ...

descriptions = transaction_descriptions(transactions)
next(descriptions)
```


### Функция для генерации номеров карт
```python
from src.generators import card_number_generator 

card_number = card_number_generator(1, 5)
next(card_number)
next(card_number)
next(card_number)
next(card_number)
next(card_number)
```

### Фунция для получения списка транзакций из csv файла
```python
from src.csv_excel import get_operations_form_csv_file

get_operations_form_csv_file("data/transactions.csv")
```

### Фунция для получения списка транзакций из excel файла
```python
from src.csv_excel import get_operations_form_excel_file

get_operations_form_excel_file("data/transactions_excel.xlsx")
```



### Фунция декоратор для логирования
```python
from src.decorators import log

@log() # лог ввыводить в консоль
def func(a, b):
    pass

@log('log.txt') # лок записывать в файл
def func2(a, b):
    pass
```

## 🧪 Информация о тестировании
В проекте используется библиотека pytest для написания и запуска тестов.
### 📦 Установленные инструменты
- pytest — запуск тестов
- pytest-cov — измерение покрытия кода тестами

Установка зависимостей:
```bash
poetry add pytest
poetry add pytest-cov
```
### ▶️ Запуск тестов
Запустить все тесты:
```bash
pytest
```
Запустить тесты с выводом покрытия:
```bash
poetry run pytest --cov=src
```