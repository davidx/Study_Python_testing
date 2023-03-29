# import requests
# import bs4
#
# import numpy as np
# a = np.

# i = 0
# while i < 11:
#     print(i)
#     i = i +1

# a = 8
# b = 1
# while(a>5):
#     a-=2
#     b+=a
#     print (b)

# a =1
# b = 3
# while(a!=5):
#     a+=1
#     b+=a
#     print(b)
# print('INput an any nimber, please')
# num = int(input())
# data = []
# while num!=0:
#     data.append(num)
#     num = int(input())
# data.sort()
# print(data)

# input('Введите любое количестов слов через ентер')
# words = input()
# data = []
# while words !='':
#     if words not in data:
#         data.append(words)
#     words = input()
# for item in data:
#     print(item)

# num = int(input())
# if num%2==0:
#     print('чётное число',num)
# else:
#     print('нечетное число',num)
#
# letter = input('input a text')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('гласная буква', letter)
# elif letter == 'y':
#     print('согласная и гласная')
# else:
#     print('Согласная', letter)

# mas = [1,2,2,4,5,]
# for item in mas:
#      print(item, end=', ')

# meel = ['мясо', 'сыр', 'сгущенка', 'конфеты']
# for food in meel:
#     if food == 'сгущенка':
#         print('no sugar!', food)
#         break
#     print('отлично перекусил', food)
# else:
#     print('хорошо, что без сгущенки')
#
# print('Good meel')


# meel = ['мясо', 'сыр', 'сгущенка', 'конфеты']
# for food in meel:
#     if food == 'сгущенка':
#         print('no sugar!', food)
#         continue
#     print('отлично перекусил', food)
# else:
#     print('хорошо, что без сгущенки')
#
# print('Good meel')

    # print('''a lot
    # of ''
    # strings''')

    # text = 'Длиннная строка'
    # print('первый знак ''')

# a = 1
# b = 73
# c = -12
# d = 2
#
#
# e=a+b
# print(e,',',type(e))

# a = -13
# b = 7
#
# a = a - b
# b = a + b
# a = b - a
#
# print(a,
#       b)

# print(3 > 10)
#
# print(2**23)
# print(50/3)

# a = -5
# b = 2
# q = a // b
# print('результатделения -5 на 2','\n',q,'\nостаток от деления = ',a%b)
# print('\nСледующее выражение')
# a = -6
# b = 2
# q = a // b
# print('результатделения -6 на 2','\n',q,'\nостаток от деления = ',a%b)
#
# f = 653457
# g = 123493
# print(f**g)
#
# 11*2.5/3
# a=11
# b=2.5
# c=3
# print(round(a*b/c,2))
#
# print(11*2.5/3)
#
# pi=3.14159
# print(round(pi**2/2))

# s = 'Hello!'
# print(s[-3:-1])
# print(s[-1])
#
# numbers = '1 2 3 4 5 6 7'
# numbers_splitSTR = numbers.split(' ')
# numbers_columnLines = '\n'.join(numbers_splitSTR)
# print('Output order:','\v',numbers_columnLines)
#
# # numb = float(input('введите число '))
# # print(numb,',',type(numb))
#
# pi = 31.4159265
# print ("%.4e" % (pi))

# day = 14
# month = 12
# year = 2012
#
# print("%d.%d.%d" % (day, month, year))
#
# L = ["а", "б", "в", 1, 2, 3, 4]
#
# print(L[3::-1])
# print(L[:3:-1])
# # [1, "в", "б", "а"]
# # [4, 3, 2]
#
# L = ['3.3', '4.4', '5.5', '6.6']
#
# print (list (map (float, L)))
#
# string = input('введите неколько целых чисел через пробел: \n')
# print(string)
# list_of_string = string.split()
# print(string, type(string))
# list_of_numbers = list(map(int, list_of_string))
# print(list_of_numbers,type(list_of_numbers))
# print(sum(list_of_numbers[::3]))

# Первое и последнее числа последовательности должны поменяться местами.
# В конец списка нужно добавить сумму всех чисел.

