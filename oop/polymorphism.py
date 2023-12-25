'''
Полиморфизм
методы называются одинаково, но работают по разному
(разное поведение одного и того же метода в разных классах)
'''

'''1. len() -> полиморфная функция'''
# len -> str, list, tuple ...

'''2. + '''
#'str' + 'hello'
# 3 + 7
# [1, 2, 3] + [4, 5, 6]

'''3. .pop()'''
# list.pop()
# dict.pop()
# set.pop()


class Animal:
    def __init__(self, type_, name, age, owner=False):
        self.type_ = type_
        self.name = name
        self.age = age
        self.owner = owner

    def make_sound(self):
        print('makes sound')

class Cat(Animal):
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def make_sound(self):
        print('Gav gav')

cat = Cat('cat', 'Garfild', 5, True)
# cat.make_sound()

dog = Dog('dog', 'Pluto', 7)

# for obj in (dog, cat):
#     obj.make_sound()

'''
Полиморфизм при наследовании - самый распространненый вид полиморфизма в ООП
'''

class Shape:
    '''
        класс для описания формы
    '''
    def __init__(self, name:str) -> None:
        self.name = name.lower()

    def area(self):
        pass

    def fact(self) -> str:
        return 'Фигура в двумерной плоскости'
    
    def __str__(self) -> str:
        return self.name
    

class Square(Shape):

    '''Класс для работы с квадратом'''

    def __init__(self, lenght):
        super().__init__('square')
        self.lenght = lenght

    def area(self) -> int:
        return self.lenght ** 2
    
    def fact(self):
        return 'У квадрата все стороны равны'
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def get_area(self) -> float:
        from math import pi
        return pi * self.radius ** 2
    
objects_list = [Circle(7), Circle(3), Circle(9), Square(5), Square(2), Circle(6), Square(55)]

for i in objects_list:
    print(i)
    print(i.area())
    print(i.fact())
