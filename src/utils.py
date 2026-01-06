import json


def info_transactions_json(path: str) -> list[dict]:
    """Читает JSON с транзакциями и возвращает их"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


if __name__ == "__main__":
    print(info_transactions_json("data/operations.json"))



