'''Напишите класс Game, с помощью которого можно создать объекты-игры, у объектов должны быть атрибуты:

type_ - тип игры
name - название игры,
extensions соответсвующий пустому списку - [].
У класса должны быть методы:

get_description, который принимает строку и возвращает описание к игре в виде названия игры и переданной строки:
Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром. 
Где Minecraft - это название игры, берется из атрибута name объекта.

get_extensions, который возвращает все подключенные расширения в виде строки разделенной пробелами, если же список extensions пуст, возвращайте сообщение:
Нет подключенных расширений   


Также напишите миксин ExtensionMixin, чтобы к игре можно было подключать расширения.

У миксина должно быть два метода:

add_extension, принимающий строку-название и добавляющий ее в список игры, также должен возвратить сообщение:

Добавлено новое расширение Multiverse-Core для игры Minecraft. 

где Multiverse-Core это строка - название расширения

remove_extension, удаляющий расширение по названию, и возращающий строку в формате:
Multiverse-Core был отключен от Minecraft. 
Если же такого расширения нет в списке должна возвращаться строка:

Такого расширения нет в списке.'''


class ExtensionMixin:
    def add_extension(self, title):
        self.extensions.append(title)
        return f'добавленно новое расширение {title} в игру {self.name}'
    
    def remove_extension(self, title):
        if title in self.extensions:
            self.extensions.remove(title)
            return f'{title} был отключен от {self.name}'
        return 'Расширение не найдено'


class Game(ExtensionMixin):

    def __init__(self, name, type_):
        self. name = name
        self.type_ = type_ 
        self.extensions = []

    def get_description(self, str_):
        return f'{self.name} это {str_}'

    def get_extensions(self):
        if self.extensions:
            return ' '.join(self.extensions)
        
        return 'Нет подключенных расширений '    
    

# game = Game('Test', 'jjj')
# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром'))
# print(game.add_extension('1'))
# print(game.add_extension('2'))
# print(game.remove_extension('0'))
# print(game.remove_extension('1'))
# print(game.get_extensions())
    
'''Герой.
# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты(Solder) и герои(Hero).
# У всех есть свойство, содержащее уникальный номер объекта(id), и свойство в котором хранится принадлежность команде(team).
# У солдат есть статический метод "go_hero", который в качестве параметра принимает уникальный номер(id) героя. И возвращает 'Иду за героем {уникальный номер героя}'
# У героев есть атрибут класса 'level = 0' и есть метод увеличения собственного уровня 'level_up' который при вызове увеличивает уровень героя на единицу.

# В основной ветке программы создается по одному герою 'hero1' и 'hero2'.
#     hero1 = (1, 'Blue)
#     hero2 = (2, 'Red)
# В цикле генерируются объекты-солдаты(10 солдат). В списке obj1 будут храниться обьекты солдаты команды 'Blue', а в obj2 'Red'. Их принадлежность команде определяется случайно.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран сообщение. Если количество солдат команды Blue больше команды Red, тогда выведете сообщение "Первый герой победил у него: {len(obj1)} солдат", если же количество солдат второй команды больше: "Второй герой победил у него: {len(obj2)} солдат" иначе "Количество солдат одинаковое!".
# Также у героя, принадлежащего команде с более длинным списком, поднимается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Также вывидите уровень героев.'''

import random


class Hero:
    level = 0

    def __init__(self, id_: int, team: str) -> None:
        self.id = id_
        self.team = team
    
    def level_up(self) -> None:
        self.level += 1
    


class Soldier:
    def __init__(self, id_, team):
        self.id = id_
        self.team = team

    @staticmethod
    def go_hero(id):
        return f'Иду за героем {id}'
    

hero1 = Hero(1, 'Blue')
hero2 = Hero(2, 'Red')

obj1 = []
obj2 = []


for i in range(10):
    res = random.choice(['Blue', 'Red'])
    s = Soldier(random.randint(1, 10000), res)
    if res == 'Blue':
        obj1.append(s)
    else:
        obj2.append(s)

if len(obj1) > len(obj2):
    print(f'Первый герой победил, у него {len(obj1)} солдат')
    hero1.level_up()
elif len(obj1) < len(obj2):
    print(f'Второй герой победил, у него {len(obj2)} солдат')
    hero2.level_up()
else:
    print('Количество солдат одинаковое')
    
print(obj1[0].go_hero(hero1.id))
print(hero1.level)
print(hero2.level)