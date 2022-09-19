# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def sum_list(list_1,list_2):
    sum_list=[]
    for i in range(0,len(list_1)):
        sum_list.append(list_1[i]+list_2[i])
    return sum_list

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

file_1 = 'polym_1.txt'
file_2 = 'polym_2.txt'
with open(str(file_1), 'r') as data:
    sum_pol_1 = data.read()
with open(str(file_2), 'r') as data:
    sum_pol_2 = data.read()
print(f"Первый многочлен: {sum_pol_1}")
print(f"Второй многочлен: {sum_pol_2}")

chars = ['x2','^','+','=','0']
sum_pol_1 = sum_pol_1.translate(str.maketrans('','',''.join(chars)))
sum_pol_2 = sum_pol_2.translate(str.maketrans('','',''.join(chars)))

sum_pol_1 = list(map(int,sum_pol_1.split()))
sum_pol_2 = list(map(int,sum_pol_2.split()))

sum_2list_pol = sum_list(sum_pol_1,sum_pol_2)

with open('sum_2_polyn.txt', 'w') as data:
    data.write(polynomial(sum_2list_pol))
