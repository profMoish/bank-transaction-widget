def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    if len(card_number) != 16:
        raise ValueError("Неверное кол-во цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функцию маскировки номера банковского счета"""
    if len(account) != 20:
        raise ValueError("Неверное кол-во цифр")
    return f"**{account[-4:]}"
