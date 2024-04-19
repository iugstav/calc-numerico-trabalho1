import numpy as np
import math
from function import *


# função do primeiro intervalo
def fp_func_intervalo_1(x: Decimal) -> Decimal:
    """o logaritmo natural de ((0.2 * x^2 * e^x - x) menos o logaritmo natural de 17"""

    return Decimal(math.log(Decimal(0.2) * Decimal(math.pow(float(x), 2)) * x.exp() - x) - math.log(17))


# função do segundo intervalo
def fp_func_intervalo_2(x: Decimal) -> Decimal:
    """a raiz quadrada de (x dividido por (0.2 * e^x) + 17 dividido por 0.2)"""

    return Decimal(math.sqrt((x / (Decimal(0.2) * x.exp())) + 85))


# array pra fazer a chamada de funções dentro do loop.
# Em vez de armazenar a invocação da função, eu armazeno
# a função em si pra poder invocá-la depois.
functions = [fp_func_intervalo_1, fp_func_intervalo_2]


# função do método do ponto fixo.
def fixed_point(a, epsilon, fixed_point_function, max_it=100):
    """Executa o método do ponto fixo

    Parâmetros
    ---
    a : int
        O valor inicial para começar a iteração. Nesse caso, o valor mínimo do intervalo
    epsilon : float
        A margem de erro apropriada para a achar o zero da função
    fixed_point_function : Callable[[Decimal], Decimal]
        a função especificada para cada caso de uso
    max_it : int, optional
        O número máximo de iterações a serem rodadas pelo método do ponto fixo (padrão é 100)

    Retorna
    ---
    float
        A raiz da função
    int
        O número de iterações necessárias para achar a raiz
    """

    # valor inicial
    x0: Decimal = Decimal(a)

    # valor a ser atualizado pela função
    x1: Decimal = Decimal(0.0)

    # contagem de iterações
    i = 0
    while i < max_it:
        x1 = fixed_point_function(x0)

        # verificação para saber se está nos conformes
        if math.fabs(x0 - x1) < epsilon or math.fabs(func(Decimal(x1))) < epsilon:
            return x1, i

        x0 = x1
        i += 1

    return x1, i


intervalos: list[tuple[int, int]] = [(-3, -2), (9, 10)]
epsilon = 1.0e-20
max_iter = 500

# encontrando as raízes de cada intervalo
for i in range(len(intervalos)):
    print(f"Intervalo: {intervalos[i]}")

    a, b = intervalos[i]
    raiz, iteracoes = fixed_point(a, epsilon, functions[i], max_iter)

    print(f"tolerancia utilizada: {epsilon}")
    print(f"raiz encontrada {raiz} | número de iterações: {iteracoes}")
    print(func(raiz))

    print("\n")
