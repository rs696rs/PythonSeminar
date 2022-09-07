'''
Напишите программу для. проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

x = int(input('Введите Х: ')) 
y = int(input('Введите Y: ')) 
z = int(input('Введите Z: '))

def proverka_istini(a,b,c):
    result = not (a or b or c) == (not a and not b and not c)
    return result

if proverka_istini(x, y, z) == True:
    print('Утверждение истинно!')
else:
    print('Утверждение не истинно!')
