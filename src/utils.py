import json
import logging

file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
my_logger = logging.getLogger(__name__)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.DEBUG)


def get_operations_form_json_file(path):
    """Returns a list of operations form json file"""
    my_logger.info("Попытка прочитать транзацкции из json файла")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            my_logger.info(f'Файл "{path}" открыли')
            result = json.load(f)
            my_logger.info("Содержимое файла конверитровали в json")
            return result if isinstance(result, list) else []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        my_logger.error(f"Ошибка при конвертации в json: {e}")
        return []
    finally:
        my_logger.info("Заверешение попытки прочитать json из файла")
