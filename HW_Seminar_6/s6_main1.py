# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# number = input('Введите вещественное число: ')
# sum = 0
# # for i in number:
# #     if i != '.' and i != ',':
# #         sum += int(i)
# print('Сумма цифр данного числа равна:',sum)


# New vervion:
number = input('Введите вещественное число: ').split('.')
number = list(map(int,number[1]))
print(sum(number))