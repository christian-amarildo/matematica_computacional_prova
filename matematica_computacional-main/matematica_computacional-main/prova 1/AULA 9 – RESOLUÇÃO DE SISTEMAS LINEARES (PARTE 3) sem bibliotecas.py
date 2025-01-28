# Implementação de métodos iterativos sem bibliotecas externas

def gerar_sistema_linear_sem_bibliotecas(n, densidade=1.0):
    """
    Gera um sistema linear Ax = b com A sendo uma matriz aleatória.

    Parâmetros:
        n (int): Dimensão do sistema.
        densidade (float): Proporção de elementos não nulos na matriz A (0 a 1).

    Retorno:
        A (list): Matriz A.
        b (list): Vetor b.
    """
    import random

    # Gerar matriz A
    A = [[random.random() if random.random() < densidade else 0 for _ in range(n)] for _ in range(n)]

    # Tornar a matriz estritamente diagonal dominante
    for i in range(n):
        A[i][i] += sum(abs(A[i][j]) for j in range(n))

    # Gerar vetor b
    b = [random.random() for _ in range(n)]

    return A, b

def norma_infinito(v):
    """
    Calcula a norma infinito de um vetor.

    Parâmetros:
        v (list): Vetor.

    Retorno:
        float: Norma infinito do vetor.
    """
    return max(abs(x) for x in v)

def gauss_jacobi_sem_bibliotecas(A, b, x0, tol=1e-5, max_iter=1000):
    """
    Resolve o sistema linear usando o método de Gauss-Jacobi.

    Parâmetros:
        A (list): Matriz do sistema.
        b (list): Vetor do lado direito.
        x0 (list): Aproximação inicial.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Retorno:
        x (list): Solução aproximada.
        iteracoes (int): Número de iterações realizadas.
    """
    n = len(b)
    x = x0[:]
    for k in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - soma) / A[i][i]

        if norma_infinito([x_new[i] - x[i] for i in range(n)]) < tol:
            return x_new, k + 1

        x = x_new[:]

    return x, max_iter

def gauss_seidel_sem_bibliotecas(A, b, x0, tol=1e-5, max_iter=1000):
    """
    Resolve o sistema linear usando o método de Gauss-Seidel.

    Parâmetros:
        A (list): Matriz do sistema.
        b (list): Vetor do lado direito.
        x0 (list): Aproximação inicial.
        tol (float): Tolerância para o critério de parada.
        max_iter (int): Número máximo de iterações.

    Retorno:
        x (list): Solução aproximada.
        iteracoes (int): Número de iterações realizadas.
    """
    n = len(b)
    x = x0[:]
    for k in range(max_iter):
        x_old = x[:]
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(i)) + sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - soma) / A[i][i]

        if norma_infinito([x[i] - x_old[i] for i in range(n)]) < tol:
            return x, k + 1

    return x, max_iter

def comparar_metodos_sem_bibliotecas(n_list, densidade, tol=1e-5):
    """
    Compara os métodos de solução de sistemas lineares.

    Parâmetros:
        n_list (list): Lista de tamanhos do sistema.
        densidade (float): Proporção de elementos não nulos na matriz A (0 a 1).
        tol (float): Tolerância para o critério de parada.
    """
    for n in n_list:
        A, b = gerar_sistema_linear_sem_bibliotecas(n, densidade)
        x0 = [0] * n

        # Gauss-Jacobi
        _, iter_jacobi = gauss_jacobi_sem_bibliotecas(A, b, x0, tol)
        print(f"Gauss-Jacobi (n={n}): {iter_jacobi} iterações")

        # Gauss-Seidel
        _, iter_seidel = gauss_seidel_sem_bibliotecas(A, b, x0, tol)
        print(f"Gauss-Seidel (n={n}): {iter_seidel} iterações")

# Exemplo de uso
n_list = [10, 100, 500]
comparar_metodos_sem_bibliotecas(n_list, densidade=0.5)
