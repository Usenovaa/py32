# Оброз типов данных
'''
                Типы данных в Питоне
'''
# 1. NoneType -> none (Пустота)
# 2. Boolean -> bool() (Правда или ложь Пример: True/False)
# 3. Числовые типы данных:
    # a. integer -> int() (Пример: 8, 10, 15) целые числа
    # b. float() -> число с плавающей точкой (Пример: 1.45, 7.9)
    # c. complex() -> Комплексные числа (Пример: 3 + 5i/j)
# 4. Списковые типы данных:
    # a. list() -> списки (Пример: [1, 4.3, 'hello', [1, 2], True])
    # b. tuple() -> кортеж (Пример: (1, 2, True, none))
# 5. string -> str() (Пример: '', "не пустая строка")
# 6. set() -> множества (Пример: {1, 2, 3, none})
# 7. frozenset() -> замороженное множество 
# 8. dict() -> словарь (Пример: {'one': 1, 2: 'two'})

# Immutable(Неизменяемые типы данных)
    # 1. NoneType
    # 2. Boolean 
    # 3. str()
    # 4. tuple()
    # 5. int()
    # 6. float()
    # 7. complex()
    # 8.frozenset()

# Mutable (Изменяемые)
    # 1. list()
    # 2. set()
    # 3. dict()


'''============= Переменные ============='''
# это ссылка на ячейку памяти в которой хранится какая-то информация, предназначены для хранения данных

# Правильно

age = 33
age2 = 9
age_2 = 77
_age = 6
hello_world = 'snake case'
helloWorld = 'camel case'
age3 = 9
age8 = 9

# Не правильно
# 2age = 'wrong'
# age% = 'worng'
# Age = 8
# int()
# int = 8 будет работать, но нельзя использовать зарезервированные слова

'''
имя переменной может состоять только из букв, чисел и _
'''

a = 5
b = 7
# c = a + b 
# print(c)

# print() ->  функция стандортного вывода данных
# input(шаблон/подсказка) -> функция стандартного ввода данных (всегда возвращает строку (str))
# type(переменная или объект) -> возвращает тип данных объекта

# name = input('Введите свое имя: ')
# print('Всем привет',name, a,  a, b)
# age =
# last_name =
# city = 

# print(type(name))
# int() -> конфертирует в число int

# number1 = int(input('Введите первое число: '))
# # будет ошибка, если пользователь передаст не числовое значение


# number2 = 3
# # int('4') -> 4
# print(number1 + number2)


'''========== Операции над числами =========='''

# сложение +

# num1 = 88
# num2 = 5
# num3 = num1 + num2
# print(num3)

# # вычитание -
# print(num1 - num2)

# # умножение *
# result = 7 * 5
# print(result)

# # деление /
# print(result / num2) -> float 7.0


# // -> целочисленное деление -> 7
a = 66
b = 8
c = 3

# print(a // b)

# ** -> возведение в степень

a = 7
b = 3
# print(a ** b)


# % -> получение остатка от деления
a = 9
b = 5
# print(a % b)

# pow() 
# 1. возведение в степень
# 2. возвращает остаток от деления возведенного в степень числа на 3е число

# print(pow(3, 2))

# print(pow(9, 2, 4))
# a = 9 ** 2 # 81
# a % 4

# abs() -> получение модуля от числа (отрицательное число делает положительным)
# print(abs(-5)) -> |-5| = 5
# print(abs(10))

# divmod() -> принимает два числа и возвращает два числа, где первое число -> это результат целочисленного деления, а второе число -> остаток от деления

# print(divmod(23, 4))
# (23 // 4) => 5
# 23 % 4 => 3

# round() -> округляет число
# print(round(23.984567896)) #24
# print(round(23.984567896, 3)) #23.985

# dir() -> возвращает методы и функции объекта
import math  
# pi
# sqrt()
# print(dir(math))

# from math import pi
# print(pi)

# print(math.sqrt(25))