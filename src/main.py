from src.csv_excel import get_operations_form_csv_file, get_operations_form_excel_file
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import get_operations_form_json_file
from src.widget import mask_account_card


def main():
    """
    Функция отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    r = input("Введите число: ")

    if r == "1":
        print("Для обработки выбран JSON-файл")
        operations = get_operations_form_json_file("data/operations.json")
    elif r == "2":
        print("Для обработки выбран CSV-файл")
        operations = get_operations_form_csv_file("data/transactions.csv")
    else:
        print("Для обработки выбран XLSX-файл")
        operations = get_operations_form_excel_file("data/transactions_excel.xlsx")
    print()

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        r = input("Введите статус: ").upper()

        if r in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {r}")
            print()

            operations = filter_by_state(operations, r)
            break
        else:
            print(f'Статус операции "{r}" недоступен.')
            print()

    print("Отсортировать операции по дате?")
    r = input("Да/Нет: ").lower()

    if r == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        reverse = input("по возрастанию/по убыванию: ").lower()
        print()

        if reverse == "да":
            operations = sort_by_date(operations)
        else:
            operations = sort_by_date(operations, reverse=False)

    print("Выводить только рублевые транзакции?")
    r = input("Да/Нет: ").lower()
    print()

    new_operations = []
    if r == "да":
        for operation in operations:
            if operation["operationAmount"]["currency"]["code"] == "RUB":
                new_operations.append(operation)
        operations = new_operations

    print("Отфильтровать список транзакций по определенному слову в описании?")
    i = input("Да/Нет: ").lower()
    if i == "да":
        search = input("Введите слово: ")
        operations = process_bank_search(operations, search)

    print()

    print("Распечатываю итоговый список транзакций...")
    print()

    print(f"Всего банковских операций в выборке: {len(operations)}")
    print()
    if len(operations) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    for operation in operations:
        print(operation["date"][:10], operation["description"])
        if isinstance(operation.get("from"), str):
            print(f'{mask_account_card(operation.get("from"))} -> {mask_account_card(operation["to"])}')
        else:
            print(mask_account_card(operation["to"]))

        print()
