'''
Множества set()
'''
# изменяемый, неупорядоченные, итерируемый, неиндексируемый тип данных. Предназначен для хранения уникальных значений. Множества, могут хранить в себе ТОЛЬКО неизменяемые типы данных.


set1 = {1, 3, 6, 2, 4}
set2 = {1, 3, 1, 2, 2, 5, 3}
# set3 = {1, (2, ['hello', True])} #unhashable type: 'list'
set3 = {1, (2, ('hello', True))}
set4 = {False, 0, True, 1} # {False, True}
set5 = {0, False, 1, True} # {0, 1}
set6 = {False, 0, True, 89} # {False, True, 89}
# print(set4)

'''
============ Создание множеств ==============
'''
# 1. set()
set1 = set([1, 2, 3])
set2 = set({'hello': 'world', 'one': 1, 2: 'two'})
set3 = set('hello world')
set4 = set() # -> пустое множество

# 2. -> {}
set4 = {} # пустой словарь
set5 = {1, 'hello', None, ' '}
# print(set5)


'''============ Методы множеств ============='''

'''добавление эл-в'''
# .add(element)
# .update(seq)

my_set = {4, 1, 6}
my_set.add(3)
my_set.add(4) # ничего не произойдет
my_set.add(False)
my_set.add('hello')
# my_set.add({1: 1, 2: 2}) # Ошибка, добавляеть можно только неизменяемые типы данных


# update -> может добавлять сразу несколько элементов (работает как extend в списках)
my_set = {'hello', 4, 88, True}
my_set.update('hello') # разбивает на элементы и добавляет каждый элемент по отдельности
my_set.update([1, 2, 3, 'print', 4])
# my_set.update(True) # можно передавать только итерируемые объекты


'''удаление элементов'''

# clear() -> очищает множество
# remove(element) -> удаляет element из множества, если элемента нет -> ошибка
# discard(element) -> удаляет element из множества, если элемента нет -> ничего не произойдет
# pop() -> удаляет случайный (первый в сформированном порядке) элемент и возвращает его (FIFO)

my_set = {5, 6, 'hello', 1, 8, (4, 6, 7)}
# my_set.clear()
# my_set.remove(False)
# my_set.remove(0) # Ошибка

# my_set.discard('hello')
# my_set.discard(9) # ничего не произошло
# print(my_set)

# popped = my_set.pop()
# my_set.pop()

# print(my_set, popped)

'''методы для работы с двумя множествами'''

# set_a.difference(set_b) -> возвращает элементы, которые есть в set_a, но нет в set_b
# set_a - set_b
set1 = {5, 6, 'hello', 1, 8, (4, 6, 7), 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(set1 - set2) 
# print(set1.difference(set2))
# print(set2.difference(set1))

# set_a.symmetric_difference(set_b) -> возвращает множество уникальные элементы с обоих множеств
# set_a ^ set_b
set1 = {5, 6, 'hello', 1, 8, (4, 6, 7)}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# print(set2.symmetric_difference(set1)) разницы нет

# set_a.intersection(set_b) -> возвращает элемент, схожие в двух множествах
set1 = {5, 6, 'hello', 1, 8, (4, 6, 7)}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(set1 & set2)
# print(set1.intersection(set2))

# set_a.union(set_b) -> соединяет множества set_a и set_b
set1 = {5, 6, 'hello', 1, 8, (4, 6, 7)}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(set1 | set2)
# print(set1.union(set2)) 

'''
д/з
diffence_update
intersection_update
symetric_difference_update

isdisjoint
issubset
issuperset
'''


