# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def spisok_kjof(n):
    list_koof = [random.randint(1, 100)]    
    for i in range(1, n ):
        list_koof.append(random.randint(0, 100))
    return list_koof

def polynomial(list):  
    x_str = ''
    if len(list) < 1:
        x_str = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                x_str += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    x_str += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                x_str += f'{list[i]}x'
                if list[i+1] != 0:
                     x_str += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                x_str += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                x_str += ' = 0'
    return x_str

k = int(input('Введите число k: '))
spisok = spisok_kjof(k)
spisok.sort(reverse=True)
print(f"Список коэффициентов: {spisok}")
with open('sem_4_task_4_polym.txt', 'w') as data:
    data.write(polynomial(spisok))