# str_numbers = input('Input some numbers with spaces ')
# temp_list_of_num = str_numbers.split()
# list_of_num = list(map(int, temp_list_of_num))
# list_of_num[0], list_of_num[-1] = list_of_num[-1], list_of_num[0]
# list_of_num.append(sum(list_of_num))
# print(list_of_num)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))

# Напишите программу, которая получает на вход название книги - title,
# фамилию автора - author и год выпуска - year.
#
# Полученные данные должны быть преобразованы в словарь book с ключами:
# title, author, year. Причем year нужно преобразовать в тип int.
#
# Примечание. Обратите внимание, что для отправки кода на проверку переменные title, author, year объявлять не нужно.
# Не забудьте удалить строку кода с её объявлением перед тем, как отправить код на тестирование.

# title = input('Введите название книги: ')
# author = input('Введите фамилию автора книги: ')
# year = int(input('Введите год выпуска книги: '))
#
# book = {'title':title,'author':author, 'year': year}
# print(book, type(book['year']),type(['author']))
#
# a={'a', 'b', 'c', 'd'}
# print(a)
#
#
# L = [1,1,2,3,2]
#
#
# c_L = list(set(L))
# print(c_L)


# text = ".."
# L_text = list(set(text))
# print(L_text, '\n',len(L_text))
# print(L_text, type(L_text))
# print(type(L_text))

# a = [1,2,3,4,5,6,7,8]
# b = [2,4,6,8,10,12]
#
# LS1, LS2 = set(a), set(b)
# print(LS1, '-', 'type of var.L_1:', type(LS1))
#
# print(LS2, '-', 'type of var.L_2:', type(LS2))
#
# dif_LS1_LS2 = LS1.symmetric_difference(LS2)
# print(dif_LS1_LS2)

# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# c = id(a)-id(b)
# print(c)


# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)

# x=int(input('Numbers'))
# if x is not int:
#     print(x)
# else:
#     print(x)

# L = [0,4,4,3,]
# if L:
#     print('Список - ', L)
# else:
#     print('Список пустой')

'''Запишите условие, которое является истинным,
когда только одно из чисел А, В и С меньше 45.
Иногда проще записать все условия и не пытаться упростить их.'''

# a,b,c = int(input("Введите любое целое число (a): ")), \
#     int(input("Введите любое целое число (b): ")), \
#     int(input("Введите любое целое число (c): "))
#
# if ((a>45) and (b>45) and (c<45)) or\
#    ((a<45) and (b>45) and (c>45)) or \
#    ((a>45) and (b<45) and (c>45)):
#
#    print('Есть число меньше 45')
# else:
#     print('Введите числа ещё раз: либо нет меньше 45, либо их больше одного')

# Как вытащить именно то число, чтобы отобразилосьв  программе?

'''Запишите логическое выражение, которое определяет, 
что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.'''

# a = int(input("put a number for 'a': "))
# if (-10<=a<=-1) or (2<=a<=15):
#     print('Число в запретных интервалах. Потворите ввод')
# else:
#     print(a)
#  # это получилось условие. Теперь пробуем логически.
#
# a = int(input("put a number for 'a': "))
# if not ((-10<=a<=-1) or (2<=a<=15)):
#     print('число, где надо. ', a)
# else:
#     print('Число в запретных промежутках. ', a)

'''Дано двузначное число. Определите, входит ли в него цифра 5. 
Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.'''

N = int(input('Введите двузначное число: '))
# if N % 5 == 0:
#     print('Bingo! ', N)
#
# else:
#     print(N, 'Repeat')
New_N = str(N)
# if '5' in New_N:
#     print(New_N)
# else:
#     print('error')

# if 5 in N_L:
#     print(N_L)
# else:
#     print(not N_L)

# N = int(input('Input any numb.^ '))
# frst_dig = N // 10
# scnd_dig = N % 10
#
# print(frst_dig, scnd_dig)
# print((frst_dig == 5) or (scnd_dig == 5))
