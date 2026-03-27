import os

import requests
from dotenv import load_dotenv


def get_amount(operation):
    """Returns the amount of the currency"""
    try:
        amount = operation["operationAmount"]["amount"]
        if operation["operationAmount"]["currency"]["code"] == "RUB":
            return amount
        else:
            load_dotenv()

            api_key = os.getenv("API_LAYER")

            code = operation["operationAmount"]["currency"]["code"]
            r = requests.get(
                "https://api.apilayer.com/exchangerates_data/convert",
                headers={"apikey": api_key},
                params={"from": code, "to": "RUB", "amount": amount},
            )
            return r.json()["result"]
    except KeyError:
        return None
