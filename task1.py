# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму нечетных элементов списка.
# import random
# N = int(input('введите число N: '))
# list = []
# for i in range(N):
#     list.append(random.randint(-10, 10))

# def Summ(list):
#     S = 0
#     for i in range (0, len(list)):
#         if list[i]%2 != 0:
#             S += list[i]
#     return S
    
# print(f"{list} -> сумма нечетных элементов: {Summ(list)}")

from random import randint

N = int(input('введите число N: '))
lst1 = [randint(-10, 10) for i in range(N)]
lst2 = [i for i in lst1 if i%2 != 0]

print(f"{lst1} -> сумма нечетных элементов: {sum(lst2)}")