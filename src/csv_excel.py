import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader


def get_operations_form_csv_file(path: str):
    """ Returns a pandas DataFrame from a csv file """
    try:
        return pd.read_csv(path)
    except FileNotFoundError as e:
        return []


def get_operations_form_excel_file(path: str):
    """ Returns a pandas DataFrame from a excel file """
    try:
        return pd.read_excel(path)
    except FileNotFoundError as e:
        return []