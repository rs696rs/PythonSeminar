'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

from math import sqrt
import math


xa = int(input('Введите координату A точки Х: ')) 
ya = int(input('Введите координату B точки X: ')) 
xb = int(input('Введите координату A точки Y: ')) 
yb = int(input('Введите координату B точки Y: ')) 

rast = float(math.sqrt(((xb-xa)**2) + ((yb-ya)**2)))

print('расстояние между ними', round(rast, 3))