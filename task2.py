#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# N = int(input('введите значение N '))
# x = -N
# while x <= N:
#     print(x)
#     x += 1

N = int(input('введите значение N '))
lst = [i for i in range (-N, N+1)]
print(lst)