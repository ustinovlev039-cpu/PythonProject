from src.processing import filter_by_state
from src.processing import sort_by_date
from src.widget import get_data
from src.widget import mask_account_card
from src.masks import get_mask_card_number
from src.masks import get_mask_account

# date = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
#
# diction = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
#
if __name__ == "__main__":
#     print(filter_by_state(diction))
#     print(sort_by_date(date))
#
#     print(mask_account_card("Счет 73654108430135874305"))
#     print(get_data("2024-03-11T02:26:18.671407"))


      print(mask_account_card("Maestro 1596837868705199"))
      print(mask_account_card("MasterCard 7158300734726758"))
      print(mask_account_card("Visa Platinum 8990922113665229"))



# 1596 83** *****5199
# 7158 30** *****6758
# 8990 92** *****5229


