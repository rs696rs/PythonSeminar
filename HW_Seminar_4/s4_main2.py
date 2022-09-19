# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

def prime_factors(a):
    i = 2  
    factors_list = []
    while i <= a:
        if a % i == 0:
            factors_list.append(i)
            a //= i
            i = 2
        else:
            i += 1
    return factors_list


num = int(input("Введите натуральное число: \n"))
print(f"Множители числа {num}: {prime_factors(num)}")
