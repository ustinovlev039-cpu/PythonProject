import os

import requests
from dotenv import load_dotenv

from src.utils import info_transactions_json

load_dotenv()

API_KEY = os.getenv("API_KEY")


def filter_transactions(info: str, transactions: list[dict]) -> list[float] | None:
    """Функция принимает транзакцию и возращает сумму транзакции"""

    paramsa = {"from": "from_cur", "to": "RUB", "amount": "amount"}

    for dict_ in transactions:
        if dict_.get("id") == int(info):
            if dict_["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
                paramsa["from"] = dict_["operationAmount"]["currency"]["code"]
                paramsa["amount"] = dict_["operationAmount"]["amount"]
                return paramsa

            else:
                return dict_["operationAmount"]["amount"]

    return None


def conversation(info_filter: dict) -> float:
    """Функиция отправки API иноформации и перевода в RUB"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_KEY}
    responses = requests.get(url, headers=headers, params=info_filter)
    end_conversation = responses.json()
    return end_conversation["result"]


if __name__ == "__main__":
    test = info_transactions_json()
    test_2 = filter_transactions("41428829", test)
    # print(filter_transactions("441945886", test))
    print(conversation(test_2))
