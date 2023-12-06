'''Файлы. Работа с файлами. JSON, модули и пакетыю, сsv'''


# open('путь до файла', 'режим') -> функция, которая позволяет открывать файлы и работать с ними

# file = open('/home/hello/Desktop/p32/basics/dict.py') -> абсолютный путь
# file = open('test.txt') -> относительный путь

'''======== Режимы ========='''
# 1. 'r' (read) -> открывает файл в режиме чтения. Это режим по умолчанию. если файл не существует, ошибка
# file = open('test.txt')
# data = file.read()
# # print(data)
# print(file)

# 2. 'w' (write) -> открывает файл в режиме записи. если передать не существующий файл, то создаст его. Перезаписывает все содержимое файла
# file = open('test2.txt', 'w') -> создас пустой файл test2.txt

# file = open('test.txt', 'w')
# file.write('helloooooooooooooooo')

# 3. 'a' (append) -> открывает файл для добавления. Все новое добавляется в конец. (Если такого файла нет, то создаст его)
# file = open('test3.txt', 'a')
# file.write('привет')

# 4. 'x' (exclusive) -> создает уникальные файлы. Будет ошибка, если передать существующий файл

# file = open('test55.txt', 'x')
# file.write('12345')

# 5. 't' (text) -> Открывает файл в текстовов виде. Режим по умолчанию

# 6. 'b' (binary) -> открывает файл в бинарном виде
# 'rb' -> чтение в бинарном виде
# 'wb' -> запись в бинарном виде
# 'ab' -> дозапись в бинарном виде

# file = open('test.txt', 'rb')
# data = file.read()
# print(data)

# 7. '+' -> открывает файл как в режиме чтения, так и записи
'r+'
'w+'

'''====== Методы режимов ======'''
# 'r'
# 1. read() -> если не передать аргумент, читает весь файл -> str
# 2. readline() -> считывает отдну строку за раз -> str
# 3. readlines() -> считывает все строки и сохраняет их в списке -> list


# file = open('test.txt')
# # print(file.tell())
# data = file.read()
# # print(file.tell())
# # file.seek(4)
# data2 = file.read()
# print(data2)
# file.close()


'''методы работающие со всеми режимами'''
# file.tell() -> возвращает индекс где находится указатель
# file.seek(index) -> перемещаем указатель на указанный индекс 


# f = open('test.txt')
# str_ = f.readline() # считывает всю строку
# str_2 = f.readline(4) # считывает только указанное кол-во символов
# print(str_, str_2)
# f.close()


# f = open('test.txt')
# list_ = f.readlines(30) # возращает список состоящий из строк, эле-ты которой были прочтены (хотя бы один элемент)
# # list_ = f.readlines()
# print(list_)
# f.close()


# f = open('test.txt')
# for line in f:
#     print(line)
# f.close()


'''==== Методы режима w ===='''
# 1. write('string') -> записывает строку в файл
# 2. writelines(list) 

# f = open('test2.txt', 'w')
# # f.write('hello\nworld')
# f.writelines(['hello', 'привет', 'world'])
# f.writelines(('g', 'o', 'o', 'd'))
# f.writelines({'a': 1})
# f.close()


# a = ['hello', 'world', 'good', 'python']

# f = open('test2.txt', 'w')
# for i in a:
#     i += '\n'
#     f.write(i)

# f.close()


# try:
#     f = open('test2.txt')
#     data = f.read()
#     print(data)
# finally:
#     f.close()
#     print(f.closed)

'''контекстный менеджер. Отркывает файл и при любом раскладе файл будет закрыт'''

# with open('test2.txt') as file:
#     print(file.read())

# with open('test2.txt', 'r') as file:
#     file.write('lj;dlfvb f')
#     data = file.read()
    # print(data)\
    

# with open('test2.txt', 'w+') as file:
#     file.write('lj;dlfvb f')
#     file.seek(0)
#     data = file.read()
#     print(data)


# with open('test2.txt', 'a') as file:
#     file.write('\nhello')
    

with open('test2.txt', 'a+') as file:
    file.write('\nhello')
    file.seek(0)
    print(file.read())

