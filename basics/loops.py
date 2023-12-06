# '''=========== Цикл for =========='''
# # это блок кода, который повторяется несколько раз
# # используется, когда нужно повторить код n-ое кол-во раз или пройтись по итерируемому объекту

# # for -> цикл, который работает с итерируемыми объектами, заканчивает свою работу, когда дошел до конца (до последнего элемента) итерируемого объекта

# # str_ = 'фиксики'

# # for a in str_:
# #     print(a)

# # for i in [1, 2, True, None, 'hello', [1, 2, 3]]:
# #     print(i)

# # for переменная in итерируемый_объект:
# #     тело цикла

# # list_ = []

# # for i in range(1, 11):
# #     list_.append(i)
# #     print(list_)

# # for i in range(1, 11):
# #     if i > 5:
# #         print('слишком много чисел')
# #     else:
# #         print(i)


# # for i in range(10):
# #     print(i)
# #     for j in range(3):
# #         print(j)
    
# # a = 1,
# # print(dir(a))

# # print(type(a))

# # print(1)
# # print(2)
# # print(3)
# # print(4)
# # print(5)
# # ...

# # for i in range(1, 10):
# #     print(i)


# # while -> цикл, который работает до тех под пока условие верно

# # while условие:
# #     тело

# # while True:
# #     print('hello')


# # count = 0
# # while True:
# #     print(count)
# #     count += 1 # count = count + 1

# # count = 0
# # while count <= 10:
# #     print(count)
# #     count += 1 # count = count + 1

# # count = 10
# # while count >= 0:
# #     print(count)
# #     count -= 1


# # while True:
# #     a = input('Введите животное: ')
# #     if a.lower() == 'собака':
# #         break

# # a = 0
# # while a: # никогда не заработает
# #     print('hello') 

# num = '6432134567'

# s = str(num)
# # sum_ = 0
# # for i in s:
# #     # print(i)
# #     sum_ += int(i) 
# #     # sum_ = sum_ + int(i)
# # print(sum_)


# sum_ = 0
# l = 0
# while l < len(s):
#     # print(s[l])
#     sum_ += int(s[l])
#     l += 1

# # print(sum_)



# '''========== Итерирование словарей ========='''

# dict_ = {1: 'one', 2: 'two', 3: 'three'}

# # for i in dict_: # по ключам
# #     print(i)

# # for i in dict_.keys(): # по ключам
# #     print(i)


# # for i in dict_.values(): # по значением
# #     print(i)

# for i in dict_.items(): # по парам
#     '''
#     в переменной i хранятсв кортежи (кляч, значение)
#     '''
#     # print(i)

# for key, value in dict_.items(): 
#     '''
#     1 ==> one
#     2 ==> two
#     3 ==> three  раздели элементы кортежа на две переменные
#     ''' 
#     # print(key, '==>', value)



# # a, b = (1, 2)
# # print(a)


'''=========== Ключевые слова в циклах ==========='''
# continue -> переход к следующей итерации (начинает следующее прохождение цикла)
# break -> выход из цикла (досрочное прерываение цикла)
# pass -> заглушка (...)

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# ls = []
# for i in range(5):
#     print(i)
#     if i == 3:
#         continue
#     a = input('Введите данные: ')
#     ls.append(a)
# print(ls)

# for i in range(10):

#     print(i)
#     # continue
#     print('hello')

# код написанный до continue  будет выполнятся вне замисимости от условия, код после continue будет пропускаться если условие верно

# for i  in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 11):
#     if i == 3:
#         print('   *   ')
#     if i == 3:
#         break
#     print(i)


# i = 0

# while i <= 10:
#     print(i)
#     if i == 7:
#         continue
#     i += 1 

# i = 0
# while True:
#     if i == 3:
#         print('hello')
    
#     print(i)
#     i += 1
#     if  i == 10:
#         break


# for i in 'hello world':
#     print(i)
#     if i == 'o':
#         break
# else:
#     print('Буквы a в строке нет')

'''=========== else в циклах ============'''
# слово else, применяется в циклах for и while
# проверяет, цикл доработал до конца без выполнения break 
# код в else отработает, если инструкция break не сработала, те цикл отработал полностью (завершился естественным путем) (зарешение через break -> принудительная остановка цикла)


i = 0
while i <= 10:
    print(i)
    if i == 12:
        break
    i += 1

else:
    print('выведены все числа ')

