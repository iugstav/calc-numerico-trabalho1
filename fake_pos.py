import math
from function import *


def avg(inf, sup, f_inf, f_sup):
    """Calcula a média ponderada a ser utilizada no método da falsa posição

    Parâmetros
    ---
    inf: float
        o limite inferior do intervalo
    sup: float
        o limite superior do intervalo
    f_inf: float
        a função dada aplicada em `inf`
    f_sup: float
        a função dada aplicada em `sup`

    Retorna
    ---
    float
        A média ponderada entre `inf` e `sup`
    """

    fabs = math.fabs
    return (inf * fabs(f_sup) + sup * fabs(f_inf)) / (fabs(f_sup) + fabs(f_inf))


def fake_pos_method(intervalo, epsilon, max_it=100):
    """Executa o método da falsa posição

    Parâmetros
    ---
    intervalo: tuple[int, int]
        O intervalo inicial a ser particionado em que a raiz pode ser encontrada
    epsilon : float
        A margem de erro apropriada para a achar o zero da função
    max_it : int, optional
        O número máximo de iterações a serem rodadas pelo método do ponto fixo (padrão é 100)

    Retorna
    ---
    float | None
        A raiz da função, se existir no intervalo
    int
        O número de iterações necessárias para achar a raiz
    """

    # definição das variáveis a serem utilizadas no método da bisseção
    inf = intervalo[0]
    sup = intervalo[1]
    weighted_avg = 0.0

    if func(inf) * func(sup) > 0:
        print("Não é possível garantir a existência de raízes no intervalo fornecido.")
        return None, 0

    i = 0
    while i < max_it:
        weighted_avg = avg(inf, sup, func(inf), func(sup))

        if abs(func(weighted_avg)) < epsilon:
            return weighted_avg, i

        if func(inf) * func(weighted_avg) < 0:
            sup = weighted_avg
        else:
            inf = weighted_avg

        i += 1

    return weighted_avg, i


intervalos: list[tuple[int, int]] = [(-3, -2), (9, 10)]
epsilon = 1.0e-14
max_it = 100

for itv in intervalos:
    print(f"intervalo atual {itv}")

    raiz, iteracoes = fake_pos_method(itv, epsilon, max_it)

    if raiz == None:
        print("deu ruim hein")
        break

    print(f"tolerancia utilizada: {epsilon}")
    print(f"raiz encontrada {raiz} | número de iterações: {iteracoes}\n")
