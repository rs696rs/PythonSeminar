# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_system(num):
    binary_symbol = ''
    while num != 0:
        binary_symbol = str(num % 2) + binary_symbol
        num //= 2
    return binary_symbol


a = int(input())
print(f'Двоичное число: {binary_system(a)}')
print(f"Читерский способ: {bin(a)}")
