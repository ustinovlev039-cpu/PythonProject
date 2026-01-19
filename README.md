# Banks — виджет банковских операций

Проект предназначен для обработки и отображения информации о банковских операциях клиента.  
Включает функции для маскировки данных, фильтрации операций, сортировки по дате и работы с данными из разных форматов (JSON/CSV/XLSX).

---

## Возможности

- Маскировка номеров карт и счетов
- Фильтрация операций по статусу (`EXECUTED`, `CANCELED`, `PENDING`)
- Сортировка операций по дате
- Форматирование даты в вид `ДД.ММ.ГГГГ`
- Загрузка транзакций из:
  - `data/operations.json`
  - `data/transactions.csv`
  - `data/transactions_excel.xlsx`
- Фильтрация транзакций по слову в `description` (через `re`)
- Подсчёт количества операций по категориям (`description`)
- Генераторные функции для работы с транзакциями
- Декоратор для логирования выполнения функций

---

## Структура проекта (основные модули)

- `src/masks.py` — маскировка номера карты и счета
- `src/widget.py` — универсальная маскировка + форматирование даты
- `src/processing.py` — фильтрация по статусу и сортировка по дате
- `src/processing_bank.py` — поиск по описанию (`re`) и подсчёт по категориям
- `src/utils.py` — чтение JSON
- `src/utils_csv_xlsx.py` — чтение CSV/XLSX (возвращают `list[dict]`)
- `generators.py` — генераторы для фильтрации/описаний/номеров карт
- `decorators.py` — декораторы логирования
- `main.py` — CLI-логика программы (диалог с пользователем)

---

## Установка

1) Клонируйте репозиторий:

```bash
git clone <repo_url>
cd Banks
```

2) Проверьте версию Python:

```bash
python --version
```

Рекомендуемая версия: **Python 3.10+**

3) (Опционально) установите зависимости, если они есть в проекте:

```bash
pip install -r requirements.txt
```

---

## Запуск программы

```bash
python main.py
```

Далее программа:
1) предложит выбрать источник данных (JSON/CSV/XLSX),
2) запросит статус операции,
3) спросит про сортировку по дате,
4) спросит про вывод только RUB,
5) спросит про фильтр по слову в описании,
6) выведет итоговый список или сообщение, если выборка пустая.

---

## Использование модулей

### Маскировка номера карты

```python
from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))
```

Результат:
```
7000 79** **** 6361
```

### Маскировка номера счета

```python
from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))
```

Результат:
```
**4305
```

### Универсальная функция маскирования

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
```

Результат:
```
7000 79** **** 6361
**4305
```

---

### Фильтрация операций по статусу

```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
    {"id": 3, "state": "PENDING"},
]

print(filter_by_state(operations, "EXECUTED"))
```

---

### Сортировка по дате

```python
from src.processing import sort_by_date

sorted_ops = sort_by_date(operations, reverse=True)
```

---

### Форматирование даты

```python
from src.widget import get_data

print(get_data("2024-03-11T02:26:18.671407"))
```

Результат:
```
11.03.2024
```

---

## Модуль `processing_bank`

### Поиск по описанию (`re`)

```python
from src.processing_bank import process_bank_search

result = process_bank_search(operations, "Перевод")
```

Функция вернёт список операций, в `description` которых встречается строка поиска (без учёта регистра).

### Подсчёт операций по категориям

```python
from src.processing_bank import process_bank_operations

categories = ["Перевод", "Открытие вклада"]
stats = process_bank_operations(operations, categories)
print(stats)
```

Пример результата:
```python
{
  "Перевод": 3,
  "Открытие вклада": 1
}
```

---

## Чтение CSV/XLSX

Две функции читают данные и возвращают формат `list[dict]`.

```python
from src.utils_csv_xlsx import info_transactions_csv, info_transactions_xlsx

csv_ops = info_transactions_csv("data/transactions.csv")
xlsx_ops = info_transactions_xlsx("data/transactions_excel.xlsx")
```

Пример результата:
```python
[
  {"id": "1", "state": "EXECUTED", "amount": "100.0", "...": "..."},
  {"id": "2", "state": "CANCELED", "amount": "50.0", "...": "..."},
]
```

---

## Генераторные функции

Генераторы позволяют обрабатывать транзакции последовательно (без загрузки всего в память).

### `filter_by_currency(transactions, value)`

```python
from generators import filter_by_currency

transactions = [
    {"id": 1, "currency": "RUB"},
    {"id": 2, "currency": "USD"},
]

for transaction in filter_by_currency(transactions, "RUB"):
    print(transaction)
```

### `transaction_descriptions(transactions)`

```python
from generators import transaction_descriptions

transactions = [
    {"description": "Оплата услуг"},
    {"description": "Перевод средств"},
]

for description in transaction_descriptions(transactions):
    print(description)
```

### `card_number_generator(start, end)`

```python
from generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)
```

---

## Декораторы

Модуль `decorators` добавляет гибкость проекту: декоратор логирует начало/конец выполнения функции, результат или ошибку.  
Если `filename` задан — пишет в файл, иначе печатает в консоль.

---

## Технологии

- Python 3.10+
- `typing`
- `re`
- `csv` / `openpyxl` (для CSV/XLSX)

---
