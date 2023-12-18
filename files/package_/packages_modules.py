# Модуль -> файл с кодом на python

# Пакет -> папка/каталог c модулями, другими пакетами и файлом __init__.py (его наличие помогает интерпритатору python понять что перед ним пакет)

# imoprt <package_name> -> импорт всего содержимого
# from <package_name> import <func_name> -> импорт частичный, конкретную функцию ... 

import random as rand
from math import pi as number_pi
# print(number_pi)
# print(rand.random())


from my_package import hello

# print(hello.test)

from my_package.hello import test as t
# print(t)

# print(globals())

# from file_module import read_file

# print(read_file('my_package/hello.py'))