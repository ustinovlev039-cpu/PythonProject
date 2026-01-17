from src.processing import filter_by_state
from src.processing_bank import process_bank_search
from src.external_api import filter_utils
from src.external_api import filter_transactions
from src.external_api import conversation
from src.utils_csv_xlsx import info_transactions_xlsx
from src.utils_csv_xlsx import info_transactions_csv
from src.utils import info_transactions_json


def type_file():
    """Составление разговора пользователя и его ответы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    ans_type = input("""
    1. Получить информацию о транзакции из JSON-файла.
    2. Получить информацию о транзакциях из CSV-файла.
    3. Получить информацию о транзакциях из XLSX-файла.
    """)

    if ans_type.lower().strip() == "1":
        print("Для обработки выбран JSON-файла.")
        return info_transactions_json("data/operations.json")
    elif ans_type.lower().strip() == "2":
        print("Для обработки выбран CSV-файла.")
        return info_transactions_csv("data/transactions.csv")
    else:
        print("Для обработки выбран XLSX-файла.")
        return info_transactions_xlsx("data/transactions.csv")


def input_status():
    while True:
        status = ("EXECUTED", "CANCELED", "PENDING")
        ans_finding = input("""
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
            """)
        if ans_finding.upper().strip() in status:
            if ans_finding.lower().strip() == "executed":
                print("Операции отфильтрованы по статусу 'EXECUTED'")
                filter_by_state(type_file())
                break

            elif ans_finding.lower().strip() == "canceled":
                print("Операции отфильтрованы по статусу 'CANCELED'")
                filter_by_state(type_file())
                break

            else:
                print("Операции отфильтрованы по статусу 'PENDING'")
                filter_by_state(type_file())
                break

        else:
            print("""
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """)


    ans_sort = input("Отсортировать операции по дате? Да/Нет")

    ans_sort_type = input("Отсортировать по возрастанию или по убыванию?")
    if ans_sort_type.lower().strip() == "по возрастанию":
        ans_sort_type = False
    else:
        ans_sort_type = True

    ans_type_transaction = input("Выводить только рублевые транзакции? Да/Нет")

    ans_type_desc_transaction = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    ans_write_transaction = input("Распечатываю итоговый список транзакций...")








starting_progrem()




