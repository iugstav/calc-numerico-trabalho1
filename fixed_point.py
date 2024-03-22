from function import *
import numpy as np
import math

def fp_func(x):
    return np.sqrt(((0.2 * x) / np.power(math.e, x)) + (17 / 0.2))


def fixed_point():
    intervals = find_intervals()
    print(f"intervalos: {intervals}\n")

    max_iterations = 100
    epsilon = 1.0e-14

    for itv in intervals:
        i = 0
        # valor inicial
        x0: float = itv[0]
        # valor a ser atualizado pela função
        x1: float = 0

        print(f"intervalo {itv}")
        while np.abs(func(x0)) > epsilon and i < max_iterations:
            x1 = fp_func(x0)

            # verificação para saber se está nos conformes
            if np.abs(x0 - x1) < epsilon:
                break

            x0 = x1

            i += 1

        print(f"iteration: {i} | phi(x1): {x0} | f(x1): {func(x0)}")
        print("")


fixed_point()
