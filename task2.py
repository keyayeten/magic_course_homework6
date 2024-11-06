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

lst = [1, 2, 3, 4, 5]
def aggregate(operation: callable, lst, nach_value):
    b = nach_value
    for i in lst:
        b = operation(i, b)
    return b

def summa(x, y):
    return x + y

def mult(x, y):
    return x * y


print(aggregate(summa, lst, 0))
print(aggregate(mult, lst, 1))