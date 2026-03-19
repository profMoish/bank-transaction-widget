from src.widget import get_data


def filter_by_state(_list: list, state: str = "EXECUTED") -> list:
    """Функция филтрует список словарей по ключю state."""
    return [transaction for transaction in _list if transaction["state"] == state]


def sort_by_date(_list: list, reverse: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(_list, key=lambda x: get_data(x["date"]), reverse=reverse)
