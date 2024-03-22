from typing import List, Tuple
import numpy as np

# type alias pra representar a lista de intervalos das funções
Intervals = List[Tuple[int, int]]


def func(x: float) -> float:
    """função do exercício

    Returns:
        imagem da função
    """
    return (x / np.exp(x)) - (0.2 * x**2) + 17


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
