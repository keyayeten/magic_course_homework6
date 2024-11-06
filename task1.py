# Есть в task1.json список товаров. Написать функцию
# которая принимает функцию которая трансформирует
# цену в нужную валюту.
# Результат также сохраните в modified_task1.json.
# Считайте, что изначально цены в рублях.
import json


def get_data(file_name) -> dict:
    with open(file_name, "r", encoding='utf-8') as file:
        return json.load(file)


def write_data(data, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        return json.dump(data, file)


def convert_ru_to_usd(price: float):
    ru_to_usd = 0.01
    return (price * ru_to_usd)


def main_func(func):
    data = get_data("task1.json")
    for item in data:
        item['price'] = func(item.get('price'))
    write_data(data, 'modified_task1.json')


main_func(convert_ru_to_usd)
print(get_data("modified_task1.json"))
