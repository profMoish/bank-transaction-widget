# bank-transaction-widget

Виджет с банковскими операциями: набор функций на Python для маскировки номеров карт и счетов, а также форматирования даты для отображения в интерфейсе.

## Возможности

### `masks.py`

- **`get_mask_card_number(card_number)`** — маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры:

  ```python
  get_mask_card_number("7000792289606361")
  # "7000 79** **** 6361"
  ```

- **`get_mask_account(account)`** — маскирует номер банковского счёта, оставляя видимыми только последние 4 цифры:

  ```python
  get_mask_account("73654108430135874305")
  # "**4305"
  ```

### `widget.py`

- **`mask_account_card(number)`** — определяет по строке, карта это или счёт (по наличию слова «Счет»), и применяет соответствующую маску:

  ```python
  mask_account_card("Visa Platinum 7000792289606361")
  # "Visa Platinum 7000 79** **** 6361"

  mask_account_card("Счет 73654108430135874305")
  # "Счет **4305"
  ```

- **`get_data(date)`** — форматирует дату из ISO-формата в `ДД.ММ.ГГГГ`:

  ```python
  get_data("2019-07-03T18:35:29.512364")
  # "03.07.2019"
  ```

## Структура проекта

```
bank-transaction-widget/
├── src/
│   ├── masks.py     # маскировка карт и счетов
│   └── widget.py     # определение типа номера и форматирование даты
├── tests/            # тесты
├── pyproject.toml    # зависимости и конфигурация (Poetry)
└── .flake8           # конфигурация линтера
```

## Требования

- Python 3.14+
- [Poetry](https://python-poetry.org/) для управления зависимостями

## Установка

```bash
git clone https://github.com/mrMoish/bank-transaction-widget.git
cd bank-transaction-widget
poetry install
```

## Использование

```python
from src.widget import mask_account_card, get_data

print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_data("2019-07-03T18:35:29.512364"))
```

## Тесты и линтинг

```bash
poetry run pytest
poetry run flake8
poetry run mypy src
poetry run black .
poetry run isort .
```

Настройки инструментов заданы в `pyproject.toml` и `.flake8`:

- `black` / `isort` — длина строки 119 символов
- `mypy` — строгий режим (`disallow_untyped_defs`, `no_implicit_optional`, `warn_return_any`)

## Зависимости

Проект не имеет внешних runtime-зависимостей — только dev-инструменты:

| Пакет | Назначение |
|---|---|
| `flake8` | проверка стиля кода |
| `mypy` | статическая проверка типов |
| `black` | автоформатирование |
| `isort` | сортировка импортов |

## Лицензия

Не указана.
