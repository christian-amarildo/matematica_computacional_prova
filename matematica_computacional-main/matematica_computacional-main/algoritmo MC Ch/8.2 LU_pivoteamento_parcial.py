# -*- coding: utf-8 -*-
"""
Calculadora de Sistemas Lineares pelo Método de Fatoração LU com Pivotamento Parcial
===================================================================================

Este programa resolve sistemas lineares da forma Ax = b utilizando o Método de Fatoração LU
com Pivotamento Parcial. O método consiste em decompor a matriz de coeficientes A em duas matrizes
triangulares: L (Triangular Inferior) e U (Triangular Superior), de forma que PA = LU,
onde P é a matriz de permutação devido ao pivotamento. Após a decomposição, o sistema Ax = b
é resolvido em duas etapas: substituição para frente e substituição para trás.

Funcionalidades:
1. Definição da matriz de coeficientes A e do vetor de constantes b.
2. Fatoração LU com Pivotamento Parcial para decompor a matriz A.
3. Substituição para Frente para resolver Ly = Pb.
4. Substituição para Trás para resolver Ux = y.
5. Validação e tratamento de erros, como matrizes singulares ou não quadradas.
6. Saída detalhada do processo de fatoração e substituição.

Autor: ChatGPT
Data: 2025-01-27
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
    n = len(A)  # Obtém o número de linhas da matriz A

    # Verificação se a matriz A é quadrada (n x n)
    for idx, row in enumerate(A):
        if len(row) != n:
            raise ValueError(f"A matriz deve ser quadrada. Linha {idx + 1} tem {len(row)} colunas.")

    # Inicializando as matrizes L e U com zeros
    # L será a matriz triangular inferior (com 1s na diagonal principal)
    # U será a matriz triangular superior
    L = [[0.0] * n for _ in range(n)]  # Cria uma matriz n x n com zeros para L
    U = [[0.0] * n for _ in range(n)]  # Cria uma matriz n x n com zeros para U

    # Inicialização do vetor de permutação p (representa a troca de linhas durante o pivotamento)
    p = list(range(n))  # p é uma lista que armazena os índices das linhas de A após o pivotamento

    # Decomposição LU com pivotamento parcial: PA = LU
    for k in range(n):
        # Encontrar o pivô na coluna k (maior valor absoluto para estabilidade numérica)
        pivot = abs(A[k][k])  # Inicializa o pivô com o valor absoluto de A[k][k]
        r = k  # Inicializa r como o índice da linha k

        for i in range(k + 1, n):
            if abs(A[i][k]) > pivot:
                pivot = abs(A[i][k])  # Atualiza o pivô com um valor maior
                r = i  # Atualiza o índice da linha do pivô

        if pivot == 0:
            raise ValueError("A matriz A é singular e não pode ser decomposta em LU.")

        # Troca as linhas k e r na matriz A e no vetor de permutação p
        if r != k:
            A[k], A[r] = A[r], A[k]  # Troca as linhas na matriz A
            p[k], p[r] = p[r], p[k]  # Troca os índices no vetor de permutação p

        # Preenche a matriz U (triangular superior)
        for j in range(k, n):
            sum_U = 0.0  # Inicializa a soma dos produtos L[k][m] * U[m][j]
            for m in range(k):
                sum_U += L[k][m] * U[m][j]  # Soma L[k][m] * U[m][j] para m de 0 a k-1
            U[k][j] = A[k][j] - sum_U  # Calcula o elemento U[k][j]

        # Preenche a matriz L (triangular inferior)
        for i in range(k, n):
            if i == k:
                L[k][k] = 1.0  # Define 1 na diagonal principal de L
            else:
                sum_LU = 0.0  # Inicializa a soma dos produtos L[i][m] * U[m][k]
                for m in range(k):
                    sum_LU += L[i][m] * U[m][k]  # Soma L[i][m] * U[m][k] para m de 0 a k-1
                L[i][k] = (A[i][k] - sum_LU) / U[k][k]  # Calcula o elemento L[i][k]

    # Exibe as matrizes L e U após a decomposição
    print("\n=== DECOMPOSIÇÃO LU CONCLUÍDA COM PIVOTAMENTO ===")
    print("\nMatriz L (Triangular Inferior):")
    for row in L:
        print(["{0:.4f}".format(num) for num in row])  # Formata os números para 4 casas decimais

    print("\nMatriz U (Triangular Superior):")
    for row in U:
        print(["{0:.4f}".format(num) for num in row])  # Formata os números para 4 casas decimais

    # Substituição para Frente: Resolver Ly = Pb (triangular inferior)
    y = [0.0] * n  # Inicializa o vetor y com zeros
    print("\n=== SUBSTITUIÇÃO PARA FRENTE ===")
    for i in range(n):
        sum_Ly = 0.0  # Inicializa a soma dos produtos L[i][j] * y[j]
        for j in range(i):
            sum_Ly += L[i][j] * y[j]  # Soma L[i][j] * y[j] para j de 0 a i-1
        y[i] = b[p[i]] - sum_Ly  # Calcula y[i] subtraindo a soma de b[p[i]] - sum_Ly
        print(f"y[{i + 1}] = {y[i]:.6f}")  # Exibe y[i] com 6 casas decimais

    # Substituição para Trás: Resolver Ux = y (triangular superior)
    x = [0.0] * n  # Inicializa o vetor solução x com zeros
    print("\n=== SUBSTITUIÇÃO PARA TRÁS ===")
    for i in range(n - 1, -1, -1):
        sum_Ux = 0.0  # Inicializa a soma dos produtos U[i][j] * x[j]
        for j in range(i + 1, n):
            sum_Ux += U[i][j] * x[j]  # Soma U[i][j] * x[j] para j de i+1 a n-1
        if U[i][i] == 0:
            raise ValueError(f"Divisão por zero detectada na posição U[{i}][{i}]. Sistema sem solução única.")
        x[i] = (y[i] - sum_Ux) / U[i][i]  # Calcula x[i] dividindo a diferença y[i] - sum_Ux por U[i][i]
        print(f"x[{i + 1}] = ({y[i]} - {sum_Ux}) / {U[i][i]} = {x[i]:.6f}")  # Exibe x[i] com 6 casas decimais

    return x  # Retorna o vetor solução x

def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Define a matriz de coeficientes A e o vetor de constantes b.
    2. Exibe o sistema linear original.
    3. Executa a fatoração LU com pivotamento parcial para decompor a matriz A.
    4. Executa a substituição retroativa para encontrar as soluções das variáveis.
    5. Exibe o vetor solução x.
    """
    # Exemplo de sistema linear 3x3:
    # 2x1 - 1x2 - 2x3 = 1
    # -4x1 + 6x2 + 3x3 = 2
    # -4x1 - 2x2 + 8x3 = 3
    A = [
        [2, -1, -2],  # Primeira linha da matriz A
        [-4, 6, 3],   # Segunda linha da matriz A
        [-4, -2, 8]    # Terceira linha da matriz A
    ]

    # Vetor de constantes do sistema linear
    b = [1, 2, 3]  # b contém os valores do lado direito das equações

    print("=== RESOLUÇÃO DE SISTEMAS LINEARES COM FATORAÇÃO LU COM PIVOTAMENTO ===")
    print("\nSistema linear a ser resolvido:")
    for i in range(len(A)):  # i percorre as linhas de A
        eq = ""  # Inicializa a string da equação
        for j in range(len(A[i])):  # j percorre as colunas de A[i]
            eq += f"{A[i][j]}x{j + 1} + "  # Constrói a parte esquerda da equação
        eq = eq.rstrip(" + ") + f" = {b[i]}"  # Remove o último " + " e adiciona "= b[i]"
        print(eq)  # Imprime a equação

    # Chama a função de decomposição LU com pivotamento para resolver o sistema linear
    try:
        x = fatoracao_LU_pivot(A, b)  # x será o vetor solução calculado pela decomposição LU com pivotamento
        # Exibe a solução do sistema linear
        print("\n=== SOLUÇÃO DO SISTEMA ===")
        for i in range(len(x)):  # i percorre as variáveis de x
            print(f"x{i + 1} = {x[i]:.6f}")  # Imprime cada variável com 6 casas decimais
    except ValueError as ve:
        # Trata erros como matrizes não quadradas ou singulares
        print(f"\nErro: {ve}")
    except Exception as e:
        # Trata quaisquer outros erros inesperados
        print(f"\nOcorreu um erro inesperado: {e}")

    print("\n=== FIM DA RESOLUÇÃO ===")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
