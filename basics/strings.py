'''
Строки
'''

# Строки -> неизменяемый тип данных, который предназначен для хранения текста (последовательность символов), заключается в кавычки

'''Синтаксис'''
string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# string3 = 'не правильная строка ТАК НЕЛЬЗЯ"
string4 = "Don't" #внутри двлйных кавыче все одинарные - просто символы
string5 = '"Привет"  ' #внутри одинарных кавычек все двойные - просто символы
# print(string5)

string6 = '''
многосточный текст, 'тут' можно 
"ставить" любые кавычки
'''

string7 = """
многосточный текст, 'тут' можно 
"ставить" любые кавычки
"""

# print(string6)

a = ' '

'''множественное присваивание'''
# a, b, c = 'a', 'b', 'c'
# print(b)

# len() -> возвращает кол-во символов в строке

# print(len(a)) # нельзя узнать длину числа (int)
# нужно перевести в строку


'''
============ Экранизация строк ============
'''
# экранированные последовательности
'\n' #-> перенос на новую строку
'\t' #-> табуляцию 
'\\' #-> отображение \
'\'' #-> отображение одинарной кавычки
"\""
'\r' #-> возвращает каретку в начало строки
'\v' #-> перенос на следующую строку со смещение вправо на длину предыдущей строки

# print('hello\nworld') #hello
                        #world

# print('hello\tworld') #hello    world

# print('hello\\')  #hello\

# print('\'hello\'') #'hello'

# print('hell0000000000000\rworld') #world000000000000

# print('hello\vworld') #hello
#                             world


'\a' #гудок встроенного в систему динамика


'''=========== Индексы ==========='''
# индекс -> порядковый номер элемента в строке

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#      ...    -4-3-2 -1

# print('Makers'[0])   'M'
# print('Makers'[1])   'a'
# print('Makers'[-1])  's' # обращаемся к последнему элементу строки
# print('Makers '[-1]) ' '

# срез -> получение/нахождение подстроки 
string = 'hello world'

# print(string[0:5]) #hello
# print(string[6:])  #world
# print(string[0:5][2:4]) #ll
# print(string[:5]) #hello
# print(string[:])  #hello world
# print(string[::2]) #hlowrd

# Срезы по индексу -> нахождение подстроки, начиная от [start:end:step] (step по умолчанию 1)
# [3:] -> начиная с 3 индекса до конца
# [:6] -> начиная с 0 до 6 индекса
# [::], [:], [0::], [::1] -> целая строка
# [::-1] -> перевернуть строку

# print(string[::-1])


'''
============== Форматирование строк =============
'''
# 1. с использованием %
# 2. с использованием метода .format()
# 3. интерполяция строк (f - строки)

# %
# name = input('Введите имя: ')
# result = 'Hello, %s' % name
# print(result)

# .format(переменная)
# name = input('Введите имя: ')
# name1 = input('Введите имя: ')
# result = '{} Hello, {}'.format(name1, name)
# print(result)

# интерполяция строк -> f-строки
# name = input('Введите имя: ')
# name1 = input('Введите имя: ')

# result = f'hello, {name} {name1}'
# print(result)


'''========='''
'конкатенация строк (склеивание строк)'
str1 = 'hello'
str2 = 'world'
# print(str1 + ' ' +str2)

'дублирование строк'
# print(str1*5)

'''============ Методы строк ============'''
# print(dir(str))

# Методы типов данных -> функция, к которой мы обращаетмся через точку

# Медоты на is
str1 = 'string'
str1.isalnum() # -> проверяет состоит ли строка только из цифр и букв
str1.isalpha() # -> проверяет состоит ли строка только из букв
str1.islower() # -> состоит ли строка из символов в нижнем регистре (все буквы маленькие)
str1.isupper() # -> состоит ли строка из символов в верхнем регистре (все буквы большие)
str1.isnumeric() # только из чисел
str1.isspace() # состоит ли строка из неотображаемых символов (пробел, экранированные последовательности)
str1.isdigit() # только из чисел
str1.istitle() # начинается ли строка с заглавной буквы


