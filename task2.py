# Напиши функцию aggregate,
# которая принимает список чисел и функцию operation,
# выполняющую определённую операцию над парой чисел,
# а также начальное значение.
# Функция должна применить operation ко всем
# элементам списка и вернуть результат.

def aggregate(func: callable, list1: list) -> int:
    count = list1[0]
    for i in list1[1:]:
        count = func(count, i)
    return count


def operation_sum(x, y):
    x += y
    return x


def operation_ymnozh(x, y):
    x *= y
    return x


_lst = [1, 2, 3, 4, 5]

print(aggregate(operation_sum, _lst))
print(aggregate(operation_ymnozh, _lst))

# Пример:
# [1, 2, 3, 4, 5]
# Передаваемая функция: функция сложения
# результат : 15

# [1, 2, 3, 4, 5]
# Передаваемая функция: функция умножения
# результат : 120
