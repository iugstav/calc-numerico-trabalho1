import math
from function import *


def bisection_method(intervalo, epsilon, max_it=100):
    """Executa o método da bisseção

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
    inferior_limit: float = intervalo[0]
    superior_limit: float = intervalo[1]
    aproximation: float = (superior_limit + inferior_limit) / 2.0

    # validação da existência da(s) raiz(es) no intervalo
    if func(inferior_limit) * func(superior_limit) > 0:
        print("Não é possível garantir a existência de raízes no intervalo fornecido.")
        return None, 0

    # contagem de iterações
    i = 0
    while math.fabs(func(aproximation)) > epsilon and i < max_it:
        if func(inferior_limit) * func(aproximation) < 0:
            superior_limit = aproximation
        else:
            inferior_limit = aproximation

        aproximation = (superior_limit + inferior_limit) / 2.0

        i += 1

    return aproximation, i


# definição dos valores a serem utilizados na invocação da função
intervalos: list[tuple[int, int]] = [(-3, -2), (9, 10)]
epsilon = 1.0e-14
max_it = 500

for itv in intervalos:
    print(f"intervalo atual {itv}")

    raiz, iteracoes = bisection_method(itv, epsilon, max_it)

    if raiz == None:
        print("deu ruim hein")
        break

    print(f"tolerancia utilizada: {epsilon}")
    print(f"raiz encontrada {raiz} | número de iterações: {iteracoes}")
