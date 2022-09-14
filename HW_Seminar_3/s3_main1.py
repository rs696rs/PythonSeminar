# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

def sum_nechet(list):
    sum = 0
    count = 0
    while count < len(list):
        for i in range(len(list)):
            if i % 2 != 0:
                sum = sum+list[i]
        return sum

list = [2, 3, 5, 9, 3, 4, 5, 6]
print(sum_nechet(list))
