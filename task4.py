# На вход программе подается строка в формате:

# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

# Необходимо ее прочитать и с помощью функции map
# преобразовать ее в кортеж tp вида:

# tp = (('ключ_1', 'значение_1'),
#       ('ключ_2', 'значение_2'),
#       ...
#       ('ключ_N', 'значение_N'))
strok = input().split()
print(type(strok))
def my_dict(func: callable, strok):
    d = {}
    for i in strok:
        k, v = func(i.split('=')) #преобраз ключ_1=значение_1
        d[k] = v
    return d

def map_f(x):
    b = tuple(x)
    return b

res = my_dict(map_f, strok)
print(res)
for tp in map_f(res.items()):
    print(tp)