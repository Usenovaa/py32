'''=============== Словари dict ==============='''
# наиболее часто используемая структура данных, позволяющая хранить объекты, для доступа к ним используется ключ

# изменяемый, итерируемый, неиндесируемый, упорядоченный тип данных, в котором значения хранятся в виде ключа и значения {ключ: значение}

# {} -> литералы

# dict_ = {}
# print(type(dict_))

# dict_ = {'one': 1, 2: 'two', 3: 'three'}
# print(dict_['one'])
# print(dict_[3])

# ключи должны относиться к неизменяемым типам данных
# dict_ = {[1, 2]: 1} # TypeError: unhashable type: 'list'

# ключи в словарях должны быть уникальными
dict_ = {'one': 1, 2: 'two', 3: 'three', 'one': 100}
# print(dict_)

# значения могут относиться к любому типу данных
dict_ = {'one': 1, 'two': True, 'three': [1, 2, 3, 4]}
# print(dict_)


'''================ Создание словарей ==============='''
# 1. {}
dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}
# dct['hobby'].append('gogo')
# print(dct)

# 2. dict()
# tuple_ = ([1, 2], (2, 3))
# dict1 = dict(tuple_)
# print(dict1)
# tuple_ = ([1, 2], [2, 3])

# dict_ = dict(['a ', 'cd', 'de'])
# print(dict_)

# dict_ = dict(short=23, a=66)
# print(dict_)

# a, b = 'hl'
# print(a)


'''============= Методы словарей ============='''
# print(dir(dict))

# .clear() -> очищает словарь
# dict_ = {'one': 1, 'text': 'hello world', 'python': 'Фиксики'}
# dict_.clear()
# print(dict_)

# .copy() -> возвращает копию словаря
# dict_ = {'one': 1, 'text': 'hello world', 'python': 'Фиксики'}
# dict_copy = dict_.copy()
# print(dict_copy)

# dict.fromkeys(iterable, [value]) -> создает словарь с ключами из iterable и значением value (для всех ключей одинаковое, по умолчанию None)
lst = ['name', 'age', 'last_name']
dict_ = dict.fromkeys(lst)
dict_ = dict.fromkeys('abcd')
# print(dict_)

'''получение элементов из словаря'''
dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}
# value = dct['name'] # John
# value = dct['nam'] # KeyError (будет ошибка, так как тагого ключа нет)

# .get(key, [default]) -> возвращает значение по ключу, но если ключа не, не бросает исключение (ошибка), а возвращает default
value1 = dct.get('name') #John
value2 = dct.get('hello', 'no such key') #no such key
value3 = dct.get('hello') # None
# print(value2)


'''изменение элементов словаря'''
dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}
# 1.
# dct['name'] = 'Sam'
# print(dct)

# 2.
# .update(new_dict) -> добавляет new_dict в словарь
new_dict = {'name': 'Tom', 'city': 'Bishkek'}
dct.update(new_dict)
# print(dct)


# .setdefault(key, [default_value]) -> работает как метод get (возвращает значение по ключу или default_value, если такого ключа нет), но если ключа нет, он создает новую пару с этим ключом и значение default_value

# 1. получение значения
dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}
a = dct.setdefault('age')
# print(a)

# 2. добавление пары
dct.setdefault('job', 'IT')
# print(dct)


# .keys() -> возвращает все ключи в словаре
# .values() -> возвращает все значения в словаре
# .items() ->  возвращает все пары в словаре

dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}
# print(dct.keys()) #dict_keys(['name', 'last_name', 'age', 'hobby'])
# print(dct.values()) # dict_values(['John', 'Snow', 26, ['football', 'fishing', 'auto']])
# print(dct.items()) #dict_items([('name', 'John'), ('last_name', 'Snow'), ('age', 26), ('hobby', ['football', 'fishing', 'auto'])])

'''удаление элементов'''
# .pop(key, [messge]) -> удаляет пару по ключу и возвращает значение. Если ключа нет, возвращает message, если не пердать message бросает исключение KeyError

dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}

# popped = dct.pop('name')
# print(dct, popped)

# dct.pop('job') # KeyError

# popped = dct.pop('job', 'Нет такого ключа')
# print(popped)


# .popitem() -> удаляет последнюю добаленную пару и возвращает ключ и значение
dct = {'name': 'John', 'last_name': 'Snow', 'age': 26, 'hobby': ['football', 'fishing', 'auto']}
popped = dct.popitem()
key, value = dct.popitem()
# print(dct)
# print(key, value)


