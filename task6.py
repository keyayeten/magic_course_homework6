# Напишите декоратор, который будет сохранять имя, аргументы, результат и время выполнения функции в json файл.
# Файл, должен каждый раз пополняться новыми данными. Пример данных в json:
# [
# {"function_name": "add",
#         "arguments": {
#             "args": [5,10],
#             "kwargs": {}
#         },
#         "result": 15,
#         "execution_time": 0.0 }
# ]
# Подсказка: имя функции можете получить как ```func.__name__```.
import json


def log_result(file_name):
    def wrapper_1(func):
        # чтоб не ломалось изначально в файле долежн лежеть пустой список, но можно допилить
        with open(file_name, "r", encoding='utf-8') as file:
            data = json.load(file)
        def wrapper(s):
            res = {"result": func(s)}
            data.append(res)
            with open(file_name, "w", encoding='utf-8') as file:
                json.dump(data, file)
            return res
        return wrapper
    return wrapper_1



@log_result("log.json")
def my_func(s):
    return 10*s

my_func(5)


#проверим что записалось
with open("log.json", "r", encoding='utf-8') as file:
    data = json.load(file)
    print(data)
