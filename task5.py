# Напиши функцию multi_filter,
# которая принимает список словарей
# и список функций-фильтров.
# Функция должна возвращать только те элементы,
# которые удовлетворяют всем фильтрам.

# P.s. фуннкции можно не только передавать как аргумент,
# но и складывать в список

def multi_filter(data, filters):
    filtered_data = []
    for i in data:
        flag = True
        for filter in filters:
            if filter(i) == False:
                flag = False
                break
        if flag:
            filtered_data.append(i)
    return filtered_data


def name_filter(human):
    return human["name"].startswith("P")


def age_filter(human):
    return human["age"] > 30


def city_filter(human):
    return human["city"].startswith("San")


filters = [name_filter, age_filter, city_filter]

data = [
    {'name': 'Jack', 'age': 27, 'city': 'San Diego'},
    {'name': 'Wendy', 'age': 22, 'city': 'Phoenix'},
    {'name': 'David', 'age': 37, 'city': 'New York'},
    {'name': 'Grace', 'age': 20, 'city': 'Philadelphia'},
    {'name': 'Xander', 'age': 25, 'city': 'San Antonio'},
    {'name': 'Tina', 'age': 21, 'city': 'Chicago'},
    {'name': 'Eve', 'age': 21, 'city': 'Houston'},
    {'name': 'Paul', 'age': 31, 'city': 'San Antonio'},
    {'name': 'Tina', 'age': 29, 'city': 'New York'},
    {'name': 'Pane', 'age': 23, 'city': 'Phoenix'},
    {'name': 'Victor', 'age': 37, 'city': 'Dallas'},
    {'name': 'Quinn', 'age': 34, 'city': 'Los Angeles'},
    {'name': 'Alice', 'age': 22, 'city': 'Dallas'},
    {'name': 'Charlie', 'age': 38, 'city': 'Dallas'},
    {'name': 'Grace', 'age': 33, 'city': 'Houston'},
    {'name': 'Mona', 'age': 37, 'city': 'San Jose'},
    {'name': 'Mona', 'age': 24, 'city': 'Philadelphia'},
    {'name': 'Rachel', 'age': 20, 'city': 'San Antonio'},
    {'name': 'Paul', 'age': 35, 'city': 'San Diego'},
    {'name': 'Pane', 'age': 32, 'city': 'Houston'},
    {'name': 'Tina', 'age': 40, 'city': 'Dallas'},
    {'name': 'Paul', 'age': 38, 'city': 'San Jose'},
    {'name': 'Nina', 'age': 40, 'city': 'San Antonio'},
    {'name': 'Wendy', 'age': 31, 'city': 'San Antonio'},
    {'name': 'Leo', 'age': 34, 'city': 'Dallas'}
]
print(*multi_filter(data, filters))
