# Напиши функцию aggregate,
# которая принимает список чисел и функцию operation,
# выполняющую определённую операцию над парой чисел,
# а также начальное значение.
# Функция должна применить operation ко всем
# элементам списка и вернуть результат.

# Пример:
# [1, 2, 3, 4, 5]
# Передаваемая функция: функция сложения
# результат : 15

# [1, 2, 3, 4, 5]
# Передаваемая функция: функция умножения
# результат : 120


def aggregate(func: callable, lst: list, start_value):
    res = start_value
    for i in lst:
        res = func(res, i)
    return res


def operation(a, b):
    return a + str(b)


if __name__ == '__main__':
    print(aggregate(operation, [1, 2, 3, 4, 5], ''))
