from math import exp


def division(): print("---------------------------------------------------")


def f(a_f: float, b_f: float, x_f: float): return (a_f / exp(x_f)) + b_f * x_f


def dihotomia(a0_dix: float, b0_dix: float, a_dix: float, b_dix: float, epsilon_dix: float, delta_dix: float):
    root: float
    x1: float
    y1: float
    l = 1  # длина отрезка [a,b]
    k = 1.0  # итерация
    while l >= epsilon_dix:
        x1 = (a_dix + b_dix) / 2.0 - delta_dix
        y1 = (a_dix + b_dix) / 2.0 + delta_dix
        if f(a0, b0, x1) <= f(a0, b0, y1):
            print("f(" + x1.__str__() + ") = " + f(a0, b0, x1).__str__())
            print("f(" + y1.__str__() + ") = " + f(a0, b0, y1).__str__())
            print("f(" + x1.__str__() + ") <= f(" + y1.__str__() + ")")
            b_dix = y1
            print("Новый интервал: [" + a_dix.__str__() + ", " + y1.__str__() + "]")
            division()

        else:
            a_dix = x1
            print("f(" + x1.__str__() + ") = " + f(a0, b0, x1).__str__())
            print("f(" + y1.__str__() + ") = " + f(a0, b0, y1).__str__())
            print("f(" + x1.__str__() + ") >= f(" + y1.__str__() + ")")
            print("Новый интервал: [" + x1.__str__() + ", " + b_dix.__str__() + "]")
            division()
        l = (b_dix - a_dix) / (2.0 ** k) + ((2.0 ** k - 1.0) / (2.0 ** (k - 1.0))) * delta_dix
        print("Длина нового интервала равна: l = " + l.__str__())

        if l < 2.0 * delta_dix:
            print("Длина интервала стала меньше 2*delta: " + l.__str__() + " < " + (2.0 * delta_dix).__str__())
            break
        k = k + 1.0

    root = (a_dix + b_dix) / 2.0
    return root


print("Активация программы...")
division()

print("Исходная функция: f(x) = a/exp(x) + bx")
a0 = float(input("Введите значение а: "))
b0 = float(input("Введите значение b: "))
print("Минимизация функции: f(x) = " + a0.__str__() + "/exp(x) + " + b0.__str__() + "*x")
division()

a = -100.0
b = 100.0
print("Рассматриваемый интервал: [" + a.__str__() + ", " + b.__str__() + "]")

epsilon = 0.001
while True:
    delta = float(input("Введите дельту на которую будем отступать(должна быть меньше epsilon/2): "))
    if delta <= epsilon / 2.0:
        print("Точка минимума равна " + dihotomia(a0, b0, a, b, epsilon, delta).__str__())
        break
    else:
        print("Значение дельты задано не верно.")
