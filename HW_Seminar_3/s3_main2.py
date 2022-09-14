# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def sum_par_elem(list):
    new_list = []
    sum = 0
    for i in range((len(list)+1)//2):
        sum = list[i]*list[len(list)-1-i]
        new_list.append(sum)
    return new_list


list = [2, 3, 5, 9, 3, 4, 5, 6]
print(f"Список сумм парных элементов: {sum_par_elem(list)}")


