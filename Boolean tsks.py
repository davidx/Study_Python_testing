# print(not not not not True)
# def is_leap_year(x):
#     return (x%400==0) or ((x%4==0) and (x%100!=0))
# без остатка на 400
# безостатка на 4

# Вариант через переменную.
number = int(input('Type a bunch of numbers: '))
number_list = list(map(int, str(number)))

print(5 in number_list and 7 in number_list)

# Вариант с быстрым решением, без переменной и доп. маппинга

number = int(input('Put some nubers in here, please: '))
print('5' in str(number) and '7' in str(number))