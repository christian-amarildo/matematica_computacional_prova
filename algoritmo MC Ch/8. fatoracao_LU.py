# -*- coding: utf-8 -*-
"""
Calculadora de Sistemas Lineares pelo Método de Fatoração LU
===========================================================
Este programa resolve sistemas lineares da forma Ax = b utilizando o Método de Fatoração LU.

Funcionalidades:
1. Definição da matriz de coeficientes A e do vetor de constantes b.
2. Fatoração LU para decompor A em L (Triangular Inferior) e U (Triangular Superior).
3. Substituição para Frente para resolver Ly = b.
4. Substituição para Trás para resolver Ux = y.
5. Validação e tratamento de erros, como matrizes singulares ou não quadradas.
6. Saída detalhada do processo de fatoração e substituição.


"""

def fatoracao_LU(A, b):
    """
    Resolve um sistema linear Ax = b utilizando a decomposição LU.

    Parâmetros:
        A (list of list of floats): Matriz dos coeficientes (n x n).
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

    # Decomposição LU: A matriz A será decomposta nas matrizes L e U, de forma que A = L * U
    for i in range(n):  # i percorre as linhas da matriz A
        # Preenche a matriz U (triangular superior)
        for j in range(i, n):  # j percorre as colunas de i até n (para manter a triangularidade superior)
            # Calcula o elemento U[i][j] com a fórmula da decomposição LU
            sum_U = sum(L[i][k] * U[k][j] for k in range(i))  # Soma L[i][k] * U[k][j] para k de 0 a i-1
            U[i][j] = A[i][j] - sum_U  # Define U[i][j]

        # Preenche a matriz L (triangular inferior)
        for j in range(i, n):  # j percorre as linhas a partir de i até n
            if i == j:
                L[i][i] = 1.0  # Define 1 na diagonal principal de L
            else:
                # Calcula o valor L[j][i] com a fórmula da decomposição LU
                sum_LU = sum(L[j][k] * U[k][i] for k in range(i))  # Soma L[j][k] * U[k][i] para k de 0 a i-1
                L[j][i] = (A[j][i] - sum_LU) / U[i][i]  # Define L[j][i]

    # Exibe as matrizes L e U após a decomposição
    print("\n=== DECOMPOSIÇÃO LU CONCLUÍDA ===")
    print("\nMatriz L (Triangular Inferior):")
    for row in L:
        print(row)
    print("\nMatriz U (Triangular Superior):")
    for row in U:
        print(row)

    # Substituição para Frente: Resolver Ly = b (triangular inferior)
    y = [0.0] * n  # Inicializa o vetor y com zeros
    print("\n=== SUBSTITUIÇÃO PARA FRENTE ===")
    for i in range(n):  # i percorre as linhas de 0 até n-1
        # Calcula a soma de L[i][j] * y[j] para j de 0 a i-1
        sum_Ly = sum(L[i][j] * y[j] for j in range(i))  # Soma L[i][j] * y[j]
        y[i] = b[i] - sum_Ly  # Calcula y[i]
        print(f"y[{i + 1}] = {y[i]:.6f}")  # Exibe y[i]

    # Substituição para Trás: Resolver Ux = y (triangular superior)
    x = [0.0] * n  # Inicializa o vetor solução x com zeros
    print("\n=== SUBSTITUIÇÃO PARA TRÁS ===")
    for i in range(n - 1, -1, -1):  # i percorre as linhas de n-1 até 0 (de baixo para cima)
        # Calcula a soma de U[i][j] * x[j] para j de i+1 até n-1
        sum_Ux = sum(U[i][j] * x[j] for j in range(i + 1, n))  # Soma U[i][j] * x[j]
        if U[i][i] == 0:
            raise ValueError(f"Divisão por zero detectada na posição U[{i}][{i}]. Sistema sem solução única.")
        x[i] = (y[i] - sum_Ux) / U[i][i]  # Calcula x[i]
        print(f"x[{i + 1}] = ({y[i]} - {sum_Ux}) / {U[i][i]} = {x[i]:.6f}")  # Exibe x[i]

    return x  # Retorna o vetor solução x

def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Define a matriz de coeficientes A e o vetor de constantes b.
    2. Exibe o sistema linear original.
    3. Executa a fatoração LU para decompor a matriz A.
    4. Executa a substituição retroativa para encontrar as soluções das variáveis.
    5. Exibe o vetor solução x.
    """
    # Exemplo de sistema linear 2x2:
    # 4x1 + 3x2 = 10
    # 6x1 + 3x2 = 12
    A = [
        [4, 3],  # Primeira linha da matriz A: 4x1 + 3x2
        [6, 3]   # Segunda linha da matriz A: 6x1 + 3x2
    ]

    # Vetor de constantes do sistema linear
    b = [10, 12]  # b contém os valores do lado direito das equações

    # Exibe o sistema linear original
    print("=== RESOLUÇÃO DE SISTEMAS LINEARES COM FATORAÇÃO LU ===")
    print("\nSistema linear a ser resolvido:")
    for i in range(len(A)):  # i percorre as linhas de A
        eq = ""  # Inicializa a string da equação
        for j in range(len(A[i])):  # j percorre as colunas de A[i]
            eq += f"{A[i][j]}x{j + 1} + "  # Constrói a parte esquerda da equação
        eq = eq.rstrip(" + ") + f" = {b[i]}"  # Remove o último " + " e adiciona "= b[i]"
        print(eq)  # Imprime a equação

    # Chama a função fatoracao_LU para resolver o sistema linear Ax = b
    try:
        x = fatoracao_LU(A, b)  # x será o vetor solução calculado pela decomposição LU
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
