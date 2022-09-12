# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = int(input('Введите N: '))
def spisok(k):
    list = []
    elem = 0
    for i in range(-n,n+1):
        elem = i
        list.append(elem)
    return list
list_n = spisok(n)
print(list_n)

list_input = input("Введите позиции элементов: ").split(' ')

def clear_int_list (list):    # список из string в int элементы
    cler_list=[]
    elem=0
    for i in list:
        elem = int(i)
        cler_list.append(elem)
    return cler_list

clear_list = clear_int_list(list_input)

def sum_elem(list_1, list_2):
    list_1_len = len(list_1)
    list_2_len = len(list_2)
    count = 0
    sum = 1
    while count<list_2_len:
        for i in range(list_1_len+1):
            for j in list_2:
                sum *= list_1[j]
                count += 1
            return sum

print(f"Произведение выбраных элементов {sum_elem(list_n, clear_list)}")
