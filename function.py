from typing import List, Tuple
from decimal import Decimal
import numpy as np

# type alias pra representar a lista de intervalos das funções
Intervals = List[Tuple[int, int]]


def func(x: Decimal) -> Decimal:
    """função do exercício

    Retorna
    ---
    Decimal
        a imagem da função
    """
    exponential = Decimal(np.exp(float(x)))
    return Decimal((x / exponential) - Decimal(0.2) * (x**2) + 17)


def find_intervals() -> Intervals:
    """acha os intervalos que contém a raíz da função

    Retorna
    ---
    Intervals = List[Tuple[int, int]]
        Os intervalos de raízes
    """

    # a variável abaixo usa list comprehensions [https://pythonacademy.com.br/blog/list-comprehensions-no-python]
    # equivalente a:
    # interval = []
    # for x in range(-200, 200):
    #     if func(x) * func(x+1) < 0:
    #         interval.append((x, x+1))
    interval: Intervals = [
        (x, x + 1) for x in range(-200, 200) if func(Decimal(x)) * func(Decimal(x + 1)) < 0
    ]

    return interval
