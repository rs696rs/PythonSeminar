# Задайте список из k чисел последовательности (1 + 1\k)^k 
# и выведите на экран их сумму.

k = int(input('Введите число K: '))
def spisok(k):
    list = []
    elem = 0
    for i in range(1,k+1):
        elem += round((1+1/k)**k,2)
        list.append(elem)
    return list
sp_num = spisok(k)
print(f"Полученный список: {sp_num} \nПроизведение элементов данного списка: {sum(sp_num)}")
