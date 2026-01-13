import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: Union[str, int]) -> str:
    """Функция принимает номер карты и потом кодирует оставляя только начала и конец"""
    result = ""
    new_card = str(card).strip()
    logger.info("Проверка на правильности ввода данных карты")
    if len(new_card) == 16:
        slice_card = new_card[6:13]
        for new in slice_card:
            new = new.replace(new, "*")
            result += new
    else:
        logging.info("Не правильный ввод")
        return "Не правильный ввод карты"

    final_ = new_card[:6] + result + new_card[12:]

    format = f"{final_[:4]} {final_[4:8]} {final_[8:12]}{final_[12:]}"

    logger.info("Вывод маски карты")
    return format


def get_mask_account(numbers: Union[str, int]) -> str:
    """Функция принимает номер счета и потом кодирует оставляя только 4 последние номера"""
    new_numbers = str(numbers).strip()
    logging.info("Проверка на правильности ввода счета")
    if len(new_numbers) == 20:
        slice_numbers = new_numbers[-4:]
        final_2 = "**" + slice_numbers

        logger.info("Вывод маски счета")
        return final_2

    else:

        logger.info("Не правильный ввод данных")
        return "Не правильный ввод счета"
