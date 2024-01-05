'''
==== Методы экземпляра, класса, статические ====
'''

#1. методы экзепляра (объекта) (Instance methods)
#2. методы класса (Class methods)
#3. статические методы (Static method) 


# 1. методы экземпляра -> обычные методы, которые первым аргументом принимают self (ссылка на объект). Нужны для работы с объектом и его атрибутами


# class A:
#     var = 10

#     def instance_method(self):
#         print('метод объекта, первы аргументом принимает: ', self)
#         self.var = 9

# obj = A()
# obj.instance_method()
# print(obj.var, A.var)
        

# 2. методы класса -> первым аргументом принимают ссылку на класс cls. Нужны для создания объектов, изменения атрибутов класса. Для их определения используется декоратор classmethod

class A:

    var = 15

    @classmethod
    def class_method(cls):
        print('метод класса, первым аргументом прилетает: ', cls)
        cls.var = 66

    def create(self):
        self.var = 8




# A.class_method()
# obj = A()
# obj.class_method()
# obj.create()
# # print(obj.var, A.var)

# print(A.__dict__)
# print('================')
# print(obj.__dict__)
        

'''
определите класс Car с атрибутом класса color 
1. определите метод экземпляра, который будет менять значения атрибута color
2. определите метод класса для изменения значения атрибута color у класса
'''
# class Car:
#     color = 'red'

#     def instance_method(self, value):
#         self.color = value

    
# obj = Car()
# Car.instance_method(obj, 'white')
# print(Car.color)
# print(obj.color)

class Car:
    color = 'red'

    @classmethod
    def class_method(cls, value):
        cls.color = value 

# print(Car.color  )

# obj = Car()
# obj.class_method('hello')
# print(Car.__dict__)
# Car.instance_method(obj, 'white')
# print(Car.color)
# print(obj.color)


'''
Методы класса меняют состояние всего класса и это отражается на всех объектах от класса. Но они не могут менять состояние конкретного объекта
'''

class Pizza:
    def __init__(self, radius, *ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def cook(self):
        print(f'готовится пицца размером {self.radius * 2} см')
        print(f'ингридиенты: {self.ingredients}')

    @classmethod
    def four_cheeze(cls, r):
        pizza = cls(r, 'млцарелла', 'Чеддер', 'Голладский', 'Дор блю')
        return pizza


# pizza = Pizza(15, 'млцарелла', 'Чеддер', 'Голладский', 'Дор блю')
# pizza1 = Pizza.four_cheeze(20)
# pizza1.cook()
# p = Pizza.four_cheeze(18)
# p.cook()
    

# 3. статические методы - создаются при помощи декоратора staticmethod, не принимают ни объект, ни класс. Просто функции внутри класса, котооая ничего не значет о классе и о объектах, в целом бесполезны, используются для различных вычислений
    

# class B:

#     @staticmethod
#     def pow_x(x):
#         print(pow(x, 2))


# B.pow_x(8)
# b = B()
# b.pow_x(7)

# print(B.__dict__)
# print(b.__dict__)
    

class Cylinder:
    def __init__(self, diametr, hight):
        self.di = diametr
        self.h = hight
        self.area = self.get_area(self.di, self.h)

    @staticmethod
    def get_area(diametr, hight):
        from math import pi

        circle = pi * diametr ** 2 / 4
        side = pi * diametr * hight
        area = circle * 2 + side
        return round(area, 2)
    
# c = Cylinder(5, 8)
# print(c.area)
    

class Iphone14:
    cost = 80000

    def __init__(self, name, money) -> None:
        if money < self.cost:
            raise Exception(f'Вам не хватает {self.cost - money}')
        self.name = name
        self.congrats()

    @classmethod
    def change_cost(cls, new_cost):
        cls.cost = new_cost

    @staticmethod 
    def congrats():
        print('Спасибо за покупку. Поздравляем с обновкой!')

    def hello(self):
        print('fghjkjhgffghj')

# a = Iphone14('Aiana', 4000)   
# a = Iphone14('Aiana', 100000) 
# Iphone14.change_cost(70000)
# print(Iphone14.cost)
# b = Iphone14('Katana', 70000)
# Iphone14.hello(a) 

#метод класса можно вызвать через класс, экзепляр класса (объект)
# Метод объекта (экземпляра класса) можно вызвать через объект и через класс (передав ссылку на объект в скобках) Iphone14.hello(a)
        
# .__class__ -> предоставляет доступ к атрибутам класса, что позволяет менять состояние класса или объекта черезе методы экземпляра класса (объекта)
        

class C:
    def method(self, atr):
        self.atr = atr

# obj = C()
# print(obj.atr)
# C.method(obj, 8)
# obj.method(0)
# print(obj.atr)
# print(obj.__class__) # ссылка на класс
# print(C.__dict__)
# print('==========')
# C.method(obj.__class__, 88)
# print(C.__dict__)
        

# def decor(func):
#     def wrapper():
#         print('оборачиваем функция')
#         func()
#     return wrapper


# @decor
# def f():
#     print('функция')

# # f() # вызывается функция wrapper, которая определенна в декораторе decor
# # f = wrapper # ссылка на функция wrapper сохраняется под именем вашей функции

# a = print
# a('hello -------------------')
