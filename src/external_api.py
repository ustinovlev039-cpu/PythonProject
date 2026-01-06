import os

import requests
from dotenv import load_dotenv

from src.utils import info_transactions_json

load_dotenv()

API_KEY = os.getenv("API_KEY")


def filter_utils(utils_transactions: list[dict], transaction_id: int) -> dict | None:
    """Функция нахождение нужной транзакции"""
    result = (transaction for transaction in utils_transactions if str(transaction.get("id")) == str(transaction_id))
    found = next(result, None)
    return found


def filter_transactions(transaction: dict) -> float:
    """Функция принимает транзакцию и возвращает транзакции или подготавливает к отправки на перевод"""

    info_filter = {"from": "from_cur", "to": "RUB", "amount": "amount"}

    if transaction["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
        info_filter["from"] = transaction["operationAmount"]["currency"]["code"]
        info_filter["amount"] = transaction["operationAmount"]["amount"]
        result = conversation(info_filter)
        return result

    else:
        return float(transaction["operationAmount"]["amount"])


def conversation(info_filter: dict) -> float:
    """Функиция отправки API иноформации и перевода в RUB"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_KEY}
    responses = requests.get(url, headers=headers, params=info_filter)
    end_conversation = responses.json()
    return float(end_conversation["result"])



if __name__ == "__main__":
    test = info_transactions_json("data/operations.json")
    print(filter_utils(test, 441945886))
    #print(filter_transactions(test_2))


