#Найти корни квадратного уравнения Ax**2 + Bx + C = 0

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

d = b**2 - 4 * a * c # дискриминант

if d > 0:
    x1 = -b + (d**0.5)/(2 * a)
    x2 = -b + (-d**0.5)/(2 * a)
    print(f'первое число - {x1}, второе число -  {x2}')
elif d == 0:
    x1 = -b/(2 * a)
    print(f'первое число - {x1}')
else: # d < 0
    print('Уравнение не имеет решения')
