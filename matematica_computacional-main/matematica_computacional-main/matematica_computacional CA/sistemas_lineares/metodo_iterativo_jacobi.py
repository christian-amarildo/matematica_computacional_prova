
import numpy as np

def jacobi(A, b, x0, erro=1e-10, max_iter=50000):
    # Definindo o tamanho do sistema (número de equações)
    n, _ = np.shape(A)
    # Inicializa o vetor de soluçòes com o chute inicial
    x = x0.copy()
    # Loop de iterações
    for _ in range(max_iter):
        # Cria um novo vetor de soluções para esta iteração
        x_novo = np.zeros_like(x)
        # Calcula o valor de cada componente de x para a nova iteração
        for i in range(n):
            sum_ax = np.dot(A[i, :], x) - A[i, i] * x[i]  # Soma dos produtos
            x_novo[i] = (b[i] - sum_ax) / A[i, i]  # Calcula novo valor de x[i]

        # Verifica a convergência
        if np.max(np.abs(x_novo - x)) < erro:
            print(f'Convergência atingida após {_+1} iterações.')
            print(x_novo)
            return x_novo

        x = x_novo

    print(f'Máximo de iterações atingido: {max_iter}.')
    return x


A = np.array([
    [3, -4, -6],
    [18, -21, -33],
    [12, -10, -22]
], dtype=float)

b = np.array([25, 141, 66], dtype=float)
x0 = np.zeros_like(b)

# Exemplo de uso
A = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]], dtype=float)

b = np.array([7, -8, 6], dtype=float)

x0 = np.zeros_like(b)  # Chute inicial

jacobi(A, b, x0)