def gauss_elimination_without_lib(A, b):
    """
    Resolve o sistema linear Ax = b utilizando eliminação de Gauss com pivoteamento parcial
    sem bibliotecas externas.

    Parâmetros:
        A (list of list of float): Matriz dos coeficientes (n x n).
        b (list of float): Vetor dos termos independentes (n).

    Retorna:
        list of float: Solução x do sistema.
    """
    n = len(A)

    # Combina A e b em uma matriz aumentada
    for i in range(n):
        A[i].append(b[i])

    # Fase de eliminação
    for k in range(n):
        # Pivoteamento parcial
        max_index = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[max_index][k]):
                max_index = i
        A[k], A[max_index] = A[max_index], A[k]

        # Eliminação para tornar elementos abaixo de A[k][k] iguais a zero
        for i in range(k + 1, n):
            if A[k][k] == 0:
                raise ValueError("Sistema sem solução ou infinitas soluções.")

            m = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] -= m * A[k][j]

    # Fase de substituição retroativa
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            raise ValueError("Sistema sem solução ou infinitas soluções.")

        x[i] = A[i][n] / A[i][i]
        for j in range(i - 1, -1, -1):
            A[j][n] -= A[j][i] * x[i]

    return x

# Exemplo de uso
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b = [8, -11, -3]

solucao = gauss_elimination_without_lib(A, b)
print("Solução:", solucao)
