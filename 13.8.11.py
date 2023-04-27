'''Напишите программу, которая на вход принимает
последовательность целых чисел,
и возвращает True, если все числа ненулевые,
и False, если хотя бы одно число равно 0.'''

# print('Введите 5 целых чисел.')
# nums = [3,-4,5]
# # while len(nums)<4+1:
# #     nums.append(int(input('')))
# print('Ваши введённые числа: ', nums)
#
# for i in nums:
#     if i == 5 and i > 0:
#         print('ok')
#     elif i < 0:
#             print('not OK')

# L = [2,3,-1,5,6]
# # print(L)
# L = list(map(int, input('input: ').split()))
# print(not any(L))
# # # print(all(L_1),type(all(L_1)))
# #
# # N = list(map(int, input().split()))
# # N = print()
# i = 2
# j = 2
# M = [[i*j for j in range(1,11)] for i in range(1,11)]
# for i in M:
#     print(i, end='\n')

# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# for i in T:
#     print(i,end=",\n")

# a = 3
# if a % 2 == 0:
#     print(bool(a))
# else:
#     print(not a)

# k = []
# for i in range(0,6):
#     if i % 2 == 0:
#         k.append(bool(i))
#     else:
#         k.append(not i)
# print(k)

# L = []
#
# for a in some_iter_obj:
#     if cond:
#         L.append(a)

# L = [int(input()) % 2 == 0 for a in range(5)]
# # L = [bool(int(input())) for i in range(5)]
# print(any(L) and not all(L))
L = [i for i in range(10)]
print(L)
M = [i for i in range(10,0,-1)]
print(M)
N = [L[i]*M[i] for i in range(10)]
# for i in range (10):
#     N.append(L[i] * M[i])
print(N)
# for a,b in zip(M,L):
#     print('a = ',a,', b = ', b, ', c = ')
Z = [a+b for a,b in zip(L,M)]





