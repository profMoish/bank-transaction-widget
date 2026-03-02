import masks


def mask_account_card(number: str) -> str:
    """Функцию маскировки номера банковской карты и номера банковского счета"""
    if "Счет" in number:
        return number[:-20] + masks.get_mask_account(number[-20:])
    else:
        return number[:-16] + masks.get_mask_card_number(number[-16:])
