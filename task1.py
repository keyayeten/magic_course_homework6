# Есть в task1.json список товаров. Написать функцию,
# которая принимает функцию, которая трансформирует
# цену в нужную валюту.
# Результат также сохраните в modified_task1.json.
# Считайте, что изначально цены в рублях.
import json


def covert_rub_to_other_valuta(func: callable, data):
    data_price_in_usd = {}
    for i in data:
        price_in_rub = i.get("price")
        name = i.get("name")
        data_price_in_usd[name] = func(price_in_rub).__round__(1)
    return data_price_in_usd


def covert_rub_to_usd(price_in_rub):
    usd_rub = 97.58
    price_in_usd = price_in_rub / usd_rub
    return price_in_usd


with open("task1.json", "r", encoding="utf-8") as file:
    data = json.load(file)

modified_task1 = covert_rub_to_other_valuta(covert_rub_to_usd, data)

with open("modified_task1.json", "w", encoding="utf-8") as file:
    json.dump(modified_task1, file, indent=4)
