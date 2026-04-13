from src.widget import get_data


def filter_by_state(_list: list, state: str = "EXECUTED") -> list:
    """Функция филтрует список словарей по ключю state."""
    list = [x for x in _list if x.get("state") is not None]
    return [transaction for transaction in list if transaction["state"] == state]


def sort_by_date(_list: list, reverse: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    list = [x for x in _list if x.get("date") is not None]
    return sorted(list, key=lambda x: get_data(x.get("date")), reverse=reverse)
