# Напиши функцию agregate,
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

def agregate(nums, start):
    nums.insert(0, start)
    total = nums[0]
    for num in nums[1:]:
        total = operation(total, num, sign)
    return total


def operation(num1, num2, sign):
    if sign == "*":
        return num1 * num2
    elif sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "/":
        return num1 / num2
    elif sign == "**":
        return num1 ** num2
    elif sign == "//":
        return num1 // num2
    elif sign == "%":
        return num1 % num2


nums = [2, 3, 4, 5]
sign = "+"
start = 1
print(f'Результат {sign} чисел {nums} с начальным значением {start}:',
      agregate(nums, start))