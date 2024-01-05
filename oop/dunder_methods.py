'''
Магические методы. (dunder_methods)
'''
# Супер методы
# Служебные методы

# методы  у которых 2 нижних подчеркивания в начале и в конце.
# Срабатывают автоматически (без вызова), при выполнении каких-то операции или вызова функция
# Нужны для того, что объекты могли работать с некоторыми операторами или встроенными функциями

# __init__, __str__


# __new__() -> конструктор, отвечает за создание объекта
# __init__() -> инициализатор, создает атрибуты объекта (вызывается сразу после создания объекта)
# __del__() -> деструктор, отвечает за удаление объекта (срабатывает, когда мы заканчиваем работу с объектом, всегда вызывается когда завершается работа интерпретатора)


from typing import Any


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('инициализация объекта: ', self)
    
    def __del__(self):
        print('удаление экземпляра: ', self)


# a = Point(4, 6)
        

class Point:

    #args, kwargs -> нужно передавать всегда (x, y при создании объекта попадают сюда)
    def __new__(cls, *args, **kwargs):
        print('вызов методв __new__')
        '''должен возвращать ссылку нового объекта. вызовом родительского метода создается объект и возвращается адрес созданного объекта'''      
        return super().__new__(cls) 

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        print('инициализация объекта: ', self)

    
# a = Point(6, 9)
# print(a)
        

class Word(str):
    def __new__(cls, *args):
        string = args[0].replace(' ', '')
        print(args)
        return str.__new__(cls, string)
    

# word1 = Word('adsfghj dcfvgdf asdv')
# word2 = Word('   a b  c   d')
# print(word2)
        

class User:
    def __new__(cls, name, age):
        if age >= 18:
            return object.__new__(cls)
        raise Exception('Вы слишком молоды') 

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        print('init')

    def __del__(self):
        print('del')
        del self

    def __str__(self):
        print('str')
        return self.name
        
    def __repr__(self): # машинноепредставление объекта (почти тоже самом что __str__, но не обязательно должно быть понятно человеку)
        print('repr')
        return self.name

# a = User('test', 19)
# print(a)


# import datetime

# time_ = repr(datetime.date.today())

# print(time_)


class Number(int):
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        '''
        вызывается оператором +
        '''
        # return super().__add__(other)
        return f'Это сложение и резутьтат: {self.value + other}'
    
    def __sub__(self, other):
        return f'Это вычитание и резутьтат: {self.value - other}'
    
    def __mul__(self, other):
        return f'Это умножение и резутьтат: {self.value * other}'
    
    def __truediv__(self, other: int) -> float:
        return f'Это деление и резутьтат: {self.value / other}'
    
    def __floordiv__(self, other):
        return f'Это // и резутьтат: {self.value // other}'
    
    def __mod__(self, other):
        return f'Это % и резутьтат: {self.value % other}'
        
    def __pow__(self, other):
        return f'Это ** и резутьтат: {self.value ** other}'
        
    
number = Number(6)

# print(number + 9)
# print(number - 4)
# print(number * 2)
# print(number / 3)
# print(number // 4)
# print(number % 4)
# print(number ** 3)
# print(pow(number, 2))
    
'''
====== Магические методы сравнения ======
'''
# == -> __eq__(self, other) #equal -> равно
# != -> __ne__(self, other) not equal -> не равно
#  > -> __gt__()self, other) greater than -> больше
# < -> __lt__() less than -> меньше
# >= -> __ge__() 
# <= -> __le__()


# __invert__(self) -> переворачивает итерируемый объект

class Base:
    def __init__(self, string):
        self.string = string

    def __invert__(self):
        print('invert')
        return self.string[::-1]
    
    def __str__(self):
        return self.string
    

# a = Base('hello')
# print(a)
# res = ~a
# print(res)
    

# __hash__() -> Хешируем данные
# hash()
    
# print(hash('string1'))
    

# __getattribute__(self, item(атрибут, к которомы мы обращается)) -> вызывается автоматически при обращении к существующему атрибуту
    

# string = 'hello'
# print(string.lower)
# print(string.__getattribute__('lower'))
    
# __getattr__(self, attr) -> автоматически вызывается при обращении к несуществующему атрибуту экземпляра (работает только когда атрибут не найден)
# __setattr__(self, attr, value) -> вызывается при присвоении атрибуту определенного значения
# __delattr__(self, attr) -> вызывается автоматически при удалении атрибута у экземпляра
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, name: str) -> Any:
        print('getattribute')
        # return super().__getattribute__(name)
        if name == 'x':
            raise Exception('Доступ запрещен')
        else:
            return super().__getattribute__(name)
    
    def __setattr__(self, name, value) -> None:
        print('setattr')
        # super().__setattr__(name, value)\
        if name == 'z':
            raise Exception('Недопустимое имя атрибута')
        else:
            return super().__setattr__(name, value)


    def __getattr__(self, name):
        print('getattr')
        
    def __delattr__(self, name: str) -> None:
        print('delattr')
        super().__delattr__(name)


# a = Point(4, 3) #2 setattr
# a.x #getattribute
# a.z #getattribute -> getattr
# del a.x #dalattr
# a.z = 7


# __getitem__(self, key) -> когда обращаемся в квадратных скобках [] (по ключу, по индексу, срез)

# __setitem__(self, key, value) -> создание новой пары по ключу или изменения элемента по индексу

# __delitem__(self, key) -> удаляет


class A:
    def __getitem__(self, key):
        print('getitem')
    
    def __setitem__(self, key, value):
        print('setitem')

    def __delitem__(self, key):
        print('delitem')

a = A()
# a.item = [1, 2, 3, 4]
# a[1]
# a[0] = 9
# del a[3]