str1.lower() #переводит все символы в нижний регистр
# a = 'GHIbkfv'
# new_string = a.lower()
# print(new_string, a)

str1.upper() #переводит все символы в верхний регистр
# str_ = 'hello'
# new_str = str_.upper()
# print(new_str, str_)

# str.title() #-> делает первую букву каждого слова заглавной (переводит в верхний регистр), все остальные в нижний регистр

str_ = 'hEllo worlD'
# new_str = str_.title()
# print(new_str)


# str.strip() # убирает пробелы в начале и в конце строки

a = '   hello world '
# b = a.strip()
# print(b)
 
# str.lstrip() -> убирает все пробелы в начале строки
# str.rstrip() -> убирает все пробелы в конце строки

# str.replace(old, new, [count]) -> Меняет old значение на new 
a = 'ha ha ha'
new = a.replace('ha', 'new', 2) #задаем кол-во замен
# print(new)
b = a.replace(' ', '')
# print(b)

# str.split(разделитель) -> делит строку по разделителю и возвращает список (по умолчанию делит по пробелу  )
a = 'hello world'
b = a.split('l')
# print(b)

# str.capitalize() -> переводит в верхний регистр только первый символ в строке, а все остальные в нижний

a = 'hELLo WorlD'
b = a.capitalize()
# print(b)


# str.startswith(string) -> возращает True, если строка начинается на string
string = 'makers bootcamp'
check = string.startswith('makers')
# print(check) 
# print(string)

# str.endswith(string) ->  возвращает True, усли строка заканчивается string
string = 'makers bootcamp'
check = string.endswith('bootcamp')
# print(check) 

# str.count(string)  -> считает кол-во вхождений string в строку
string = 'Python Makers Bootcamp'
element_count = string.count('o') #3
string.count('Makers') #1 
# print(element_count)

# str.index(string, [start], [end]) ->  принимает string и возвращает его индекс в строке. если string нет в строке, вызывает ошибку
str_ = 'Hello python32 o'
result = str_.index('p') # 6
result = str_.index('o', 6, 11) # 10
# print(result)


# str.find(value, [start], [end]) -> аналагочен index, разнича в том, что если value нет в строке возвращает -1
str_ = 'Hello python32 o'
result = str_.find('p') # 6
# result = str_.find('ф') # -1
# print(result)

# if result > 0:
#     print('Такая буква есть в строке')
# elif result < 0:
#     print('Такой буквы нет')

# str.zfill(width) -> делает длину строки не меньше width, но недостующие символы заполняет нулями (если символов нужное кол-во или больше, ничего не происходит)
hello_ = 'hellohellohellohellohello'
new_hello = hello_.zfill(20)
# print(new_hello)

# 'разделитель'.join(iterable) -> соеденяет строку по разделителю, которая находится в iterable 
text = 'Milk, Bread, Water'
splited_text = text.split(', ') #['Milk', 'Bread', 'Water']
# print(splited_text)
joined = '->'.join(splited_text) #'Milk->Bread->Water'
# print(joined)

# test = 'hello everyone'
# test2 = test.capitalize().title().zfill(22).count('o')
# print(test2)




# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# address = "1.1.1.1"
# print(address.replace('.', '[.]'))


"""
1. Даны две переменные num1 со значением 10 и num2 со значением 3.
Поменяйте значения этих переменных между собой. ВАЖНО: Нельзя использовать множественное присваивание.
"""

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1, num2)

# sum_ = num1 + num2 # 13
# num1 = sum_ - num1 # 13 - 10
# num2 = sum_ - num2 # 13 - 3
# print(num1, num2)


# id() -> возвращает id ячецки памяти

# a = 3 + 1
# b = 4
# a = 'hello'
# b = a.lower()
# b = 'hello'

