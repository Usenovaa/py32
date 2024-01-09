'''
Введение в PostgreSQL
'''

# Система управления базами данных (СУБД) -> компдекс программно-языковых средств, позволяющих управлять базами данных (создавать бд, манипулировать данными)

# MySQL, Firestore, MongoDB, SQLite


# БД -> хранилище (предназначено для хранения, изменения и обработки информации, преимущественно большиъ объемов)

# SQL (Structured Query Language) -> Язык запросов (применяется для создания, поиска, получения, удаления... данных или бд)


'''
============ Команды =============
'''
# psql -> если есть пользователь и бд с таким же именем как ваш юзернэйм на компе (заходим в postgres под  вашим пользователем и подключаемся к вашей бд)

# 1. sudo -i -u postgres -> перехлод в учетную запись postgres (# exit -> выход с учетной записи postgres)
# 2. psql -> переход к командной строке postgres

# sudo -u postgres psql -> напрямую переходим к командной строке (для входа в postgres)

# psql -U <username> -> переход к командной строке (напрямую) через пользователя <username> (для входа в postgres)
# psql -d <username/db> (для входа в postgres)

# \q -> выход из командной строки
# \l -> выводит список бд
# \du -> выводит список пользователей


'''
======== Запросы ========
'''
# SQL -> не чувствителен к регистру, но желательно ключевые слова писать в верхнем регистре (CREATE, ALTER, SELECT, JOIN, GROUP BY...) 

# CREATE USER <username>; -> создание пользователя
# CREATE USER <username> WITH PASSWORD 'password';
# CREATE USER <username> WITH SUPERUSER PASSWORD 'password';

# CREATE DATABASE <db_name>; -> создание бд
# CREATE DATABASE WITH OWNER <user>; 


'''
===========  ============
'''
# 1. Numeric Types (Числовый типы)
    # a. smallint(2 bytes) -> -32т до 32т
    # b. integer(4 bytes) -> от -2млрд до 2млрд
    # c. bigint (8 byte)

    # d. smallserial -> целые числа с автоинкрементом (только положительные) (1-32тыс)
    # e. serial 
    # f. bigserial

# ...

# 2. Character Types (Строковые/Текстовый)
    # a. varchar(кол-во символов) -> макс. кол-во символов 255 -> 'one' (занимает только нужное кол-во)

    # b. char(кол-во символов) ->  макс. кол-во символов 255 -> 'one       ' (если в скобках указать char(10), то недостающие символы заменяет на пробелы)

    # c. text() -> Неограниченное кол-во символов

#3. Boolean Type 
    # boolean (TRUE/FALSE)

# 4. date -> календарные даты (год.месяц.день)

# 5. location -> координаты (x, y) (243, -9)

# 6. Enumerated Types 
    # ('f', 'm')
    # CREATE TYPE <любое название> AS ENUM ('male', 'female')


'''
============ Ограничения (constraint) ===========
'''
# 1. UNIQUE -> все значения должны быть уникальными
# 2. DEFAULT -> у столбца будет значения по умолчанию (запишестя если не передать данные)
# 3. NULL | NOT NULL -> определет будет ли столбец обяхательным для заполнения
# 4. CHECK -> проверяет значение столбца на определенное условие
# 5. PRIMARY KEY -> (первичный ключ) определяет, будет ли столбец идентификатором (нужен чтобы отличать одну запись от другой) (участует в сязях)
# 6. FOREIGN KEY -> используется для связей (внешний ключ)  создание связей


'''
создание таблиц

CREATE TABLE <table_name>(названия колонок с указанием типа нанных)
'''
# INSERT INTO <table_name> VALUES (данные)
# INSERT INTO <table_name>(названия колонок) VALUES (данные)
# insert into product values (nextval('product_id_seq'), 'Iphone13', 1100);
# insert into product (name, price) values ('Iphone14', 1600);
# insert into product (price, name) values (900, 'Iphone12');
# insert into product (name, price) values ('MacBookAir', 1700), ('MacBookPro', 2000), ('Iphone8+', 600);
# '''запись определенных полей в таблицу'''
# insert into product (name) value ('oooo')

'''Вывод данных из таблицы'''
# select * from product; # -- получение всех записей с таблицы (всех полей) 
# select name from product; # получение всех значений колонки name
# select price from product; # получение всех значений колонки price

'''Условия'''
# ORDER BY: Позволяет нам сортировать данные по убыванию или возрастанию. ASC(по возрастанию) и DESC(по убыванию) используються для определения сортировки
# SELECT * FROM product ORDER BY name; -- сортировка по определенному полю (по возрастанию ASC)
# SELECT * FROM product ORDER BY price DESC; -- сортировка по определенному полю (по убыванию DESC)
# SELECT name FROM product ORDER BY name ASC/DESC
# SELECT name FROM product ORDER BY id;
# SELECT name FROM product ORDER BY id DESC;

