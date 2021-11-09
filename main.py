from math import exp, sqrt


def division(): print("---------------------------------------------------")


def f(x_f: float): return (a0 / exp(x_f)) + b0 * x_f


def zolotsech(a_zol: float, b_zol: float, epsilon_zol: float):
    root: float  # искомое число(точка минимума)
    delta_0: float
    delta_1: float
    delta_2: float
    x0: float
    y0: float

    x1: float
    y1: float

    # Производим вычисления для k = 0
    delta_0 = b_zol - a_zol
    delta_1 = (sqrt(5.0)-1.0)/2.0 * delta_0
    delta_2 = delta_0 - delta_1
    x0 = a_zol + delta_2
    y0 = b_zol - delta_2

    fx0: float = f(x0)
    fy0: float = f(y0)

    k: float = 1.0  # Итерация
    while True:
        division()
        print("Итерация номер " + k.__str__())
        if f(x0) <= f(y0):
            b_zol = y0
            y1 = x0
            x1 = a_zol + delta_2
            print("Новый интервал: [" + a_zol.__str__() + ", " + b_zol.__str__() + "]")
            print("x_k = " + x1.__str__())
            print("y_k = " + y1.__str__())
            print("delta_k = " + delta_1.__str__())
            if x1 < y1:
                if delta_1 <= epsilon_zol:
                    print("Так как delta_k <= epsilon процесс завершён.")
                    root = (x1 + y1)/2.0
                    break
            k += 1
            delta_0 = delta_2
            delta_2 = delta_1 - delta_2
            delta_1 = delta_0
            y0 = y1
            x0 = x1
        else:
            a_zol = x0
            x1 = y0
            y1 = b_zol - delta_2
            print("Новый интервал: [" + a_zol.__str__() + ", " + b_zol.__str__() + "]")
            print("x_k = " + x1.__str__())
            print("y_k = " + y1.__str__())
            print("delta_k = " + delta_1.__str__())
            if x1 < y1:
                if delta_1 <= epsilon_zol:
                    print("Так как delta_k <= epsilon процесс завершён.")
                    root = (x1 + y1) / 2.0
                    break
            k += 1
            delta_0 = delta_2
            delta_2 = delta_1 - delta_2
            delta_1 = delta_0
            y0 = y1
            x0 = x1
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

epsilon = 0.0001

print("Точка минимума равна " + zolotsech(a, b, epsilon).__str__())

