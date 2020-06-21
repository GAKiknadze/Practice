'''
Задача №1.
Известны: катеты прямоугольного треугольника.
Найти: гипотенузу, периметр и площадь.
'''
import math
try:
    k1,k2 = input('Введите два катета:').split()
    k1 = float(k1)
    k2 = float(k2)
    if k1>0 and k2>0:
        g = math.hypot(k1,k2)
        print('''Гипотенуза: {}
Периметр: {}
Площадь: {}'''.format(g, k1 + k2 + g, (k1 * k2) / 2))
    else:
        1/0
except (ValueError,ZeroDivisionError):
    print('Ошибка ввода')