# LIMIT: Позволяет нам вернуть данные в ограниченном количестве
# SELECT * FROM product LIMIT 5; -- выводит первые 5 записей
# SELECT * FROM product OFFSET 5; -- пропускает первые 5 записей
# SELECT * FROM name_of_table LIMIT 4 OFFSET 3;
# -- пропускает первые 3 записей
# -- выбирает следующие 4 записей

# DISTINCT: Позволяет нам убирать дубликаты и возвращает только уникальные значения
# SELECT DISTINCT name FROM product;
# select distinct price from product

# =========================================== операции сравнения
# >, <, >=, <=, =, != или <>
# ======================== 
# WHERE: Используется для фильтрации по полям. Будут выводиться только те условия которые верны WHERE
# SELECT name FROM product WHERE price = 10; -- получение всех записей соответствующих этому условию
# SELECT name FROM product WHERE name = 'Iphone';

# Логические операции: and, or, not
# select * from product where not price > 15;

# проверка на вхождение (in)
# select * from product where name in ('world', 'name');

# SELECT * FROM product WHERE price >= 200 AND price <= 5000;

# BETWEEN - проверка на нахождение в диапазоне
# SELECT * FROM product WHERE price BETWEEN 200 AND 1500;



# LIKE: Выводит результать который соостветсвует введеному шаблону. Чувствителен к регистру
# ILKIE: Тоже самое только не зависит от регистра
# where name like 'A%' - имена нач на A
# like %@gmail.com
# %a% - что бы была а в слове
# like 'Ki_%' после только один символ
# like '__Ki%' перед 2 символа
# ilike не чувствителен к регистру

# SELECT * FROM product WHERE name like '%world%';
# -- выбирает все записи у которых в поле title есть названия содержащие world
# SELECT * FROM product WHERE name ilike '%world%'; --не чувтвителен к регистру


'''Удаление записей из таблицы'''
# DELETE FROM product; --удаление всех записей из таблицы
'''Условия'''
# delete from product where name = 'ooo'; -- удаление всех записей соответствующих этому условию
# delete from product where id > 15; -- удаление всех записей соответствующих этому условию
# ...

'''Обновление записей в таблице'''
# UPDATE product SET name = new_val; -- обновление всех записей в таблице
'''Условия'''
# UPDATE product SET price = new_val WHERE id < 10; -- обновление всех записей соответствующих этому условию
# UPDATE product SET price = price - 100.00
#     WHERE name = 'Iphone13';


'''================================='''
# GROUP BY - это ключевое слово которое позволяет выводить значение из колонок объеденённые в группы.
# GROUP BY: разделяет строки, возвращаемы оператором SELECT на группы. И теперь для каждой группы можно применить фукнцию

# select name, SUM(price) from product group by name;

# select name, count(*) from product group by name;

# select count(name) from product group by name;


# HAVING: Работает так же как и WHERE только он используется в GROUP BY ВСЕГДА используется с GROUP BY конструкцией.
# select * from post group by id having id > 1;


''' ======================== ALTER TABLE #редактирование таблицы (Служит для изменения таблицы после того, как она была создана с помощью инструкции CREATE TABLE.) ========================'''

#переименование таблицы
# ALTER TABLE название_таблицы RENAME TO новое_название;

#добавление нового столбца
# ALTER TABLE название_таблицы ADD COLUMN название_столбца тип ограничения;

#удаление столбца
# ALTER TABLE название_таблицы DROP COLUMN название_столбца;

#переименование столбца
# ALTER TABLE название_таблицы RENAME COLUMN старое_название TO новое_название;

#изменение типа столбца
# ALTER TABLE название_таблицы ALTER COLUMN название_столбца TYPE новый_тип;

# ALTER TABLE название_таблицы ALTER COLUMN название_столбца SET/DROP NOT NULL;

# ALTER TABLE products ALTER COLUMN price SET DEFAULT 0; # установка default

# ALTER TABLE products ALTER COLUMN price DROP DEFAULT; # удаление default

# ALTER TABLE products ADD CHECK(price > 0);
# ALTER TABLE products ADD CONSTRAINT check_price CHECK(price > 0);


'''
Import/export баз данных
'''
# write from file to db
# psql db_name < file.sql
# psql -U username -d db_name -f file.sql
# db_name -> бд должна существовать

# write from db to file
# pg_dump db_name > file.sql
# pg_dump -U username db_name > file.sql