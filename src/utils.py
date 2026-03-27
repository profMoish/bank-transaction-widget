import json


def get_operations_form_json_file(path):
    try:
        with open(path) as f:
            result = json.load(f)
            return result if isinstance(result, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


