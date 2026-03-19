from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функцию маскировки номера банковской карты и номера банковского счета"""

    _list = number.split(' ')

    if _list[0] == 'Счет' and len(_list) == 2:
        if _list[1].isdigit():
            return _list[0] + " " + get_mask_account(_list[1])
        else:
            raise ValueError('В номере счета не должно быть букв')
    elif len(_list[-1]) == 16 and _list[-1].isdigit():
        return number[:-16] + get_mask_card_number(_list[-1])
    else:
        raise ValueError('Неверный формат')


def get_data(date: str) -> str:
    """Функция форматирования даты"""
    if not date or not date.strip():
        raise ValueError('строка с датой пуста')
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
