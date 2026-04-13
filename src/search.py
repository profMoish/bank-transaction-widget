import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """
    Ищет банковские операции по строке в описании.

    Args:
        data: список словарей с данными о банковских операциях.
        search: строка поиска (поддерживает регулярные выражения).

    Returns:
        Список словарей, у которых в поле 'description' найдено вхождение строки поиска.
    """
    r = []
    for row in data:
        description = row.get('description')
        if isinstance(description, str) and re.search(search, description, re.IGNORECASE):
            r.append(row)

    return r