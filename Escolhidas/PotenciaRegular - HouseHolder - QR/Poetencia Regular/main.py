import numpy as np
from functools import reduce



def produto_matriz_vetor(matriz, vetor):
    produto = []

    for i in range(0, len(matriz)):
        soma_linha = 0
        for j in range (0, len(matriz[i])):
            soma_linha += matriz[i][j] * vetor[j]
        produto.append(soma_linha)

    return produto

def produto_escalar(v1, v2):
    p_escalar = 0
    
    if len(v1) == len(v2):
        for i in range(len(v1)):
            p_escalar += v1[i] * v2[i]
    
    return p_escalar


def normalizar(vetor):
    c = np.sqrt(reduce(lambda acumulador, coordenada: acumulador + coordenada**2, vetor, 0))
    return list(map(lambda coordenada : coordenada/c, vetor))

def potencia_regular(A, v, error):
    autovalor_novo = 0
    v_k_novo = v
    erro = np.Infinity

    while (erro > error):
        autovalor_velho = autovalor_novo
        v_k_velho = v_k_novo
        autovetor_velho = normalizar(v_k_velho)
        v_k_novo = produto_matriz_vetor(A, autovetor_velho)
        autovalor_novo = produto_escalar(autovetor_velho, v_k_novo)
        erro = abs((autovalor_novo - autovalor_velho)/autovalor_novo)

    return (autovalor_novo, v_k_novo)




def main():
    A1 = [
        [5, 2, 1], 
        [2, 3, 1],
        [1, 1, 2]
    ]

    A2 = [
        [40, 8, 4, 2, 1], 
        [8, 30, 12, 6, 2,],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5]
    ]
    ##vetor arbitrário 
    v0 = [3, 3, 3]
    
    autovalor, autovetor = potencia_regular(A1, v0, 0.0001)

    print("Autovalor da matriz: {0}".format(autovalor))
    print("\nAutovetor da matriz: {0}".format(autovetor))


main()