import math


def square(side):
    return side * side


side = float(input("Введите размер стороны квадрата: "))

side = math.ceil(side)

print(f"Площадь квадрата со стороной {side} равна {square(side)}")
