# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo(a):
    list = [1, 1]
    for i in range(2, a+1):
        list.append(list[-1]+list[-2])
    return list


def nega_fibo(a):
    list = [0, 1]
    for i in range(1, a):
        list.append(list[i-1]-list[i])
    list.reverse()
    return list


a = int(input())
result = nega_fibo(a) + fibo(a)
print(str(result))
