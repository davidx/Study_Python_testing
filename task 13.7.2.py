'''

Гипотеза Сиракуз заключается в том, что любое натуральное число можно свести к 1,
если повторять над ним следующие действия:

если число четное, то разделить его пополам,
если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.
'''

# n = int(input('Введите число: '))
#
# while True:
#     if n % 2 == 0:
#         n = n // 2
#         if n == 1:
#             break
#     else:
#         n = (n * 3 + 1) // 2
#         if n == 1:
#             break
# print('End of loop', n)

# n = int(input(''))
#
# while n > 1:
#     if n == 1:
#         break
#     if n % 2 == 0:
#         n //= 2
#     else:
#         n = (n * 3 + 1) // 2
# print(n)


# n = int(input('Введите число: '))
# while True:
#     if n % 3 == 0:
#         n = n // 3
#
#     #     if n == 1:
#     #         break
#     # n += 1
#     # # else:
#     # #     break
#     print('Итоговое последнее число: ', n)