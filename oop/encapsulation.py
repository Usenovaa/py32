'''
Основные принципы ООП: Инкапсуляция 
'''

# 1.Объединение методов и свойств в одну капсулу (класс)

# 2. Сокрытие/Ошраничение доступа к методам и атрибутам (сокрытие данных от внешнего воздействия)


# Инкапсуляция как связь
class Phone:
    number = '+996747485775'

    def print_number(self):
        print(f'My number: {self.number}')

# my_phone = Phone()
# my_phone.print_number()
# связали поведение объекта с его данными


# Инкапсуляция как управление доступом

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# pt = Point(4, 7)
# pt.x = 'hello'
        
'''
3 модификатора доступа
1. public -> публичный (название без нижнего подчеркивания в начале) -> данные доступны всем (x, y, name, number, number_ ...)
2. _protected -> защищенный (с одним нижним подчеркиванием) -> данные доступны внутри класса и в дочерних -> _number, _x, _y ...
3. __private -> приватный (с двумя нижними подчеркиваниями) -> служит для обращения только внутри класса (Данные доступны только классу которому они принадлежат) -> __number. __x, __y
'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# pt = Point(4, 7)
# pt.x = 'hello'
# print(pt.x, pt.y)
        

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

# pt = Point(4, 7)
# pt._x = 'hello' # на уровне договоренности
# print(pt._x, pt._y) # атрибуты и методы с одним нижним подчеркиванием в начале стараемся не использовать вне класса
        


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

        
# pt = Point(4, 99)
# print(pt.__dict__)
# pt.__x = 'hello'
# print(pt.__x, pt.__y) # ошибка
# pt._Point__x = 'hello'
# print(pt._Point__x, pt._Point__y) # но так обращаться не стоит
        
'''!!!!!!!! 
Инкапсуляция -> работает на уровне соглашения (договоренности), надеясь что люди не будут их вызывать вне класса (защищенные и приватные) !!!!!!!!!'''


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x_y(self): #getter
        return self._x, self._y
    
    def set_x_y(self, x, y): #setter
        if type(x) in (int, float) and type(y) in (int, float):
            self._x = x
            self._y = y
        else:
            raise Exception('координаты должны были числами')
    
pt = Point(4, 5)
# pt.set_x_y(8.9, 'hello')
# print(pt.get_x_y())


# getter & setter
'''
методы для работы с защищенными и приватными атрибутами. Используются: getter -> для получения значения, setter -> для установки нового значения
Добавляют логику проверкипри задании и получении данных
Чтобы избежать прямого обращения к защищенным и приватным атрибутам
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 132

    def get_age(self):
        return self.__age
    
    def set_age(self, new_age=0):
        if new_age != 0 :
            if 0 < new_age < 135:
                self.__age = new_age
            else:
                raise Exception('Invalid age')
        else:
            self._add_age()
        
    def _add_age(self):
        if self.__age < 135:
            self.__age += 1
        
# a = Person('Malik')
# a.set_age()
# a.set_age()
# a.set_age()
# a.set_age()
# print(a.get_age())
    

'''
для удобства, в инкапсуляции сужечтвуют декораторы для getterа и setterа 
декоратор property  -> используется для обращения к методу как к атрибуту (getter)
Пример: 
obj.age -> getter

декоратор "название, которое предоставляет property".setter -> для settera
чтобы к методу settor обращаться как к атрибуту
Пример:
obj.age = 67 -> setter


'''


class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 132 

    @property #getter
    def age(self):
        return self.__age
    
    # @age.getter
    # def age(self):
    #     return self.__age
    
    @age.setter
    def age(self, new_age=0):
        if new_age != 0 :
            if 0 < new_age < 135:
                self.__age = new_age
            else:
                raise Exception('Invalid age')
        else:
            self._add_age()

    
    @age.deleter
    def age(self):
        del self.__age
        
    def _add_age(self):
        if self.__age < 135:
            self.__age += 1
        
# p = Person('Aliza')
# p.age = 136
# print(p.age)
# del p.age
# print(p.age)
# del p.age


# la = [1, 2, 3]
# del la[0]
# print(la)
            
class Car:
    def __init__(self, model: str) -> None:
        self.__model = model

    def set_model(self, model):
        print('setter')
        self.__model = model

    def get_model(self):
        print('getter')
        return self.__model
        
    model = property(
        # lambda self: self.__model,
        get_model,
        set_model
        )

    # @property
    # def model(self):
    #     return self.__model

# car = Car('hbh')
# print(car.model)
# car.model = 7
# print(car.model)
        

class Circle:
    def __init__(self, diametr):
        self.__diametr = diametr

    # @property
    def get_d(self):
        return self.__diametr
    
    # @d.setter
    def set_d(self, diametr):
        if not isinstance(diametr, (int, float)):
            raise Exception('Invalid value')
        self.__diametr = diametr

    def del_d(self):
        print('deletter')
        del self.__diametr

    diametr = property(get_d, set_d, del_d)

# c = Circle(77)
# c.diametr = 9
# print(c.diametr)
# del c.diametr


# c = Circle(77)
# c.d = 9
# print(c.d)

# c = Circle(77)
# c.set_d(6.9)
# print(c.get_d())
"""
1.Создайте класс PrivateProject. Внутри этого класса есть атрибуты класса: github_link и developers.
В github_link хранится ссылка на проект (любая), а в developers хранится список с юзернеймами, у которых есть доступ к этой ссылке (атрибуту github_link).
Создайте объект класса PrivateProject, при создании необходимо передать в качестве аргумента username.
Далее, попытайтесь через созданный объект класса получить атрибут github_link. При этом, если данный username есть в списке developers, ему открыт доступ к ссылке.
В противном случае выводится сообщение: Forbidden. Список developers должен быть скрыт.
"""

    
