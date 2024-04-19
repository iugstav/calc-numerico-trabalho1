import math
from decimal import Decimal, getcontext

getcontext().prec = 30

# f(x) do exercício
def f(x: Decimal):
    return x / x.exp() - (Decimal(0.2) * x**2) + 17

# derivada da função
def df(x: Decimal):
    return (x.exp() - x * x.exp() - Decimal(0.4) * x * Decimal(2*x).exp()) / Decimal(2*x).exp()

# Método de Newton-Raphson
def newton_raphson(x0, epsilon, max_iter):
    x: Decimal = Decimal(x0)
    iteracoes = 0

    for i in range(max_iter):
        x_new = x - f(x) / df(x)

        if abs(x_new - x) < epsilon:
            return x_new, iteracoes

        x = x_new
        iteracoes += 1
    return None, iteracoes

# Intervalos e precisão
intervalos = [(-3, -2), (9, 10)]
epsilon = 1.0e-20
max_iter = 100

# Iterações para cada intervalo
for intervalo in intervalos:
    print(f"Iterações para o intervalo {intervalo}:")

    raiz, iteracoes = newton_raphson(intervalo[0], epsilon, max_iter)

    print(f"Raiz encontrada: {raiz}")
    print(f'Número de iterações: {iteracoes}')
