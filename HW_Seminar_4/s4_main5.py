# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


file_1 = 'polym_1.txt'
file_2 = 'polym_2.txt'
with open(str(file_1), 'r') as data:
    pol = data.read()
with open(str(file_2), 'r') as data:
    pol_2 = data.read()
print(pol)
print(pol_2)


