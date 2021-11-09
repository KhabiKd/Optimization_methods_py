from math import exp, sqrt


def division(): print("---------------------------------------------------")


def f(x1_f: float, x2_f: float): return 100 * (x2_f - x1_f * x1_f) + (1 - x1_f) * (1 - x1_f)


def difmnog(x1_dif: float, y1_dif: float, x2_dif: float, y2_dif: float, x3_dif: float, y3_dif: float):
    n: float = 2
    alpha: float = 1.0
    betta: float = 0.5
    gamma: float = 2.0
    epsilon: float = 0.001
    k: float = 0.0
    root: float

    xl: float  # Наилучший
    xh: float  # Наихудший
    xs: float



    return root


print("Активация программы...")
division()

print("Исходная функция: f(x, y) = 100(y - x^2)^2 + (1 - x)^2")
division()

print("Введите координаты первой точки: ")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
print("(" + x1.__str__() + ", " + y1.__str__() + ")")
division()

print("Введите координаты второй точки: ")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
print("(" + x2.__str__() + ", " + y2.__str__() + ")")
division()

print("Введите координаты третьей точки: ")
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))
print("(" + x3.__str__() + ", " + y3.__str__() + ")")
division()

print("Точка минимума равна " + difmnog(x1, y1, x2, y2, x3, y3).__str__())
