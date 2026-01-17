import re
from collections import defaultdict

from src.utils import info_transactions_json
from src.utils_csv_xlsx import info_transactions_csv
from src.utils_csv_xlsx import info_transactions_xlsx


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Ищет в банковских операциях нужную заданную строку"""
    result = []
    pattern = re.escape(search)
    for op in data:
        text = op.get("description", "")
        if re.search(pattern, text):
            result.append(op)

    return result

def process_bank_operations(data:list[dict], category:list)->dict:
    """Считает количество заданной операции"""
    count = defaultdict(int)
    for op in data:
        desc = op.get("description", "")
        if desc in category:
            count[desc] += 1

    return count





if __name__ == "__main__":
    test_1 = info_transactions_json("data/operations.json")
    #print(process_bank_search(test_1, "Перевод организации"))
    #categories = ["Перевод организации", "Открытие вклада", "Перевод со счета на счет"]
    print(process_bank_operations(test_1, categories))






