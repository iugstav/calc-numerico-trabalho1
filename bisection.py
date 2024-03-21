import math
from function import *
from decimal import getcontext

# aumenta a a precisão de float
getcontext().prec = 30


def bisection_method():
    """o próprio método da bissecção"""

    # chamada da função que acha os intervalos e
    # atribuição do retorno dela à variável 'intervals'
    intervals = find_intervals()
    print(f"intervalos: {intervals}\n")

    # definição das variáveis a serem utilizadas no método da bisseção
    inferior_limit: float
    superior_limit: float
    aproximation: float

    # epsilon é a precisão desejada
    epsilon: float = 1.0e-14
    max_iterations: int = 5

    idx: int
    # realiza o algoritmo abaixo para cada intervalo presente em 'intervals'
    for itv in intervals:
        print(f"intervalo atual {itv}")

        inferior_limit = itv[0]
        superior_limit = itv[1]
        aproximation = (inferior_limit + superior_limit) / 2.0

        idx = 0
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
