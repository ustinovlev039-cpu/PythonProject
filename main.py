from src.processing import filter_by_state, sort_by_date
from src.processing_bank import process_bank_search
from src.utils_csv_xlsx import info_transactions_xlsx, info_transactions_csv
from src.utils import info_transactions_json
from src.widget import mask_account_card, get_data


def type_file() -> list[dict]:
    """Диалог о выборе формата """
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

        if ans_type == "1":
            print("Для обработки выбран JSON-файл.")
            return info_transactions_json("data/operations.json")
        if ans_type == "2":
            print("Для обработки выбран CSV-файл.")
            return info_transactions_csv("data/transactions.csv")
        if ans_type == "3":
            print("Для обработки выбран XLSX-файл.")
            return info_transactions_xlsx("data/transactions_excel.xlsx")

        print("Не правильный ввод, попробуйте еще раз")


def input_status() -> str:
    """Запрашивает статус для фильтрации и возвращает его в верхнем регистре."""
    allowed = ("EXECUTED", "CANCELED", "PENDING")
    while True:
        ans_finding = input(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
"""
        )
        normalize = ans_finding.upper().strip()
        if normalize in allowed:
            print(f"Операции отфильтрованы по статусу '{normalize}'")
            return normalize

        print(f"Статус операции '{ans_finding.strip()}' недоступен.")


def only_digits(text: str) -> str:
    """Оставляет в строке только цифры."""
    return "".join(ch for ch in str(text) if ch.isdigit())


def currency_code(op: dict) -> str:
    """Возвращает валюту и поддерживает, все выбранные форматы."""
    if "currency_code" in op:
        return str(op.get("currency_code", ""))
    try:
        return op["operationAmount"]["currency"]["code"]
    except Exception:
        return ""


def amount(op: dict) -> str:
    """Возвращает сумму операции во всех выборных форматах."""
    if "amount" in op:  # CSV/XLSX
        return str(op.get("amount"))
    try:  # JSON
        return str(op["operationAmount"]["amount"])
    except Exception:
        return ""


def main() -> None:
    files = type_file()
    result_status = input_status()

    list_operation = filter_by_state(files, result_status)

    ans_sort = input("Отсортировать операции по дате? Да/Нет\n")
    if ans_sort.lower().strip() == "да":
        ans_sort_type = input("Отсортировать по возрастанию или по убыванию?\n")
        reverse_flag = ans_sort_type.lower().strip() != "по возрастанию"
        list_operation = sort_by_date(list_operation, reverse_flag)

    transaction = list_operation

    ans_type_transaction = input("Выводить только рублевые транзакции? Да/Нет\n")
    if ans_type_transaction.lower().strip() == "да":
        transaction = [op for op in transaction if currency_code(op) == "RUB"]

    ans_type_desc_transaction = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
    )
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
