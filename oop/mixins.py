'''
Миксины -> классы, которые используются для наследования
'''
# классы примеси, задача: расширять функционал класса (добавляем методыб атрибуты) Не предназначены для создания от них объектов


class MoveMixin:
    def move(self):
        print('двигаюсь')


class StopMixin:
    def stop(self):
        print('Стою')


# s = StopMixin() # ошибки не будет, но нельзя
# s.stop()


# class Car(MoveMixin, StopMixin):

    
#     def rent(self):
#         pass

#     def remont(self):
#         pass


# class Person(MoveMixin, StopMixin):
#     pass


# car1 = Car()
# car1.move()
# car1.stop()

# sam = Person()
# sam.move()
# sam.stop()
        

class PersonInitMixin:
    def __init__(self, name, age, last_name):
        self.name = name 
        self.age = age
        self.last_name = last_name


class GetInfoMixin:
    def get_info(self):
        print(f'name: {self.name}\nage: {self.age}\nlast_name: {self.last_name}')


class YearMixin:
    def get_year(self):
        print(2023 - self.age)
        

class Person(PersonInitMixin, GetInfoMixin, YearMixin):
    pass

# p1 = Person('Peter', 34, 'Jackson')

# p1.get_info()
# p1.get_year()

class Child(PersonInitMixin, YearMixin):
    pass

# c1 = Child(' ', 4, '  ')
# c1.get_year()



class CreateMixin:
    def create(self, key, todo):
        if key in self.todos.keys():
            return'Такая задача уже существует'
        
        self.todos[key] = todo
        return self.todos
    
class DeleteMixin:
    def delete(self, key):
        deleted = self.todos.pop(key)
        return f'задача {deleted} успешно удалена'
    

class UpdateMixin:
    def update(self, key, todo):
        if key in self.todos:
            self.todos[key] = todo
            return 'update'
        return 'нет такой задачи'


class Note(CreateMixin, DeleteMixin, UpdateMixin):
    todos = {'h/w': 'tasks'}

# tasks = Note()
# print(tasks.create('h/w2', 'bla bla bla'))
# print(tasks.delete('h/w'))
# print(tasks.update('h/w', 'math'))
# print(tasks.todos)
