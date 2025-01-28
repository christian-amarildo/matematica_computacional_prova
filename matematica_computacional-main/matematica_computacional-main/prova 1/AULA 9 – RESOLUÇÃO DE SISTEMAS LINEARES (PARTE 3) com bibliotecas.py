# Importação de bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import time

# Funções auxiliares para geração de sistemas lineares aleatórios
def gerar_sistema_linear(n, densidade=1.0):
    """
    Gera um sistema linear Ax = b, onde A é uma matriz aleatória.

    Parâmetros:
        n (int): Dimensão do sistema.
        densidade (float): Proporção de elementos não nulos na matriz A (0 a 1).

    Retorno:
        A (ndarray): Matriz A.
        b (ndarray): Vetor b.
    """
    A = np.random.rand(n, n)
    b = np.random.rand(n)
    
    if densidade < 1.0:
        mascara = np.random.rand(n, n) < densidade
        A *= mascara

    # Garantir que a matriz A seja estritamente diagonal dominante
    for i in range(n):
        A[i, i] += np.sum(np.abs(A[i]))

    return A, b

# Implementação do método de Gauss-Jacobi
def gauss_jacobi(A, b, x0, tol=1e-5, max_iter=1000):
    """
    Resolve o sistema linear usando o método de Gauss-Jacobi.

    Parâmetros:
        A (ndarray): Matriz do sistema.
        b (ndarray): Vetor do lado direito.
        x0 (ndarray): Aproximação inicial.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Retorno:
        x (ndarray): Solução aproximada.
        iteracoes (int): Número de iterações realizadas.
    """
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        x = x_new
    return x, max_iter

# Implementação do método de Gauss-Seidel
def gauss_seidel(A, b, x0, tol=1e-5, max_iter=1000):
    """
    Resolve o sistema linear usando o método de Gauss-Seidel.

    Parâmetros:
        A (ndarray): Matriz do sistema.
        b (ndarray): Vetor do lado direito.
        x0 (ndarray): Aproximação inicial.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Retorno:
        x (ndarray): Solução aproximada.
        iteracoes (int): Número de iterações realizadas.
    """
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1
    return x, max_iter

# Função para comparar os métodos

def comparar_metodos(n_list, densidade, tol=1e-5):
    """
    Compara os métodos de solução de sistemas lineares.

    Parâmetros:
        n_list (list): Lista de tamanhos do sistema.
        densidade (float): Proporção de elementos não nulos na matriz A (0 a 1).
        tol (float): Tolerância para o critério de parada.

    """
    tempo_jacobi = []
    tempo_seidel = []
    iteracoes_jacobi = []
    iteracoes_seidel = []

    for n in n_list:
        A, b = gerar_sistema_linear(n, densidade)
        x0 = np.zeros(n)

        # Tempo e iterações para Gauss-Jacobi
        start = time.time()
        _, it_j = gauss_jacobi(A, b, x0, tol)
        tempo_jacobi.append(time.time() - start)
        iteracoes_jacobi.append(it_j)

        # Tempo e iterações para Gauss-Seidel
        start = time.time()
        _, it_s = gauss_seidel(A, b, x0, tol)
        tempo_seidel.append(time.time() - start)
        iteracoes_seidel.append(it_s)

    # Plotar os gráficos
    plt.figure(figsize=(12, 6))

    # Gráfico de tempo de execução
    plt.subplot(1, 2, 1)
    plt.plot(n_list, tempo_jacobi, label='Gauss-Jacobi', marker='o')
    plt.plot(n_list, tempo_seidel, label='Gauss-Seidel', marker='s')
    plt.xlabel('Tamanho do sistema (n)')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Tempo de execução')
    plt.legend()

    # Gráfico de número de iterações
    plt.subplot(1, 2, 2)
    plt.plot(n_list, iteracoes_jacobi, label='Gauss-Jacobi', marker='o')
    plt.plot(n_list, iteracoes_seidel, label='Gauss-Seidel', marker='s')
    plt.xlabel('Tamanho do sistema (n)')
    plt.ylabel('Número de iterações')
    plt.title('Número de iterações')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Exemplo de uso
n_list = [10, 100, 500, 1000]
comparar_metodos(n_list, densidade=0.5)
