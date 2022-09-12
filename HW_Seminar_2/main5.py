# Реализуйте алгоритм перемешивания списка.

import random
spisok = ['qwe', 'rty', 'uio', 'asd', 123, 456, 789]
print(f"Исходный список {spisok}") 
random.shuffle(spisok)
print(f"Новый список {spisok}") 