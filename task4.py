#Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random
# N = int(input('введите число N: '))
# list = []
# for i in range(N):
#     list.append(random.randint(-10, 10))
# print(f"Исходный список: {list}")
# print()

# def New_list(list):
#     new_list = []
#     for i in range ((N+1)//2):
#         new_list.append(list[i]*list[(N-1-i)])
#     return new_list

# print(f"Новый список с произведениями пар чисел: {New_list(list)}")

from random import randint
N = int(input('введите число N: '))
lst1 = [randint(-10, 10) for i in range(N)]
print(f"Исходный список: {lst1}")
print()

lst2 = [i for i in range ((N+1)//2)]
lst3 = list(map(lambda i: lst1[i]*lst1[(N-1-i)], lst2))

print(f"Новый список с произведениями пар чисел: {lst3}")