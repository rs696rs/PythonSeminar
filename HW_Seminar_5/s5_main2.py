# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


from random import randint


def input_сandy(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def interim_result_print(name, candy, counter_candy, value_candy):
    print(
        f"Игрок {name} взял {candy} конфет, теперь у него {counter_candy}. Осталось {value_candy} конфет.")


player_1 = input("Имя 1 игрока: ")
player_2 = input("Имя 2 игрока: ")
value_candy = int(input("Введите количество конфет: "))
flag = randint(0, 2)
if flag:
    print(f"Первым ходит {player_1}")
else:
    print(f"Первым ходит {player_2}")


count_сandy_1 = 0
count_сandy_2 = 0

while value_candy > 28:
    if flag:
        candy = input_сandy(player_1)
        count_сandy_1 += candy
        value_candy -= candy
        flag = False
        interim_result_print(player_1, candy, count_сandy_1, value_candy)
    else:
        candy = input_сandy(player_2)
        count_сandy_2 += candy
        value_candy -= candy
        flag = True
        interim_result_print(player_2, candy, count_сandy_2, value_candy)

if flag:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")
