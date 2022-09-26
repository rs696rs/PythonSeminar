# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


# def diff_value(list):
#     min_elem = 1
#     max_elem = 0
#     diff_value = 0
#     for i in list:
#         if (i - int(i)) <= min_elem:
#             min_elem = i - int(i)
#         if (i - int(i)) >= max_elem:
#             max_elem = i - int(i)
#     diff_value = max_elem - min_elem
#     return round(diff_value, 3)



# list = [1.1, 1.2, 3.1, 10.01, 23.4]
# print(f"Разница между максимальным и минимальным значением дробной части элементов: {diff_value(list)}")

# new version:

spisok = [1.1, 1.2, 3.1, 10.01]
lst = ['.'+str(i).split('.')[1] for i in spisok]
max = max(list(map(float,lst)))
min = min(list(map(float,lst)))
print(max-min)