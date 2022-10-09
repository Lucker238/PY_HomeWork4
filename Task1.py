# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

def show_me_pi():
    check = True
    while check:
        try:
            numbers = int(input('Введитечисло знаков после запятой: '))
            check = False
        except ValueError:
            print('Нужно ввести число!')
    return round(math.pi, numbers)

print(show_me_pi())