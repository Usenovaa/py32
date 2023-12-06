'''Тип данных Списки List. 
        Цикл for.
            Тип данных кортеж Tuple'''

'''======== Списки (list) ========'''
# изменяемый, итерируемый, индексируемый, упорядоценный(хранит порядок вставленых элементов),тип данных. Предназначен для хранения любых данных. 
# [] -> литералы, это выражения (константа), которое создает объект


# list_ = [1, 2, 3, 'hello', [True, False, None, [1, 2, 3,4, 5]], {'a': 1}]
# # print(list_[0])
# # print(list_[:5])
# print(list_[4][-1][-1])

# l1 = list_[4]
# l2 = l1[-1]
# print(l1, l2, l2[-1])


'''========== Создание списков ========='''

# 1. -> list(iterable)
# my_list = list('hello') 
# print(my_list)

# 2. -> range([start], stop) возвращает последовательность элементов, если не указать start последовательность начинается с 0, заканчивается не включая stop

# a = range(11)
# print(a)
# list_ = list(a)

# list_ = list(range(1, 11))
# print(list_)

# 3. -> []
# list_ = []
# print(type(list_))

# 4. -> *
# list1 = [1] * 5 
# print(list1)

# итерация -> это прохождение по последовательности
# итерируемый объект -> объект, по которому можно пройтись, который способен возвращать элементы по одному

# str_ = [True, 1, 2, 'hello']

# for i in str_:
#     print(i)
    # print(i + 'makers')
    # print('hello')


'''============ методы списков ============'''
# .append(element) -> добавляет элемент в конец списка
list_ = [1, 2, 3, 4]
list_.append([5, 6, 7, 8])
# print(list_)

# .copy() -> возвращает копию объекта, (поверхносное копирование)
# list_ = ['hello', 1, 2, 3, [1, 2, 3]]
# list_2 = list_.copy()
# list_[-1].append(4)
# list_2.append(5)
# print(list_, list_2)
# print(id(list_), id(list_2))

# .extend(element[iterable]) -> расширяет список добавляя в конец элементы итерируемого объекта
# lis_ = [1, 2, 3]
# lis_.extend([4, 5, 6, 7, 8, 9])
# lis_.extend('hello') 
# print(lis_)

# .insert(index, element) -> добавляет element по указанному индексу
# list_ = [1, 2, 4]
# list_.insert(2, 3)
# list_ = ['hello', 'фиксики', 'makers', 'bootcamp']
# list_.insert(3, 'python')
# print(list_)


# .index(element, [start], [end]) -> возвращает индекс element
# list_ = ['hello', 'makers', 'фиксики', 'makers', 'bootcamp', '', 'makers']
# print(list_.index('makers'))


# .clear() -> очищает список
list_ = [1, 2, 3, 4]
list_.clear()
# print(list_)

# .count(element) -> кол-во вхождений element в список 
list_ = ['hello', 'makers', 'фиксики', 'makers', 'bootcamp', '', 'makers']
# print(list_.count('makers'))

# .pop([index]) -> удаляет элемент из списка по индексу, если индекс не передали, удаляет с конца. Возвращает удаленный элемент
list_ = ['hello', 'makers', 'фиксики', 'makers', 'bootcamp', '', 'makers']
popped = list_.pop()
popped = list_.pop(2)
# print(list_)
# print(popped)

# .reverse() -> переворачивает список
list_ = [1, 2, 6, 4, 5]
list_.reverse() #[5, 4, 6, 2, 1]
# print(list_)

# .remove(element) -> удаляет первый всчтретившийся element из списка
list_ = ['hello', 'makers', 'фиксики', 'makers', 'bootcamp', '', 'makers']
list_.remove('makers')
# print(list_)

# .sort() -> сортирует список, состоящий из элементов одного типа данных
list_ = ['hello', 'makers', 'фиксики', 'makers', 'bootcamp', 'makers', 'a', 'aaaa', 'aaab']
# list_.sort(reverse=True) # reverse=True по убыванию
# print(list_)

# print(len(list_))


'''=========== Цикл for =========='''
# это блок кода, который повторяется несколько раз
# используется, когда нужно повторить код n-ое кол-во раз или пройтись по итерируемому объекту

# for -> цикл, который работает с итерируемыми объектами, заканчивает свою работу, когда дошел до конца (до последнего элемента) итерируемого объекта

# str_ = 'фиксики'

# for a in str_:
#     print(a)

# for i in [1, 2, True, None, 'hello', [1, 2, 3]]:
#     print(i)

# for переменная in итерируемый_объект:
#     тело цикла

# list_ = []

# for i in range(1, 11):
#     list_.append(i)
#     print(list_)

# for i in range(1, 11):
#     if i > 5:
#         print('слишком много чисел')
#     else:
#         print(i)


# for i in range(10):
#     print(i)
#     for j in range(3):
#         print(j)
    
# a = 1,
# print(dir(a))

# print(type(a))

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# ...

# for i in range(1, 10):
#     print(i)

'''
========== Tuple (Кортеж) ===========
'''
# неизменяемый тип данных, индексируемый, итерируемый, упорядоченный. Предназначен для хранения любых данных

# tuple1 = 1, 2, 3
# tuple2 = (1, 2, 3)
# tuple3 = 1,
# tuple4 = ()
# tuple5 = tuple([1, 2, 3, 4])
# tuple6 = tuple('hello')
# print(tuple6)

'''============ Методы tuple ============='''
# .count(element) -> кол-во вхождений element в кортеже
tuple_ = 'hello', 'makers', 'фиксики', 'makers', 'bootcamp', '', 'makers'
# print(tuple_.count('makers'))

# .index(element, [start], [end]) -> возвращает индекс element
tuple_ = 'hello', 'makers', 'фиксики', 'makers', 'bootcamp', '', 'makers'
print(tuple_.index('makers'))

'''========== Инкремент и Дикремент ==========='''
# 
a = 11
# a = a + 1
a += 1 #Инеремент (a = a + 1 ==> a += 1)
print(a, 'сложение')

# 
a = 23
# a = a - 1
a -= 1 #Дикремент (a = a - 1 ==> a -= 1)
print(a, 'вычитание')

a *= 2 # a = a * 2 ==> a *= 2
print(a, 'умножение')

a /=3 # a = a / 3 ==> a /= 3
print(a, 'деление')
