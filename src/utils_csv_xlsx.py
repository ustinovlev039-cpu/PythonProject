import csv

import pandas as pd


def info_transactions_csv(csv_path: str) -> list[dict]:
    """Читает csv транзакции и возвращает их"""
    with open(csv_path, "r", encoding="utf-8") as table:
        reader = csv.DictReader(table, delimiter=";")
        new_table = []
        for row in reader:
            new_table.append(row)

    return new_table


def info_transactions_xlsx(path_excel: str) -> list[dict]:
    """Читаем excel транзакции и возвращает"""
    df = pd.read_excel(path_excel)
    new_df = df.to_dict(orient="records")

    return new_df


if __name__ == "__main__":
    print(info_transactions_xlsx("data/transactions_excel.xlsx"))
