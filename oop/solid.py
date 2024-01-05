'''
SOLID -> аббревиатура набора принципов проектирования, для ООП
'''
# 1. S -> Single responsibility Priciple
# Принцип единственной ответственности -> требует чтобы один класс выполнят только одну работу (задачу)

# class ExportCSV:
#     def __init__(self, data):
#         self.data = data

#     def prepare(self, data):
#         result = ''

#         for dict_ in data:
#             line = f'{dict_["name"]}, {dict_["last_name"]}'
#             result += line
#         return result
    
#     def write_file(self, filename):
#         with open(filename, 'w') as file:
#             file.write(self.prepare(self.data))


data = [
    {
        'name': 'Sherlock',
        'last_name': 'Holmes'
    },
    {
        'name': 'John',
        'last_name': 'Snow'
    },
    {
        'name': 'John',
        'last_name': 'Watson'
    }
]

# exp = ExportCSV(data)
# exp.write_file('data.txt')


class FormatData:
    def __init__(self, data):
        self.data = data

    def prepare(self):
        result = ''

        for dict_ in self.data:
            line = f'{dict_["name"]}, {dict_["last_name"]}'
            result += line
        return result
    

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)


# data_ = FormatData(data)
# prepared_data = data_.prepare()

# writer = FileWriter('data.txt')
# writer.write_file(prepared_data)
            
# 2 O -> Open-Closed Principle (OCP) 
# Принцип открытости/закрытости (открыт для расширения, закрыт для изменения (модификации))

# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer 
#         self.price = price

#     def give_discount(self):
#         if self.customer == 'fav':
#             return self.price * 0.05
#         if  self.customer == 'vip':
#             return self.price * 0.2

'''соблидение принципа OCP''' 

# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer 
#         self.price = price

#     def give_discount(self):
#         return self.price * 0.05


# class VIPDiscount(Discount):
#     def give_discount(self):
#         return super().give_discount() * 0.2


# class VIPSDiscount(Discount):
#     def give_discount(self):
#         return super().give_discount() * 0.4
    

# 3. Liskov Substitution Principle
# Принцип постановки Лисков
# Для любого класса клиент должен иметь возможность использовать любой подкласс (Дочерний), не замечая разницы между ними (поведение программы не должно меняться)

# class Animal:
#     def __init__(self, attrs):
#         self.attrs = attrs

#     def eat(self):
#         print('ate some food')

# class Cat(Animal):
#     def eat(self, amount=0.1):
#         if amount > 0.3:
#             print('Слишком много')
#         else:
#             print('ate some food')

# class Dog(Animal):
#     def eat(self):
#         print('Ate some doog\'s food')


# pluto = Dog({'name': 'Pluto', 'age': 3})
# bethoven = Dog({'name': 'Bethove', 'age': 2})
# cat =  Cat(('Garfild', '4'))


# animals = [pluto, bethoven, cat]
# for animal in animals:
#     if animal.attrs['age'] > 2:
#         print('Взрослое животное')


# class Animal:
#     def __init__(self, name, age):
#         self.attrs = {'name': name, 'age': age}

#     def eat(self, amount=0):
#         print('ate some food')

# class Cat(Animal):
#     # def __init__(self, name, age):
#     #     super().__init__(name, age)

#     def eat(self, amount=0.1):
#         if amount > 0.3:
#             print('Слишком много')
#         else:
#             print('ate some food')

# class Dog(Animal):
#     # def __init__(self, name, age):
#     #     super().__init__(name, age)

#     def eat(self, amount=0):
#         print('Ate some doog\'s food')

# pluto = Dog('pluto', 3)
# bethoven = Dog('Bethove',2)
# cat =  Cat('Garfild', 4)

# animals = [pluto, bethoven, cat]

# for animal in animals:
#     if animal.attrs['age'] > 2:
#         print('Взрослое животное')
#     animal.eat(9)
        

# 4. I -> Interface Segregation Principle
# Принцип разделения интерфейсов

# class Shape:
#     def draw(self):
#         raise NotImplementedError('Нужно переопределить')
    
# class Circle(Shape):
#     def draw(self):
#         pass

# class Rectangle(Shape):
#     def draw(self):
#         pass


        
# class Creature:
#     def __init__(self, name):
#         self.name = name

#     def swim(self):
#         pass

#     def fly(self):
#         pass

#     def walk(self):
#         pass

#     def talk(self):
#         pass

# class Human(Creature):
#     pass

# class Fish(Creature):
#     pass


# правильно
          
# class Creature:
#     def __init__(self, name):
#         self.name = name

# class Swimmer:
#     def swim(self):
#         pass

# class Walker:
#     def walk(self):
#         pass

# class Talker:
#     def talk(self):
#         pass

# class Flyer:
#     def fly(self):
#         pass


# class Human(Creature, Walker, Talker, Swimmer):
#     ...

# class Fish(Creature, Swimmer, Flyer):
#     pass

# class Bird(Creature, Walker, Flyer, Swimmer):
#     ...

# 5. D -> Dependency Inversion Principle
#  Принцип инверсии зависимостей
        


# class TerminalWriter:
#     def write(self, msg):
#         print(msg)

# class FileWriter:
#     def write(self, msg):
#         with open('log.txt', 'w') as file:
#             file.write(msg)

# import time

# class Logger:
#     def __init__(self):
#         self.prefix = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())

#     def log_str(self, msg):
#         TerminalWriter().write(msg)

#     def log_file(self, msg):
#         FileWriter().write(msg)


# logger = Logger()
# print(logger.prefix)
# logger.log_str('hello')
        

'''========='''
# class TerminalWriter:
#     def write(self, msg):
#         print(msg)

# class FileWriter:
#     def write(self, msg):
#         with open('log.txt', 'w') as file:
#             file.write(msg)


# class TestWriter:
#     pass


# import time

# class Logger:
#     def __init__(self):
#         self.prefix = time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())


#     def log(self, message, logger):
#         logger().write(message)
    
# l = Logger()
# l.log('hello', FileWriter)
    
# l2 = Logger()
# l2.log('test', TerminalWriter)
# l3= Logger()
# l3.log('hhh', TestWriter)
