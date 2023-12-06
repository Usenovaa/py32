'''
================ Comprehensions ==============
'''
# генерация последовательности в одну строку с использованием цикла (синтаксический сахар)
# основная цель -> упрощение и повышение читаемости кода
# есть три вида list, set, dict comprehension

'''синтаксис'''
# 1. результат for элемент in итерируемый_объект
# 2. результат for элемент in итерируемый_объект if условие(фильтр)


'''============ List comprehension ============'''
# упрощенный подход создания списков
# выигрывает по скорости так как не используется метод append

# list_ = []

# for i in range(1, 11):
#     list_.append(i)

# print(list_)

# list_ = [i for i in range(1, 11)]
# # list_ = list((i for i in range(1, 11)))
# print(list_)


# import time
# # import datetime

# start_time = time.time()
# list_ = []
# for i in range(100):
#     list_.append(i)

# time1 = time.time() - start_time
# print(time1)

# start_time = time.time()
# list_ = [i for i in range(100)]
# time2 = time.time() - start_time
# print(time2)


# print(time1/time2)


# list_ = [i for i in range(1, 11) if i%2==0]
# print(list_)

# list_ = []
# for i in range(1, 11):
#     if i%2==0:
#         list_.append(i)

# list_ = [i for i in range(2, 11, 2)]
# print(list_)


# list_ = [input('Введите данные: ') for i in range(10)]
# print(list_)

# list_ = []
# for i in range(10):
#     a = input('  ')
#     list_.append(a)

'''если в условии есть else, то вся конструкция пишется до for'''

# list_ = []

# for i in range(1, 11):
#     if i%2==0:
#         list_.append('четное')
#     else:
#         list_.append('нечетное')

# list_ = ['четно' if i%2==0 else 'нечетное' for i in range(1, 11)]

# for i in range(1, 11):
#     if i%2==0:
#         list_.append(i)

# print(list_)

ls = [1, 2, 4, 'hello', 'world', 5, 'wooow', 9]
'''
создать новый список состоящий 'str', 'int' 
нужно проверить тип данных элементов списка ls
Вывод: [int, int, int, str, str, int, str, int]
'''

# l = [int if type(element)==int else str for element in ls]
# print(l)


# l = []
# for a in ls:
#     if type(a) == int:
#         l.append('int')
#     else:
#         l.append('str')
# print(a)

# print(l)

# a = 4
# if a == 4:
#     ...
# if type(a) == int:
#     ...

# for i in range(1, 11):
#     if i < 5:
#         if i%2==0:
#             ls.append('четное'):
#             if i :
#                 ...
#         elif i==0:
#             ls.append('ноль')

ls = []
for i in range(1, 21):
    if i > 15:
        if i%2==0:
            ls.append('четное')
        else:
            ls.append('нечетное')

# 1. пройтись по последовательности и получить новый список
ls = [i for i in range(1, 21)]

# 2. отфильтровать элементы
ls = [i for i in range(1, 21) if i > 15]

# 3. поставить условие на записываемые элементы
ls = ['четно' if i%2==0 else 'нечетное' for i in range(1, 21) if i > 15]
# print(ls)



'''========== set comprehension =========='''

# set_ = set()
# for i in range(1, 11):
#     set_.add(i)

# print(set_)

# set_ = {i for i in range(1, 11)}

# set_ = {'четно' if i%2==0 else 'нечетное' for i in range(1, 21) if i > 15}
# print(set_)


'''======== dict comprehension ========'''

# dict_ = {}
# for i in range(1, 11):
#     dict_.update({i: i*2})


# dict_ = {i: i*2 for i in range(1, 11)}
# print(dict_)

# dict_1 = {'one': 1, 'two': 2}

# dict_ = {v: k for k, v in dict_1.items()}
# print(dict_)

# a, b = ('one', 1)
# print(a)
# print(b)

# ls = [1, 2, 3, 1, 1, 3, 2, 2, 2, 2]

# dict_ = {i: ls.count(i) for i in ls}
# print(dict_)

# dict_ = {i: str(i) for i in range(1, 6)}
# print(dict_)

# dct = {1: 2, 2: 3, 3: 4}
# dict_ = {k: str((v**2)) for k, v in dct.items()}
# print(dict_)

ls = [3, 1, 5, 3, 6]
'''создайтк словарь, где ключ -> элемент списка значение -> индекс этого элемента'''
# dict_ = {i: ls.index(i) for i in ls}
# print(dict_)

# 'даны 2 списка, создайте словарь, где ключи - элементы 1 списка, а значения - второго'
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# dict_ = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict_)



'''========== Вложенные comprehensions ==========='''

# словарь, где ключи числа от 1 до 5
# значение список от 1 до ключа

dict_ = {i: list(range(1, i+1)) for i in range(1, 6)}
ls = [i for i in range(1, 6)]
dict_ = {i:[a for a in range(1, i+1)] for i in range(1, 6)}
# {1: [1], 2: [1, 2], 3: [1, 2, 3]...}
# print(dict_)

# 'создайте список, состоящий из 10 списков, в которых строка "hello world" повторяется 5 раз'

# [["hello world", "hello world", "hello world", "hello world", "hello world"], ["hello world", "hello world", "hello world", "hello world", "hello world"]]

# l1 = ['hello world' for i in range(5)]
# list_ = [
#     ['hello world' for i in range(5)] 
#     for i in range(10)
# ]

# list_ = [[['hello world'] * 5] * 10]
# print(list_)


employees = {
    'id1': {
        'first_name': 'Алекс',
        'last_name': 'Иванов',
        'age': 27,
        'job': 'backend developer'
        },
     'id2': {
        'first_name': 'John',
        'last_name': 'Snow',
        'age': 27,
        'job': 'frontend developer'
    }
}

for info in employees.values():

    for k, v in info.items():
        
        if k == 'age':
            
            info[k] = float(v)

# print(employees)

# dict_ = {
#     id_: {k: (int(v) if k=='age' else v) for k, v in info.items()} for id_, info in employees.items() 
# }
# print(dict_)

# from functions import sum_range

# sum_range()

