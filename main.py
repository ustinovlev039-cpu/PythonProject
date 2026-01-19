from src.processing import filter_by_state
from src.processing import sort_by_date
from src.processing_bank import process_bank_search
from src.utils import info_transactions_json
from src.utils_csv_xlsx import info_transactions_csv
from src.utils_csv_xlsx import info_transactions_xlsx
from src.widget import get_data
from src.widget import mask_account_card


def type_file() -> list[dict]:
    """Составление разговора пользователя и его ответы о формате"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")

    while True:
        ans_type = input(
            """
        1. Получить информацию о транзакции из JSON-файла.
        2. Получить информацию о транзакциях из CSV-файла.
        3. Получить информацию о транзакциях из XLSX-файла.
        """
        ).strip()

        if ans_type in ("1", "2", "3"):
            if ans_type.lower().strip() == "1":
                print("Для обработки выбран JSON-файла.")
                return info_transactions_json("data/operations.json")
            elif ans_type.lower().strip() == "2":
                print("Для обработки выбран CSV-файла.")
                return info_transactions_csv("data/transactions.csv")
            else:
                print("Для обработки выбран XLSX-файла.")
                return info_transactions_xlsx("data/transactions_excel.xlsx")

        else:
            print("Не правильный ввод, попробуйте еще раз")


def input_status() -> str:
    """ "Составление разговора пользователя и его ответы о фильтрации"""
    while True:
        status = ("EXECUTED", "CANCELED", "PENDING")
        ans_finding = input(
            """
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
            """
        )
        normalize = ans_finding.upper().strip()
        if normalize in status:
            print(f"Операции отфильтрованы по статусу '{normalize}'")
            return normalize

        else:
            print(
                """
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
            )


def only_digits(text: str | int) -> str:
    """Маску для карты"""
    return "".join(ch for ch in str(text) if ch.isdigit())


def currency_code(op: dict) -> str:
    """Возвращает код валюты транзакции, в разныз форматах"""
    if "currency_code" in op:
        return str(op.get("currency_code", ""))
    try:
        return op["operationAmount"]["currency"]["code"]
    except Exception:
        return ""


def amount(op: dict) -> str:
    """Возвращает сумму операции, в разных форматах"""
    if "amount" in op:
        return str(op.get("amount"))
    try:
        return str(op["operationAmount"]["amount"])
    except Exception:
        return ""


def main() -> None:
    """Составление логики программы"""
    files = type_file()
    result_status = input_status()

    list_operation = filter_by_state(files, result_status)

    ans_sort = input("Отсортировать операции по дате? Да/Нет")
    if ans_sort.lower().strip() == "да":
        ans_sort_type = input("Отсортировать по возрастанию или по убыванию?")

        if ans_sort_type.lower().strip() == "по возрастанию":
            reverse_flag = False
        else:
            reverse_flag = True

        list_operation = sort_by_date(list_operation, reverse_flag)

    transaction = list_operation

    ans_type_transaction = input("Выводить только рублевые транзакции? Да/Нет")
    if ans_type_transaction.lower().strip() == "да":
        transaction = [op for op in list_operation if currency_code(op) == "RUB"]
    else:
        transaction = list_operation

    ans_type_desc_transaction = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    if ans_type_desc_transaction.lower().strip() == "да":
        words = input("Введите слово для поиска в описании: ")
        transaction = process_bank_search(transaction, words)

    if not transaction:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transaction)}\n")

    for op in transaction:
        print(get_data(op.get("date", "")), op.get("description", ""))

        frm = only_digits(op.get("from", ""))
        to = only_digits(op.get("to", ""))

        if frm and to:
            print(mask_account_card(frm), "->", mask_account_card(to))
        elif to:
            print(mask_account_card(to))

        print("Сумма: ", amount(op), currency_code(op))
        print()


if __name__ == "__main__":
    main()
