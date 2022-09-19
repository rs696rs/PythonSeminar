# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def not_repeat_elements(list):
    new_list = []
    for i in list:
        if list.count(i) == 1:
            new_list.append(i)
    return new_list


old_list = [1, 1, 1, 2, 3, 1, 4, 7, 5, 5, 5, 5, 6]
print(f"Исходный список: {old_list}\nCписок неповторяющихся элементов: {not_repeat_elements(old_list)}")
