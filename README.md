# Виджет банковских операций

Проект предназначен для обработки и отображения информации о банковских операциях клиента.  
Включает функции для маскировки данных, фильтрации операций и форматирования дат.



## Цель проекта

Реализовать набор инструментов для:
- безопасного отображения номеров карт и счетов,
- фильтрации операций по статусу,
- сортировки по дате,
- форматирования даты под удобный для пользователя вид,
- обработки входных данных вне зависимости от формата.

## Установка

1. Скопируйте проект или клонируйте репозиторий:

git clone <репозиторий>

2. Проверьте версию Python

python --version

# Использование 
### Маскировка номера карты 

~~~python
from src.masks import get_mask_card_number

print(get_mask_card_number("7000792289606361"))
~~~

Результат:
~~~
7000 79** **** 6361
~~~

### Маскировка номера счета

~~~python
from src.masks import get_mask_account

print(get_mask_account("73654108430135874305"))
~~~

Результат:
~~~
**4305
~~~

### Универсальная функция

~~~python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
~~~

Результат:
~~~
7000 79** **** 6361
**4305
~~~

### Фильтрация операций

~~~python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"}
]

print(filter_by_state(operations))
~~~

### Сортирвока по дате

~~~python
from src.processing import sort_by_date

sorted_ops = sort_by_date(operations)
~~~

### Форматированние даты

~~~python
from src.widget import get_data

print(get_data("2024-03-11T02:26:18.671407"))
~~~

Результат:
~~~
11.03.2024
~~~

## Реализованные функции
### Маскировка 
- get_mask_card_number()
- get_mask_account()
- mask_account_card()

### Обработка
- filter_by_state()
- sort_by_date()
- get_data()

# Генераторные функции

В проекте реализован модуль с генераторными функциями для обработки транзакций и генерации номеров банковских карт. Генераторы позволяют работать с данными последовательно, не загружая их полностью в память.

## Функциональность

### `filter_by_currency(transactions, value)`

Генератор, который возвращает транзакции с заданной валютой.

**Пример использования:**
```python
from generators import filter_by_currency

transactions = [
    {"id": 1, "currency": "RUB"},
    {"id": 2, "currency": "USD"},
]

for transaction in filter_by_currency(transactions, "RUB"):
    print(transaction)
```

**transaction_descriptions(transactions)**

Генератор, который возвращает описание каждой транзакции.

### Пример использования:

```python
from generators import transaction_descriptions

transactions = [
    {"description": "Оплата услуг"},
    {"description": "Перевод средств"},
]

for description in transaction_descriptions(transactions):
    print(description)
```

**card_number_generator(start, end)**

Генератор, который формирует номера банковских карт в формате
XXXX XXXX XXXX XXXX в заданном диапазоне.

### Пример использования:

```python
from generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)
```

### Добавление модуля decorators:

Модуль ,который дает проект гибкость. Декоратор логирует начало/конец выполнения функции, результат или ошибку.
И если filename задан — пишет в файл, иначе печатает в консоль.

### Добавление модуля utills_csv_xlsx
Две функции читают файлы в формате csv and excele и каждый выводит формат list[dict]. 

Пример простого вывода:
~~~python
[
  {"id": "1", "state": "EXECUTED", "amount": "100.0", ...},
  {"id": "2", "state": "CANCELED", "amount": "50.0", ...},
]
~~~

### Используемые технологии

- Python 3.10+

- typing




