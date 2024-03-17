import math
from decimal import getcontext
from typing import List, Tuple

# aumenta a a precisão de float
getcontext().prec = 30

# type alias pra representar a lista de intervalos das funções
Intervals = List[Tuple[int, int]]

def func(x: float) -> float:
    """função do exercício

    Returns:
        imagem da função
    """
    return (x / pow(math.e, x)) - 0.2 * pow(x, 2) + 17

def find_intervals() -> Intervals:
    """acha os intervalos e armazena no type alias Intervals

    Returns:
        todos os intervalos que podem conter uma raiz da equação
    """
    # a variável abaixo usa list comprehensions [https://pythonacademy.com.br/blog/list-comprehensions-no-python]
    # equivalente a:
    # for x in range(-200, 200):
    #     if func(x) * func(x+1) < 0:
    #         interval.append((x, x+1))
    interval: Intervals = [
        (x, x + 1) for x in range(-200, 200) if func(x) * func(x + 1) < 0
    ]

    return interval


def bisection_method():
    """o próprio método da bissecção
    """
    intervals = find_intervals()
    print(f"intervalos: {intervals}\n")

    inferior_limit: float
    superior_limit: float
    aproximation: float
    epsilon: float = 1.0e-14
    max_iterations: int = 400

    for itv in intervals:
        print(f"intervalo atual {itv}")

        inferior_limit = itv[0]
        superior_limit = itv[1]
        aproximation = (inferior_limit + superior_limit) / 2.0

        idx: int = 0
        while math.fabs(func(aproximation)) > epsilon and idx < max_iterations:
            if func(inferior_limit) * func(aproximation) < 0:
                superior_limit = aproximation
            else:
                inferior_limit = aproximation

            aproximation = (inferior_limit + superior_limit) / 2.0
            idx += 1

        print(f"tolerancia utilizada: {epsilon}")
        print(f"raiz encontrada {aproximation} | número de iterações: {idx}\n")


bisection_method()
