import json


def info_transactions_json() -> list[dict]:
    """Читает JSON с транзакциями и возвращает их"""
    try:
        with open("data/operations.json") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    print(info_transactions_json())
