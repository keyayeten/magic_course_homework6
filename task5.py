# Напиши функцию multi_filter,
# которая принимает список словарей
# и список функций-фильтров.
# Функция должна возвращать только те элементы,
# которые удовлетворяют всем фильтрам.

# P.s. фуннкции можно не только передавать как аргумент,
# но и складывать в список

dicts = [{'name': 'Leon',  'age': 22}, {'name': 'Olga', 'age': 20}, {'name': 'Peter', 'age': 50}, {'name': 'Pavel', 'age': 55}]
def multi_filter(func: callable, dicts):
    lst = []
    for i in dicts:
        if func(i):
            lst.append(i)
    print(lst)

def filtres(x):
    filter_1 = x['age'] > 25
    filter_2 = len(x['name']) > 4
    n = x['name']
    filter_3 = n.startswith('P')
    return filter_1 and filter_2 and filter_3


multi_filter(filtres, dicts)