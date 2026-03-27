import json


def get_operations_form_json_file(path):
    """Returns a list of operations form json file"""
    try:
        with open(path) as f:
            result = json.load(f)
            return result if isinstance(result, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
