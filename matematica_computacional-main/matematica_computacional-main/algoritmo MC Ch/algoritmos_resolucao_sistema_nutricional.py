# -*- coding: utf-8 -*-
"""
Solução do Problema Nutricional usando Fatoração LU com Pivotamento Parcial
============================================================================
Este programa resolve o sistema linear para determinar a quantidade de cada alimento que deve ser ingerida diariamente.

Autor: Seu Nome
Data: 2023-10-20
"""

def fatoracao_LU_pivot(A, b):
    """
    Resolve um sistema linear Ax = b utilizando a decomposição LU com pivotamento parcial.

    Parâmetros:
        A (list of list of floats): Matriz de coeficientes (n x n).
        b (list of floats): Vetor de constantes (tamanho n).

    Retorna:
        x (list of floats): Vetor solução x.

    Levanta:
        ValueError: Se a matriz não for quadrada ou se for singular.
    """
    n = len(A)
    for idx, row in enumerate(A):
        if len(row) != n:
            raise ValueError(f"A matriz deve ser quadrada. Linha {idx + 1} tem {len(row)} colunas.")

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    p = list(range(n))

    for k in range(n):
        pivot = abs(A[k][k])
        r = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > pivot:
                pivot = abs(A[i][k])
                r = i

        if pivot == 0:
            raise ValueError("A matriz A é singular e não pode ser decomposta em LU.")

        if r != k:
            A[k], A[r] = A[r], A[k]
            p[k], p[r] = p[r], p[k]

        for j in range(k, n):
            sum_U = 0.0
            for m in range(k):
                sum_U += L[k][m] * U[m][j]
            U[k][j] = A[k][j] - sum_U

        for i in range(k, n):
            if i == k:
                L[k][k] = 1.0
            else:
                sum_LU = 0.0
                for m in range(k):
                    sum_LU += L[i][m] * U[m][k]
                L[i][k] = (A[i][k] - sum_LU) / U[k][k]

    # Substituição para frente: Resolver Ly = Pb
    y = [0.0] * n
    for i in range(n):
        sum_Ly = 0.0
        for j in range(i):
            sum_Ly += L[i][j] * y[j]
        y[i] = b[p[i]] - sum_Ly

    # Substituição para trás: Resolver Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_Ux = 0.0
        for j in range(i + 1, n):
            sum_Ux += U[i][j] * x[j]
        x[i] = (y[i] - sum_Ux) / U[i][i]

    return x

def main():
    # Definindo a matriz de coeficientes A (nutrientes por grama de cada alimento)
    A = [
        # Arroz   Macarrão Pão  Batata  Tomate Maracujá Atum CarneBov Porco
        [1.28,    3.71,    3.0, 1.18,   2.75,  2.62,    0.04, 0.17,   0.16],   # Energia (kcal)
        [0.025,   0.1,     0.08,0.006,  0.011, 0.02,    0.257,0.299,  0.321],  # Proteína (g)
        [0.002,   0.013,   0.031,0.001, 0.002, 0.021,   0.009,0.163,  0.139],  # Lipídeos (g)
        [0.281,   0.779,   0.586,0.184, 0.031, 0.123,   0.0,  0.0,    0.0],    # Carboidrato (g)
        [0.04,    0.17,    0.16, 0.17,  0.05,  0.07,    0.3,  0.18,   0.03],   # Cálcio (mg)
        [0.001,   0.009,   0.01, 0.002, 0.002, 0.006,   0.013,0.028,  0.013],  # Ferro (mg)
        [0.01,    0.04,    0.17, 0.07,  0.05,  0.07,    0.51, 0.62,   0.62],   # Sódio (mg)
        [0.0002,  0.0015,  0.0013,0.0006,0.0004,0.0019, 0.0009,0.0008,0.0009], # Cobre (mg)
        [0.005,   0.008,   0.008,0.001, 0.001, 0.004,   0.004,0.067,  0.033]   # Zinco (mg)
    ]

    # Vetor b (exigências diárias)
    b = [5756, 401, 98.8, 782.8, 344, 27, 1824, 2.84, 35.8]

    # Nomes dos alimentos
    alimentos = [
        "Arroz",
        "Macarrão",
        "Pão",
        "Batata doce",
        "Tomate",
        "Maracujá",
        "Atum",
        "Carne bovina",
        "Porco, pernil"
    ]

    print("=== RESOLUÇÃO DO SISTEMA NUTRICIONAL ===")
    try:
        x = fatoracao_LU_pivot(A, b)
        print("\n=== QUANTIDADE DE CADA ALIMENTO (gramas) ===")
        for i in range(len(x)):
            print(f"{alimentos[i]}: {x[i]:.2f}g")
    except ValueError as ve:
        print(f"\nErro: {ve}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()