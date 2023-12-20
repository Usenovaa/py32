'''Принцип ООП Наслевование'''

'''ООП есть 3 основных принципа - наследование, инкапсуляция, полиморфизм. (придают объектам новые свойства)'''

'''
============ Наследование =============
принцип, в котором мы можем унаслевовать, переопределить в дочернем классе все методы и атрибуты родительского класса. Создаем новый класс на основе существующего
'''

# Синтаксис

# class Родительский_класс:
#     # методы_и_атрибуты_родительского_класса
#     ...

# class Дочерний_класс(Родительский_класс):
#     # методы и атрибуты_дочернего_класса
#     ...

'''========================'''

class Animal:
    legs = 4

    def make_sound(self):
        print('I\'m animal')


class Cat(Animal):
    def make_sound(self): #переопределяем метод родительского класса (название такое же, функционал другой)
        print('Мяу Мяу')

# Теперь класс Cat имеет, те же свойства (атрибуты/переменные) и методы, что и класс Animal (но метод make_sound переопределен)

class Kitten(Cat):
    pass

# Теперь класс Kitten имеет, те же свойства (атрибуты/переменные) и методы, что и классы Animal и Cat

# cat = Cat()
# print(cat.legs)
# cat.make_sound()

# cat1 = Kitten()
# cat1.legs
# cat1.make_sound()


class A:
    a = 'атрибут класса A'

    def method(self):
        print('Метод внутри класса A')


# obj = A()
# print(obj.a)
# obj.method()

        
class B(A):
    '''
    Наследовали все методы и атрибуиты класса A
    '''
    pass

# obj_b = B()
# print(obj_b.a)
# obj_b.method()


class C(A):
    '''
    Наследовали все методы и 
    атрибуты у класса А
    и полностью переопределили метод
    method, и определили новый атрибут класса в классе C

    '''
    c = 'Атрибут класса С'

    def method(self):
        print('Метод класса C')

# obj_c = C()
# print(obj_c.a)
# obj_c.method()
# obj_c.c
        
'''
mro (method resolution order) -> порядок поиска атрибутов/методов
'''

# print(C.__mro__)
# print(C.mro())

# class Person:
#     pass

'''одинаковые записи'''

# class Person(object):
#     pass


'''============ Виды наследования ============'''
# 1. одиночное наследование -> наследуемся от одного родительского класса
# 2. иерархическое наследование -> когда у одного родительского класса много дочерних классов
# 3. многоуровневое наследование -> когда мы наследуемся от класса, у которого уже есть родитель
# 4. множественное наследование -> когда мы наследуемся в дочернем классе от нескольких классов (у дочернего класса несколько родительских классов)
# гибридное наследование -> когда используется несколько видов наследования

# 1. 2
class Person(object):
    def __init__(self, name, age, last_name):
        self.name = name
        self.age = age
        self.last_name = last_name

    def display_info(self):
        print(f'Name: {self.name}\nLast_name: {self.last_name}')

class Student(Person):

    '''
    1. полностью переопределить
    (занимает много времени и код повторяется)
    '''

    def __init__(self, name, age, last_name, faculty, class_):
        self.name = name
        self.age = age
        self.last_name = last_name
        self.faculty = faculty
        self.class_ = class_

    '''
    2. дополняем родительский метод
    вызываем его и дописываем что нам нужно
    '''

    def __init__(self, name, age, last_name, faculty, class_):
        Person.__init__(self, name, age, last_name)
        self.faculty = faculty
        self.class_ = class_

    '''
    3. исправляем недостатки 2го вариант, желательно не обращать напрямую к родительскому классу (имя класса может измениться)
    '''

    def __init__(self, name, age, last_name, faculty, class_):
        super().__init__(name, age, last_name)
        self.faculty = faculty
        self.class_ = class_



    def study(self):
        print(f'{self.name} studies')


# sam = Student('Sam', 21, 'Black')
# sam.display_info()
# sam.study()

# 3
# class Employee(Person):
#     pass


# 4. 5
# class A(Person):
#     ...


# class B(Person):
#     ...


# class C(Person):
#     ...

# class M(A, B, C):
#     pass

# print(M.mro())

'''создайте класс А и в нем определите метод my_range с помощью которого мы будем создавать списки в измененном диапазоне'''

class A:
    def my_range(self, n):
        return list(range(n+1))
    
a = A()
# print(a)
# print(a.my_range(10))
# print(A().my_range(17))
    

class My_str(str):
    def __init__(self, s):
        self.s = s

    def append(self, string):
        self.s += string
        return self.s

    # pass

s = My_str('hello')

s.append(' world')
# print(s.s)




'''
issubclass() -> проверяет, является ли класс, дочерним классом
isinstance() -> проверяет, является ли объект экземпляром класса
'''

# print(issubclass(My_str, str))
# print(issubclass(str, object))
# print(issubclass(My_str, Person))

# print(isinstance(s, My_str))
# print(isinstance(s, str))
# print(isinstance(s, Person))


class User:
    def __init__(self, username, email, password, city, age):
        self.username = username
        self.email = email
        self.password = password
        self.city = city
        self.age = age
        self.posts = []
    
    def describe_user(self):
        print(f'email: {self.email}')

    def create_post(self, img, description):
        self.posts.append({'img': img, 'descr': description})
        return 'Пост опубликован'
    
    def view_posts(self):
        print('все ваши публикации: ', self.posts )
    
# user = User('test_user', 'test@gmail.com', 12345678, 'Osh', 32)
# user.create_post('/home/hello/Documents/image.jpeg', 'бла бла бла')
# user.view_posts()
        

class Admin(User):
    def __init__(self, username, email, password, city, age, privileges):
        super().__init__(username, email, password, city, age)
        self.priv = privileges

    def show_privileges(self):
        print(self.priv)

    def delete_post(self, user):
        user.posts.pop()
        print(f'Вы успешно удалили пост пользователя {user.username}')


# admin = Admin('admin', 'admin@gmail.com', 1, 'Bishkek', 15, 'delete posts')

# admin.delete_post(user)
# user.view_posts()





'''
========= Множественное наследование ============
'''

class Grandpa:
    def sleep(self):
        print('I\'m sleeping')

class Grandma:
    def cook(self):
        print('I\'m cooking')


class Father:
    last_name = 'Black'

    def work(self):
        print('I\'m working')

class Mother(Grandma, Grandpa):
    last_name = 'Brown'

class Child(Mother, Father):
    pass

# print(Child.mro())

# child = Child()
# child.cook()
# child.sleep()
# child.work()
# print(child.last_name)



'''==== Проблемы множественного наследования ==='''

# Проблема Ромба

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# print(D.mro())


# проблема ромба, заключалась в том, что при поиске атрибутов мы заходили два раза в один класс
# данная проблема решена -> mro 

#          A
    

#     B         C


#          D

# DCABA



'''========Проблема Перекресного наследования ======='''
# Скрещенного наследования (не решена)

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass

# class M(C, D):
#     pass

# print(M.mro()) # не может создать (порядок) mro




# class X:
#     ...

# class Y:
#     ...

# class Z:
#     ...

# class A(X, Y):
#     ...

# class B(Y, Z):
#     ...

# class M(B, A, Z):
#     ...

# M B A X Y Z obj
# print(M.mro())
