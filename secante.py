from function import *
from decimal import Decimal, getcontext

getcontext().prec = 30


def secante(intervalo, epsilon, max_it=100):
    a: Decimal = Decimal(intervalo[0])
    b: Decimal = Decimal(intervalo[1])
    aproximation: Decimal = Decimal(0.0)

    validation = (func(b) - func(a)) / (b - a) == 0
    if validation:
        print("Não é possível garantir a existência de raízes no intervalo fornecido.")
        return None, 0

    i = 0
    while abs(func(aproximation)) > epsilon and i < max_it:
        aproximation = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if abs(aproximation - b) < epsilon:
            return aproximation, i

        a = b
        b = aproximation
        i += 1

    return aproximation, i


intervalos: list[tuple[int, int]] = [(-3, -2), (9, 10)]
epsilon = 10e-20
max_it = 100

for itv in intervalos:
    print(f"intervalo atual {itv}")

    raiz, iteracoes = secante(itv, epsilon, max_it)

    if raiz == None:
        print("deu ruim hein")
        break

    print(f"tolerancia utilizada: {epsilon}")
    print(f"raiz encontrada {raiz} | número de iterações: {iteracoes}\n")
    print("{:.30f}".format(func(raiz)))
