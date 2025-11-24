from typing import Union

def get_mask_card_number(card: Union[str, int] ) -> str:
    '''Функция принимает номер карты и потом кодирует оставляя только начала и конец'''
    result = ""
    new_card = str(card)
    slice_card = new_card[6:13]
    for new in slice_card:
        new = new.replace(new, "*")
        result += new

    final_ = new_card[:6] + result + new_card[12:]

    format = f"{final_[:4]} {final_[4:8]} {final_[8:12]}{final_[12:]}"

    return format


card = 7000792289606361
get_mask_card_number(card)


def get_mask_account(numbers: Union[str, int]) -> str:
    '''Функция принимает номеер счета и потом кодирует оставляя только 4 полседнее номера'''
    new_numbers = str(numbers)
    slice_numbers = new_numbers[-4:]

    final_2 = "**" + slice_numbers

    return final_2


numbers = 73654108430135874305
get_mask_account(numbers)
