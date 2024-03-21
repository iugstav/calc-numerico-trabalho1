import math
from function import *


def avg(inf: float, sup: float, f_inf: float, f_sup: float):
    """Calcula a média ponderada

    Parâmetros:
        inf: float : o limite inferior do intervalo
        sup: float : o limite superior do intervalo
        f_inf: float : a função dada aplicada em `inf`
        f_sup: float : a função dada aplicada em `sup`

    Retorna:
        A média ponderada entre `inf` e `sup`
    """
    return ((inf * math.fabs(f_sup)) + (sup * math.fabs(f_inf))) / (
        math.fabs(f_sup) + math.fabs(f_inf)
    )


def fake_pos_method():
    """ método da falsa posição
    """
    # chamada da função que acha os intervalos e
    # atribuição do retorno dela à variável 'intervals'
    intervals = find_intervals()
    print(f"intervalos: {intervals}\n")

    # definição das variáveis a serem utilizadas no método da bisseção
    inferior_limit: float
    superior_limit: float
    weighted_avg: float

    # epsilon é a precisão desejada
    epsilon: float = 1.0e-14
    max_iterations: int = 5

    idx: int
    # realiza o algoritmo abaixo para cada intervalo presente em 'intervals'
    for itv in intervals:
        print(f"intervalo atual {itv}")

        inferior_limit = itv[0]
        superior_limit = itv[1]
        weighted_avg = avg(inferior_limit, superior_limit, func(inferior_limit), func(superior_limit))

        idx = 0
        while math.fabs(func(weighted_avg)) > epsilon and idx < max_iterations:
            if func(inferior_limit) * func(weighted_avg) < 0:
                superior_limit = weighted_avg
            else:
                inferior_limit = weighted_avg

            weighted_avg = avg(inferior_limit, superior_limit, func(inferior_limit), func(superior_limit))
            idx += 1

        print(f"tolerancia utilizada: {epsilon}")
        print(f"raiz encontrada {weighted_avg} | número de iterações: {idx}\n")


fake_pos_method()
