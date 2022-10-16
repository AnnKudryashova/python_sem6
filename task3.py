#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('введите число n: '))
# def Summ(n):
#     sum  = 0
#     for i in range (1, n + 1):
#         result = float((1+1/i)**i)
#         sum += result
#     return sum
# print(f'Сумма чисел заданной последовательности {round(Summ(n),2)}')


n = int(input('введите число n: '))
lst = [i for i in range(1, n+1)]
result = list(map(lambda i: (1+1/i)**i, lst))
print(f'Сумма чисел заданной последовательности {round(sum(result),2)}')