'''
Введение в ООП. 
'''
# a = 5

# class Person:
#     arms = 2
#     legs = 2

#     def walking(self):
#         print('Я иду') 


# person1 = Person()
# person1.walking()  
# print(person1.arms)

# int('9')


'''
ООП -> объектно ориентированное программирование, парадигма (способ написания кода, набор правил написания) программирования в которой все основывается на классах и объектах
'''

'''
класса -> это описание того, какими свойствами (переменными) и поведением (методы) будет обладать объект (Чертеж)
'''

'''
Объект -> это экземпляр от класса с собственным поведением и состоянием свойст 
'''


'''Синтаксис'''

# class A: # объявление класса
#     string = '' # создали переменную класса (атрибут класса)

#     def first_method(self): # объявили метод, self - ссылка на объект
#         print('первый метод')

# a = A() # создание объекта
# b = A()
# # print(a)
# A.first_method(a) == a.first_method()

# a.string = 'hello' # изменили значение атрибута "string" у объекта "a"
# print(b.string)




class Person: # объявление класса
    arms = 2 # создали переменную класса (атрибут класса)
    legs = 2

    def __init__(self, naem: str, age: int, last_name: str):
        '''
        функция, которая вызывается когда мы создаем объект от класса
        здесь определяются (создаются) переменные (атрибуты) объекта (экземпляра класса)
        Отвечает за инициализацию объекта
        '''
        self.name = naem
        self.age = age
        self.last_name = last_name

    def add_age(self):
        self.age += 1

    def __str__(self):
        '''
        функция, которая примает только ссылку на объект (self) и возвращает строку
        строкое представление объекта, вызывается когда пытаемся рапечатать объект (чтобы при printе выводилось что-то конкретное)
        '''
        return self.last_name


# john = Person('John', 27, 'Snow')
# sam = Person('Sam', 57, 'Brown')
# print(john, sam)

# print(dir(Person))
# print('===============')
# print(dir(john))
# print(Person.__dict__)
# print(john.__dict__)




'''
===== Атрибуты класса (переменные внутри класса) =====
'''
# атрибуты на уровне класса.
# данные в этихи атрибутах будут одинаковыми у всех объектов (константа, статические) предполагается, что они не будут меняться в будущем 
# к ним можно обращаться как через объект, так и через класс
# A.string
# a = A()
# a.string


'''====== Атрибуты объекта (переменные объекта) ======'''
# атрибуты экземпляра класса, атрибуты на уровне объекта. атрибуты уровня инстанции класса
# атрибуты, которые есть у объекта, но возможно их нет у класса
# определяются в методе __init__(self) и к ним незьзя обратиться через класс 

class A:
    s = 'ggg'
    

    def __init__(self, a):
        self.a = a

    # def test(self, n):
    #     self.n = n

# print(A.s)
# obj = A(4)
# print(A.a) # будет ошибка, так как у класса A нет атрибута "a"
# print(obj.a)
        

'''
==== Методы класса =====
'''
# создаются с использованием декоратора, работают с классом

'''
====== Методы объекта ======
'''
# функции, которые первым аргументом принимают ссылку на объект self (работают с конкретным объектом, для которого вызываем)



class B:
    var1 = 'переменная класса (атрибут класса)'

    def __init__(self):
        self.var2 = 'переменная объекта'
        print('__init__')

    def test(self, a: str):
        print(a + self.var1)
        

# print(B.var1) # переменная класса (атрибут класса)
# print(B.var2) #AttributeError: type object 'B' has no attribute 'var2'

# b = B()
# B.__init__(b)
# print(b.var1) #переменная класса (атрибут класса)
# print(b.var2) #переменная объекта

# B.test(b, 'hello ') # метод объекта можно вызвать через класс, передав ссылку на объект (перменную в которой хранится объект)

# b.test('hello ') # при вызове метода через объект ссылка на объект передается автоматически
    
    


class Salary:
    nalog = 0.15

    def __init__(self, zp, staj):
        self.zp = zp
        self.staj = staj

    def sum_zp(self):
        zp = self.zp * self.staj * 12 * (1 - self.nalog)
        print(zp)

# person1 = Salary(15000, 3)
# person1.sum_zp()
        

class Car:
    def __init__(self, owner, year, model):
        self.owner = owner
        self.year = year
        self.model = model
        self.mileag = 0
        self.is_going = False

    def go(self, km):
        self.is_going = True
        self.mileag += km
        print('Whuuuuuuuum')

# new_car = Car('Malik', 2018, 'lx570')
# new_car.go(15)
# new_car.go(5)
# print(new_car.mileag, new_car.is_going)



    
