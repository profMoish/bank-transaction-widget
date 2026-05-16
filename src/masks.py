import logging

file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
my_logger = logging.getLogger(__name__)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    my_logger.info("Запуск функции для маскировки номера банковской карты")
    if len(card_number) != 16:
        my_logger.error(f"Неверное кол-во цифр. Ожидалось 16, а не {len(card_number)}")
        raise ValueError("Неверное кол-во цифр")

    my_logger.info("Завершение функции для маскировки номера банковской карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функцию маскировки номера банковского счета"""
    my_logger.info("Запуск функции для маскировки номера банковского счета")
    if len(account) != 20:
        my_logger.error(f"Неверное кол-во цифр. Ожидалось 20, а не {len(account)}")
        raise ValueError("Неверное кол-во цифр")

    my_logger.info("Завершение функции для маскировки номера банковского счета")
    return f"**{account[-4:]}"
