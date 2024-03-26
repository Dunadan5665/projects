from math import sqrt

a = float(input('Введите коэффицент a: '))
b = float(input('Введите коэффицент b: '))
c = float(input('Введите коэффицент c: '))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)

    print(f'Корни квадратного уравнения: {round(x1, 2)} и {round(x2, 2)}')

elif discriminant == 0:
    x = -b / (2 * a)
    print(f'Корень квадратного уравнения: {round(x, 2)}')

else:
    print('Квадратное уравнение не имеет корней')
