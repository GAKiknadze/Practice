'''
Задача №2.
Известны: координаты (X,Y) двух точек.
Найти: k и b из уравнение прямой(y=k*x+b).
'''
try:
    x1,y1 = input('Введите координаты первой точки в формате(X,Y):').split()
    x2,y2 = input('Введите координаты второй точки в формате(X,Y):').split()
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    k = (y1-y2)/(x1-x2)
    b = k*x1-y1
    print('Уравнение прямой для точек A1({},{}) и A2({},{}) имеет вид y={}*x+{}'.format(x1,y1,x2,y2,k,b))
except ValueError:
    print('Ошибка ввода')