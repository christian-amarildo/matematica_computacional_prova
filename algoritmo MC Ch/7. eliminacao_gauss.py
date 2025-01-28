# -*- coding: utf-8 -*-
"""
Calculadora de Sistemas Lineares pelo Método de Eliminação de Gauss
===================================================================

Este programa resolve sistemas lineares da forma Ax = b utilizando o Método de Eliminação de Gauss
seguido pela Substituição Retroativa para encontrar as soluções das variáveis.

Funcionalidades:
1. Definição da matriz de coeficientes A e do vetor de constantes b.
2. Eliminação de Gauss para triangularizar a matriz A.
3. Substituição Retroativa para resolver o sistema triangular superior.
4. Validação e tratamento de erros, como matrizes singulares.
5. Saída detalhada do processo de eliminação e substituição.

"""

def eliminacao_gaussiana(A, b):
    """
    Realiza a eliminação de Gauss para transformar a matriz A em uma matriz triangular superior.
    
    Parâmetros:
        A (list of list of floats): Matriz de coeficientes (n x n).
        b (list of floats): Vetor de constantes (tamanho n).
    
    Retorna:
        A (list of list of floats): Matriz A modificada após a eliminação de Gauss.
        b (list of floats): Vetor b modificado após a eliminação de Gauss.
    
    Levanta:
        ValueError: Se a matriz for singular (pivô zero durante a eliminação).
    """
    n = len(A)  # Obtém o número de linhas da matriz A (deve ser igual ao número de colunas)
    
    # Itera sobre cada coluna da matriz A
    for k in range(n):
        # Verifica se o pivô (elemento diagonal) é zero
        if A[k][k] == 0:
            raise ValueError("Matriz singular detectada durante a eliminação de Gauss. Não é possível continuar.")
        
        # Elimina os elementos abaixo do pivô na coluna k
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]  # Calcula o multiplicador para zerar A[i][k]
            # Subtrai m vezes a linha k da linha i para eliminar A[i][k]
            for j in range(k, n):
                A[i][j] -= m * A[k][j]
            # Atualiza o vetor b
            b[i] -= m * b[k]
        
        # Exibe a matriz A e o vetor b após cada passo de eliminação
        print(f"\nApós eliminar os elementos abaixo do pivô na coluna {k + 1}:")
        print("Matriz A:")
        for row in A:
            print(row)
        print("Vetor b:")
        print(b)
    
    return A, b  # Retorna a matriz A e o vetor b modificados

def substituicao_retroativa(A, b):
    """
    Resolve o sistema triangular superior Ax = b utilizando substituição retroativa.
    
    Parâmetros:
        A (list of list of floats): Matriz triangular superior (n x n).
        b (list of floats): Vetor de constantes (tamanho n).
    
    Retorna:
        x (list of floats): Vetor solução (tamanho n).
    """
    n = len(A)  # Obtém o número de variáveis (igual ao número de linhas da matriz A)
    x = [0 for _ in range(n)]  # Inicializa o vetor solução com zeros
    
    # Itera de trás para frente, resolvendo para cada variável
    for i in range(n - 1, -1, -1):
        sum_ax = 0  # Inicializa a soma dos produtos de A[i][j] * x[j]
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]  # Acumula os produtos para as variáveis já resolvidas
        x[i] = (b[i] - sum_ax) / A[i][i]  # Calcula a variável atual
        print(f"Resolvendo x[{i}] = ({b[i]} - {sum_ax}) / {A[i][i]} = {x[i]}")
    
    return x  # Retorna o vetor solução

def resolver_sistema(A, b):
    """
    Resolve o sistema linear Ax = b utilizando Eliminação de Gauss e Substituição Retroativa.
    
    Parâmetros:
        A (list of list of floats): Matriz de coeficientes (n x n).
        b (list of floats): Vetor de constantes (tamanho n).
    
    Retorna:
        x (list of floats): Vetor solução (tamanho n).
    """
    print("Matriz original A:")
    for row in A:
        print(row)
    print("Vetor original b:")
    print(b)
    
    # Passo 1: Eliminação de Gauss
    A_tri, b_tri = eliminacao_gaussiana(A, b)
    
    # Passo 2: Substituição Retroativa
    x = substituicao_retroativa(A_tri, b_tri)
    
    return x  # Retorna a solução do sistema

def main():
    """
    Função principal que controla o fluxo do programa.
    
    Executa as seguintes etapas:
    1. Define a matriz de coeficientes A e o vetor de constantes b.
    2. Exibe o sistema linear original.
    3. Executa a eliminação de Gauss para triangularizar a matriz A.
    4. Executa a substituição retroativa para encontrar as soluções das variáveis.
    5. Exibe o vetor solução x.
    """
    # Exemplo de sistema linear 4x4:
    # 1x + 1y + 0z + 3w = 4
    # 2x + 1y -1z +1w = 1
    # 3x -1y -1z +2w = -3
    # -1x +2y +3z -1w = 4
    A = [
        [1, 1, 0, 3],
        [2, 1, -1, 1],
        [3, -1, -1, 2],
        [-1, 2, 3, -1]
    ]
    
    b = [4, 1, -3, 4]
    
    print("=== RESOLUÇÃO DE SISTEMAS LINEARES ===")
    print("Sistema linear a ser resolvido:")
    for i in range(len(A)):
        eq = ""
        for j in range(len(A[i])):
            eq += f"{A[i][j]}x{j + 1} + "
        eq = eq.rstrip(" + ") + f" = {b[i]}"
        print(eq)
    
    # Chama a função para resolver o sistema
    try:
        x = resolver_sistema(A, b)  # Resolve o sistema linear
        print("\n=== SOLUÇÃO DO SISTEMA ===")
        for i in range(len(x)):
            print(f"x{i + 1} = {x[i]:.6f}")  # Exibe cada variável com 6 casas decimais
    except ValueError as ve:
        # Trata erros como matrizes singulares
        print(f"\nErro: {ve}")
    except Exception as e:
        # Trata quaisquer outros erros inesperados
        print(f"\nOcorreu um erro inesperado: {e}")

    print("\n=== FIM DA RESOLUÇÃO ===")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
