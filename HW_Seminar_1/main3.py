'''
Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).
'''

a = int(input('Введите номер координатной четверти: ')) 

if a == 1:
    print('X от 0 до +∞ Y от 0 до +∞')
if a == 2:
    print('X от 0 до -∞ Y от 0 до +∞')
if a == 3:
    print('X от 0 до -∞ Y от 0 до -∞')
if a == 4:
    print('X от 0 до +∞ Y от 0 до -∞')        
else :
    print('Координатных четвертей всего 4!')  