# a=15
# if a>5:
#     a=5
# a=a+2
# print(a)

# a = 11
# if a < 6:
#     a = a+13
# else:
#     a = a-8
# print(a)
#
# a = 7
# b = 9+a
# print("a=F(",b,")")
#
#
# a = 16
# b = 14 + a
# print("b=",b)


# mx = 0
# s = 0
# x = int(input())
# if x < 0:
#     s = x
#
# b = 7
# b /= b
#
# if x > mx:
#     mx = x
#
# print(s)
# print(mx)

# is_rainy = True
# heavy_rain = False
#
# if is_rainy:
#     if heavy_rain:
#         print('Брать зонт')
#     else:
#         print('Надеть дождевик')
# else:
#     print('Не брать зонт')

# zero = 3
# if zero:
#    print(10 / zero)
# else:
#    print("Делить на ноль нельзя")

# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!")
# #
# try:
#     x = int(input('введите число/числа - '))
#     print(x)
# except ValueError as error:
#     print(error)
#     print('Введите число заново')
# else:
#     print(f'Вы ввели правильное число - {x}')
# finally:
#     print('Выход из программы')
#
# '''Проверка целого числа А'''
#
# A = int(input('Введите число - '))
# if (A % 2 == 0) or (A % 3 == 0):
#     print(A, 'Число кратно 2-м и 3-м')


# '''Проверка времени суток'''
#
# hour = int(input('Веедите значение часа - '))
#
# if 6 <= hour < 12:
#     print('Сейчас утро')
# elif 12 <= hour < 18:
#     print('Day time!')
# elif 18 <= hour < 23:
#     print("It's evening time'")
# else:
#     print("It's night, my friend'")

# x = int(input('Enter something for X: '))
# y = int(input('Enter something for Y: '))
#
# if x > 0 and y > 0:
#     print('I')
# elif x < 0 and y > 0:
#     print('II')
# elif x < 0 and y < 0:
#     print('III')
# else:
#     print('IV')

'''Определите сезон в зависимости от номера месяца и выведите сообщение:'''
# month = int(input('Введите номер месяца - '))
#
# if month in [12,1,2]:
#     print('Zima')
# elif month in [3,4,5]:
#     print('Vesna')
# elif month in [6,7,8]:
#     print('Leto')
# elif month in [9,10,11]:
#     print("Osen'")
# else:
#     if month or (month==0):
#         print('Попробуйте заново ввести номер месяца от 1 до 12')

''' letter = input('Введите латинскую букву: ')
if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
    print('Гласная буква')
elif letter == 'y':
    print('Это гласная и согласная буква')
else:
    print('Согласная буква;', type(letter))
    '''
# То же самое со списком:
# count, letters, vowels, consonants = 0, [], [], []
# while count <=9:
#         letters.append(input('Введите 10 латинских букв: '))
#         count +=1
#
# print('Весь список введённых букв - ', letters)
#
#
# for i in letters:
#         if i == 'a' or i == 'o' or i == 'e'\
#                 or i == 'u' or i == 'i':
#                 vowels.append(i)
#         elif i == 'y':
#                 consonants.append(i)
#                 vowels.append(i)
#         else:
#                 consonants.append(i)
# print('В списке есть гласные буквы - ', vowels,'\n'
# 'В списке есть согласные буквы - ', consonants, '\n')



# if letter == 'a' or letter == 'e' or letter == 'i' \
#         or letter == 'o' or letter == 'u':
#     print('Гласная буква')
# elif letter == 'y':
#     print('Это гласная и согласная буква')
# else:
#     print('Согласная буква;', type(letter))

# numb = int(input('Введите любое целое число: '))
#
# if numb % 2 == 0:
#         print(f'Вы ввели чётное число - {numb}')
# elif numb % 2!= 0:
#         print(f'Вы ввели нечётное число - {numb}')
# else:
#         print('Вы ввели что-то не то')


# heads = 35
# leg = 94
#
# # rab - rabbits
# # ph - phazans
#
# for rab in range(heads):
#     for ph in range(heads):
#         if (rab + ph) > heads or \
#                 (4 * rab + 2 * ph) > leg:
#             continue
#         if (rab + ph) == heads and \
#                 (4*rab + 2*ph) == leg:
#             print(rab, ' - кроликов;\n',
#       ph, '- фазанов')

'''Представим, что на вход нашей программы подается число. 
А мы хотим проверить, является ли оно целым, находится ли в определенном промежутке 
(например от 100 до 999 включительно), да еще и делится ли на 2 и 3 одновременно. 
Очень много условий. И такое случается в реальных проектах.

Решение в лоб — использовать вложенные условные операторы. 
Один if внутри другого if и так далее. Наверняка есть способ сделать это быстрее и эффективнее, 
но для начала попробуем написать решение в таком варианте, чтобы было с чем сравнить:

'''
a = int(input())

if a