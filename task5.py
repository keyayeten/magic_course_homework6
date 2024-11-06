# Напиши функцию multi_filter,
# которая принимает список словарей
# и список функций-фильтров.
# Функция должна возвращать только те элементы,
# которые удовлетворяют всем фильтрам.

# P.s. фуннкции можно не только передавать как аргумент,
# но и складывать в список


def multi_filter(filter_list: list, dict_list: list):
    res = dict_list
    for _filter in filter_list:
        res = _filter(res)
    return res


def f_len_more_than_two(lst: list):
    return list(filter(lambda x: len(x) > 2, lst))


def f_all_val_in_dict_are_int(lst: list):
    def check_val(d: dict):
        for i in d.values():
            if type(i) != int:
                return False
        return True
    return list(filter(check_val, lst))


dict_list = [{"1": 1, "2": 2}, {"1": 1, "2": '2', "3": 3}, {"1": 3, "2": 4, "3": 5}, {"1": 1, "2": 2, "3": 3}, ]
filter_list = [f_len_more_than_two, f_all_val_in_dict_are_int]

res = multi_filter(filter_list, dict_list)

print(dict_list)
print(res)
