import numpy as np

def gauss_seidel(A, b, x0, erro=1e-10, max_iter=50000):
    # Definindo o tamanho do sistema (número de equações)
    n = len(b)
    # Inicializa o vetor de soluções com o chute inicial
    x = x0.copy()
    # Inicia o loop de iterações
    for _ in range(max_iter):
        # Cria uma cópia de x para armazenar os novos valores
        x_novo = x.copy()

        # Calcula o valor de cada componente de x para a nova iteração
        for i in range(n):
            # Soma dos termos para o cálculo de x[i] utilizando o valor mais recente de x
            soma = np.dot(A[i], x_novo) - A[i, i] * x_novo[i]

            # Atualiza x[i] para o valor calculado
            x_novo[i] = (b[i] - soma) / A[i, i]

        # Verifica a convergência
        if np.max(np.abs(x_novo - x)) < erro:
            print(f'Convergência atingida após {_+1} iterações.')
            print(x_novo)
            return x_novo

        # Atualiza o vetor x para a próxima iteração
        x = x_novo

    print(f'Máximo de iterações atingido: {max_iter}.')
    return x


# Exemplo de uso
A = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]], dtype=float)

b = np.array([7, -8, 6], dtype=float)

x0 = np.zeros_like(b)  # Chute inicial

gauss_seidel(A, b, x0)
