# Есть в task1.json список товаров. Написать функцию
# которая принимает функцию которая трансформирует
# цену в нужную валюту.
# Результат также сохраните в modified_task1.json.
# Считайте, что изначально цены в рублях.

import json


def calculation_func(price, rate_rub, rate_doll):
    exchange_rate = rate_rub / rate_doll
    return price * exchange_rate


def new_price(file_name, new_file_name, calculation_func):
    with open(file_name, "r", encoding="utf-8") as file:
        prices = json.load(file)

    for i in prices:
        i["price"] = calculation_func(i["price"], rate_rub, rate_doll)

    with open(new_file_name, "w", encoding="utf-8") as file:
        json.dump(prices, file, indent=4)


file_name = "task1.json"
new_file_name = "modified_task1.json"
rate_rub = 1
rate_doll = 97.21
new_price(file_name, new_file_name, calculation_func)