def filter_by_state(_list, state='EXECUTED') -> list:
    """Функция филтрует список словарей по ключю state."""
    return [transaction for transaction in _list if transaction['state'] == state]


def sort_by_date(_list, reverse=True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(_list, key=lambda x: x['date'], reverse=reverse)
