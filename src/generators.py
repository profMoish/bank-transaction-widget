def filter_by_currency(transactions: list, currency: str):
    """Фунция генератор которая возвращает отфилтрованые по валюте транзакции"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list):
    """Фунция генератор которая возвращает описания транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """Фунция генератор которая генерируют номера карт"""
    for number in range(start, end + 1):
        card = str(number).zfill(16)

        formatted = f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"

        yield formatted
