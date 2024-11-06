# Есть в task1.json список товаров. Написать функцию
# которая принимает функцию которая трансформирует
# цену в нужную валюту.
# Результат также сохраните в modified_task1.json.
# Считайте, что изначально цены в рублях.
import json

lst = []
with open('task1.json', 'r', encoding='utf-8') as file:
    a = json.load(file)
    for i in a:
        lst.append(i)

l = lst
print(l)
def money(func: callable, a):
    new_list = []
    for j in l:
        if func(j):
            new_list.append(j)
    return new_list

def dollars(x):
    new_price = x['price'] * 97.80
    x['price'] = new_price
    return x

dollars_total = money(dollars, lst)
print(dollars_total)

with open('modified_task1.json', 'w', encoding='utf-8') as f:
    json.dump(dollars_total, f,  indent=4)
