'''
Задача №6.
Известно: количество данных в байтах.
Найти: килобайтах и мегабайтах
'''
try:
    m = float(input('Введите количество байтов: '))
    print('Килобайт:',m*0.001)
    print('Мегабайт:',m*0.000001)
except ValueError:
    print('Ошибка ввода')