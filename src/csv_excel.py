import pandas as pd


def get_operations_form_csv_file(path: str):
    """Returns a pandas DataFrame from a csv file"""
    try:
        return pd.read_csv(path, sep=";").to_dict(orient="records")  #
    except FileNotFoundError:
        return []


def get_operations_form_excel_file(path: str):
    """Returns a pandas DataFrame from a excel file"""
    try:
        r = pd.read_excel(path).to_dict(orient="records")
        return r
    except FileNotFoundError:
        return []
