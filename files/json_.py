'''========== JSON ==========='''
# (JavaScript Object Notation) -> единый текстовый формат хранения и передачи данных между ПК, приложениями, сервисами и языками программирования (В основном применяется для передачи данных между сервером и веб-приложением (обмен между фронтом и бэком))

# {
#     "id": 1,
#     "author": "John",
#     "posts": null,
#     "is_famous": false
# } # -> JSON


# Python              JSON
# dict                Object
# list                Array
# tuple               Array
# str                 String
# int                 Number
# float               Number
# True                true
# False               false
# None                null


import json

# Сериализация -> (запись данных в Json) перевод Python объекта в JSON

# Десериализация -> перевод JSON в python 


# dump(python_object, file) ->  метод записывает Python объект в файл в формате json
# dumps(python_object) -> метод записывает python объект в json строку

# load(file) -> считывает файл в формате json и переводит его в python объект
# loads(json_object) -> считывает строку в формате json и переводит ее в python объект


# person = '{"name": "John", "age": 27}'
# result = json.loads(person)
# print(type(result))


# with open('test.json', 'w+') as file:
#     person = '{"name": "John", "age": 27}'
#     file.write(person)
#     file.seek(0)
#     data = json.load(file)
#     print(data.get('name'))


# person = {'name': 'John', 'age': 27, 'is_': False}
# json_ = json.dumps(person)
# print(json_)


# person = {'name': 'John', 'age': 27, 'is_': False}

# with open('test.json', 'w+') as file:
#     json.dump(person, file)
#     file.seek(0)
#     data = file.read()
#     print(data)


'''======== CSV =========='''
# очень схож с excel (Comma Separated Values) -> данные, разделенные запятой

# import csv

# with open('test.csv', 'w+') as file:
#     file.write('this is csv file, csv, json, python')
#     file.write('1, 2, 3, 4')
#     file.write('1, 2, 3, 4')
#     file.write('1, 2, 3, 4')
#     file.seek(0)
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
