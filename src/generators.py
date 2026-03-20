def filter_by_currency(transactions: list, currency: str):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]['code'] == currency:
            yield transaction
    yield None

def transaction_descriptions(transactions: list):
    for transaction in transactions:
        yield transaction["description"]
    yield None

def card_number_generator(start: int, end: int):
    for number in range(start, end+1):
        card = str(number).zfill(16)

        formatted = f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"

        yield formatted