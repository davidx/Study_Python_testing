x = int(input('Введите год - '))
def is_leap_year(x):
    return (x%400==0) or ((x%4==0) and (x%100!=0))
print(is_leap_year(x))

A = int(input('Введите первое число - '))
B = int(input('Введите второе число - '))

def are_both_odd(A, B):
    # return A%2!=0 and B%2!=0 - Также возможный вариант
    return A % 2 == 1 and B % 2 == 1
    print('Числа А и B нечетные')
print(are_both_odd(A,B))

'''Про функции'''

def get_wind_class(speed):
    # def - объявили функцию
    # get_wind_class - это мы так функцию назвали
    # speed - переменная , которую мы передали в функцию get_wind_class. Выходит, что это аргумент этой функции
