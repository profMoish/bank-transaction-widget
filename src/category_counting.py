from collections import Counter


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество банковских операций по каждой категории.

    Аргументы:
        data: Список словарей с банковскими операциями.
              Каждый словарь должен содержать ключ 'description'.
        categories: Список категорий операций для подсчёта.

    Возвращает:
        Словарь, где ключи — названия категорий, а значения —
        количество операций в каждой категории.
    """

    all_description = [row["description"] for row in data]

    counted = Counter(all_description)

    r = {}

    for row in categories:
        r[row] = counted[row]

    return r
