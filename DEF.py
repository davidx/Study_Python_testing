# x = int(input('Введите год - '))
# def is_leap_year(x):
#     return (x%400==0) or ((x%4==0) and (x%100!=0))
# print(is_leap_year(x))
#
'''Определяем четные и нечетные числа'''
# A = int(input('Введите первое число - '))
# B = int(input('Введите второе число - '))
#
#
# def are_both_odd(A, B):
#     # return A%2!=0 and B%2!=0 - Также возможный вариант
#     return \
#             A % 2 == 1 and \
#             B % 2 == 1
#
# if are_both_odd(A, B):
#     print('Числа А и B нечетные')
# else:
#     print(are_both_odd(A, B))
#
'''Про функции
Вам нужно вместо ??? написать код, который возвращает из функции класс ветра в зависимости от его характера:

от 1 до 4 м/с включительно - "weak [1]"
от 5-10 м/c - "moderate [2]"
от 11-18 м/c - "strong [3]"
от 19 м/c - "hurricane [4]"'''

# def - объявили функцию
# get_wind_class - это мы так функцию назвали
# speed - переменная , которую мы передали в функцию get_wind_class. Выходит, что это аргумент этой функции

# speed = int(input('Введите скорость ветра - '))
# def get_wind_class(speed):
#     if (1 <=speed <= 4):
#         return "weak [1]"
#     elif (5<=speed<=10):
#         return "moderate [2]"
#     elif (11 <= speed <= 18):
#         return "strong [3]"
#     elif (speed>=19):
#         return "hurricane [4]"
# print(get_wind_class(speed))

'''Рбаота со словарём'''
'''Дан словарь - user_database
Допишите функцию check_user так, чтобы она по логину пользователя проверяла, 
существует он или нет, после чего с помощью вложенного условия проверяла
правильность пароля этого пользователя.

Функция должна возвращать только True или False.'''

# user_database = {'user': 'password',
#                  'iseedeadpeople': 'greedisgood',
#                  'hesoyam': 'tgm'}
#
# # username = input('Ввести имя пользователя: ')
# # password = input('Ввести пароль: ')
#
# def check_user(username, password):
#     if (username in user_database.keys()) and (password in user_database.values()):
#         return True
#     else:
#         return False
#
# print(check_user(username = 'user', password = '234'))

'''проверить есть ли имя пользователя в словаре.
проверить корректный ли пароль.
как?'''

# Ещё один вариант решения

# username = input('TYpe a username: ')
# password = input('Type password for username: ')
# user_database = {'user': 'password',
#                  'iseedeadpeople': 'greedisgood',
#                  'hesoyam': 'tgm'}
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
# print(check_user(username, password))


# for i in letters:
#         if i == 'a' or i == 'o' or i == 'e'\
#                 or i == 'u' or i == 'i':
#                 vowels.append(i)
#         elif i == 'y':
#                 consonants.append(i)
#                 vowels.append(i)
#         else:
#                 consonants.append(i)
# print('В списке есть гласные буквы - ', vowels, len(vowels), '\n'
# 'В списке есть согласные буквы - ', consonants, len(consonants), '\n')

# n = 3
# def print_ladder(n):
#     for i in range(1, n):
#       for
# print(print_ladder(n))

#
# def print_ladder(n):
#     for i in range(1, n+1):
#         print(i * '*')
# print_ladder(n = 3)


'''Напишите функцию print_2_add_2, которая будет складывать 2 и 2, 
а затем печатать этот результат. Не забудьте вызвать функцию, чтобы увидеть результат.'''

# def print2_add_2():
#     x = 2*2
#     print(x)
#
# print2_add_2()

'''Напишите функцию hello_world, которая будет печать приветственную строку "Hello World".'''

# def hel_wrld():
#     print('Hello world')
#
# hel_wrld()

'''Напишите функцию, которая проверяет,
является ли число n делителем числа a. И выводит на экран соответствующее сообщение,
является ли число делителем или нет.'''

# def what_is_a(a,n):
#     if a % n == 0:
#         print(n)
#     else:
#         print(not n)

'''Напишите функцию, которая печатает «обратную лесенку» следующего типа:
n = 3
***
**
*
n = 4
****
***
**
*'''
# def print_ladder(n):
#     for i in range(n,0,-1):
#         print(i * '*')
# print_ladder(4)


'''Напишите функцию, которая будет возвращать количество делителей числа а.'''
# a = 5
# def a_division(a):
#     cnt = 0
#     for i in range(1, a+1):
#         if a % i == 0:
#             cnt += 1
#
#     return cnt
# print(a_division(a))

'''Напишите функцию, которая проверяет, является ли данная строка
палиндромом или нет, и возвращает результат проверки. Пример:

check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True'''

thing = input('type some words: ')
def if_palindrome(thing):
    thing = thing.lower()
    thing = thing.replace(" ", "")
    thing = thing.replace("\n", "")

    if thing == thing[::-1]:
        return True
    else:
        return False

print(if_palindrome(thing))


