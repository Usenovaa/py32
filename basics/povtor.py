'''
бесконечный цикл с for
'''

# a = [1, 2, 3, 4]

# for i in a:
#     print(i)
#     a.append(i)


'''глубокое копирование'''

list_ = [1, 2, [3, 4, 5]]
list_copy = list_.copy()

list_.append(6)
list_[-2].append(6)

# print(list_)
# print(list_copy)
# print(id(list_[-2]))
# print(id(list_copy[-1]))

# import copy

# list_ = [1, 2, [3, 4, 5]]
# list_copy = copy.deepcopy(list_)

# list_.append(6)
# list_[-2].append(6)
# print(list_)
# print(list_copy)

# print(id(list_[-2]))
# print(id(list_copy[-1]))


'''
есть список гостей, вам принять от пользователя имя и проветить, находится ли он в списке гостей
'''

# guests = ['Тима', 'Сэм', 'Роман']
# name = input('Введите имя: ')

# if name in guests:
#     print('Проходите')
# else:
#     print('Вас нет в списке')


# for i in guests:
#     if name != i:
#         continue
#     print('Проходите')
        
# flag = False

# for i in guests:
#     if name == i:
#         flag = True
    
#     if i == guests[-1]:
#         if flag:
#             print('Проходите')
#         else: 
#             print('Вас нет в списке')


# list_ = [2, 5, 1, 7, 4]
# list_2 = [76, 445, 8]
# print(sum(list_+list_2))


# list_ = [2, 5, 1, 7, 4]
# list_ = ('hello', 'Apple', 'ban', 'make', 'tomato')
# print(sorted(list_, key=len))


list_ = [2, 5, 1, 7, 4]
# print(list(reversed(list_)))

# for i in reversed(list_):
#     print(i)



# import random

# from random import randint

# print(randint(1, 1000))
# print(random.randint(1, 100)) # возвращает рандомное число из указанного диапазона
# # print(random.choice(list_)) # возвращает рандомное число из итерируемого объекта
# print(random.random()) # возвращает рандомное число  от 0 до 1 (float)
# print(dir(random))


# dict_ = {1: 'one', 2: 'two', 3: 'three'}

# dict_1 = {}
# for k, v in dict_.items():
#     dict_1.update({v: k})

# print(dict_1)

# Дан словарь dict1. Создайте словарь dict2, с ключами как в словаре dict1, а значениями пусть будут произведение чисел внутренних словарей
# Вывод:
# {'a': 4, 'b': 8, 'c': 27}
dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}

for k, v in dict1.items():
    # print(k, '->', v)
    # values = v.values()
    new_value = 1
    for i in v.values():
        new_value *= i
        
    # dict2[k] = new_value
    dict2.update({k: new_value})

# print(dict2)
    
        
     

