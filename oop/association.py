'''
Абстракция - принцип ООП, в котором создается класс пустышка, где задаются атрибуты и методы, чтобы не забыть их переопределить в дочерних классах
'''

from abc import ABC, abstractmethod

class A(ABC): #объявили Абстрактный класс

    def method(self): # обычный метод, его переопределять не обязательно
        print('Обычный метод')
    
    @abstractmethod 
    def method2(self): # метод обязательный к переопределению
        print('Абстрактный метод')
    
    @abstractmethod
    def method3(self): # метод обязательный к переопределению
        # обычно не определяют логику 
        pass


# a = A() # Нельзя создавать объекты от Абстрактного класса, в тором есть abstractmethod
    
# Абстрактный метод - методЮ у которого есть объявления, но нет реализации (pass). Для его создания нужно использовать декоратор abstractmethod

# class B(A):
#     def method2(self):
#         print('обязательно нужно переопределить')

#     def method3(self):
#         print('переопределили')

# b = B()
# b.method()
    
from abc import ABC, abstractmethod, abstractproperty 

class AbstractAnimal(ABC):
    
    @abstractproperty # для создания абстрактных атрибутов
    def legs(self):
        pass

    @abstractmethod
    def voice(self):
        pass


# class Dog(AbstractAnimal):
#     pass

# dog = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice
    

# class Dog(AbstractAnimal):
#     def voice(self):
    #   pass

# dog = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract methods legs


# class Dog(AbstractAnimal):
#     legs = 4

#     # def legs(self):
#     #     pass
#     # voice = 'Gav'

#     def voice(self):
#         print('gav gav')

# dog = Dog()


class Abst(ABC):

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def set_info(self):
        pass


class Automobile(Abst):
    def __init__(self, model, year, owner):
        self.model = model
        self.year = year 
        self.__owner = owner

    def get_info(self):
        return f'model: {self.model}\nyear: {self.year}'
    
    def set_info(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner
    
# automobile = Automobile('vv', 2013, 'Shirin')
# automobile.set_info('Malik')
# print(automobile.get_owner())
        
class Auto(Automobile):
    
    def __init__(self, model, year, owner, color):
        super().__init__(model, year, owner)
        self.color = color
    
    @property
    def owner(self):
        return self.get_owner()
    
    @owner.setter
    def owner(self, owner):
        # self._Automobile__owner
        self.set_info(owner)

    

# auto = Auto('rerrge', 2016, 'Katana', 'blue')
# print(auto.__dict__)
        

'''
============= Ассоциация =============

принцип ООП, в котором два класса связаны друг с другом
'''

# Композиция - сильная связь
# Агрегация - слабая связь


'''
Композиция
A -> компонентный (предоставляет объект (компонент)     
|               для составного класса)
|
|
|
V
B -> составной (содержит объект другого класса (A))
'''


class Engin:
    def __str__(self):
        return 'двигатель'

class Wheel:
    def __str__(self):
        return 'колесо'
    
class Elochka:
    def __str__(self):
        return 'елочка'

class Car:
    def __init__(self, model, freshener):
        self.model = model
        self.engin = Engin() #композиция
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
        self.freshener = freshener

# elochka = Elochka()

# car = Car('camry 3.5', elochka) # агрегация -> объект от другого класса передается при инициализации
        
# print(car.engin)
# print(car.wheels)
# print(car.freshener)

# del car #при удалении главного объекта удаляются все компоненты (композиция)
# car.engin # уже не доступен, удаляется вместе с объектом

# print(elochka) # слабая связь, при удалении главного объекта, объект елочки все еще существует
        
'''
агрегация
'''

# class Salary:
#     def __init__(self, pay):
#         self.pay = pay

#     def get_total(self):
#         return self.pay * 12


# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus

#     def annualSalary(self): # годовой оклад с бонусами
#         return 'Total: ' + str(self.pay.get_total() + self.bonus)

# s = Salary(30000)

# a = Employee(s, 7000)
# print(a.annualSalary())
# del a


class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus) -> None:
        self.bonus = bonus
        self.pay = Salary(pay)

    def annualSalary(self): # годовой оклад с бонусами
        return 'Total: ' + str(self.pay.get_total() + self.bonus)
    
# a = Employee(20000, 8000)
# print(a.annualSalary())