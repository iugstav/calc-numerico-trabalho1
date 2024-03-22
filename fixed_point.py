from function import *
import numpy as np
import math

def fp_func(x):
    return np.sqrt(((0.2 * x) / np.power(math.e, x)) + (17 / 0.2))


def fixed_point(a, epsilon, max_it = 100):
    i = 0
    # valor inicial
    x0: float = 0
    # valor a ser atualizado pela função
    x1: float = 0

    while i < max_it:
        x1 = fp_func(x0)

        # verificação para saber se está nos conformes
        if np.abs(x0 - x1) < epsilon or np.abs(func(x1) < epsilon):
            return x1, i

        x0 = x1
        i += 1

    return None, i


intervalos = [(-3, -2), (9, 10)]
epsilon = 1.0e-15
max_iter = 100

# encontrando as raízes de cada intervalo
for intervalo in intervalos:
    print(f"Intervalo: {intervalo}")

    a, _ = intervalo
    raiz, iteracoes = fixed_point(a, epsilon, max_iter)

    if raiz is not None:
        print(f'Raiz encontrada: {raiz}')
        print(f'Número de iterações: {iteracoes}')
    else:
        print("Não foi possível encontrar a raiz com a precisão especificada.")
