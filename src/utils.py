import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def info_transactions_json(path: str) -> list[dict]:
    """Читает JSON с транзакциями и возвращает их"""
    try:
        logger.info(f"Выполняем декодирование + запись JSON файла c заданным путем {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError) as error:
        logger.info(f"Произошла ошибки {error}")
        return []


if __name__ == "__main__":
    print(info_transactions_json("data/operations.json"))
