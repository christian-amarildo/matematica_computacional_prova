import numpy as np

# Matriz com as funções, precisa escrever as funções aqui e adicionar as variáveis como parâmetros
# [F1,
#  F2,
#  ...]
def funcao(x, y, z):
    return np.array([10*x + 2*y + z - 7,
                     x + 5*y + z + 8,
                     2*x + 3*y + 10*z - 6])

# Matriz com as derivadas, precisa escrever as derivadas aqui e adicionar as variáveis como parâmetros
# [[dx_F1, dy_F1],
#  [dx_F2, dy_F2],
#  ...]
def jacobiana(x, y, z):
    return np.array([[10, 2, 1],
                     [1, 5, 1],
                     [2, 3, 10]])

def newton(funcao, jacobiana, vetor_chute, erro=1e-10, max_iter=50000):
    # Chute inicial
    x = np.array(vetor_chute, dtype=float)

    for i in range(max_iter):
        # Calcula o F(x) e J(x)
        # Ajustar variáveis também: x0, x1, x2
        F_val = funcao(x[0], x[1], x[2])
        J_val = jacobiana(x[0], x[1], x[2])

        # Verificar se a solução convergiu
        if np.linalg.norm(F_val, ord=2) < erro:
            print(f"Solução encontrada após {i+1} iterações.")
            print(x)
            return x

        # Atualizar x usando a fórmula de Newton
        delta_x = np.linalg.solve(J_val, F_val)
        x = x - delta_x

    print(f'Máximo de iterações atingido: {max_iter}.')
    return x

def newton_modificado(funcao, jacobiana, vetor_chute, erro=1e-10, max_iter = 50000):
    # Chute inicial
    x = np.array(x0, dtype=float)  # Estimativa inicial
    # Calcular a Jacobiana uma única vez na estimativa inicial
    J = jacobiana(x[0], x[1], x[2])
    
    for i in range(max_iter):
        # Calcular o vetor de funções no ponto atual
        F_val = funcao(x[0], x[1], x[2])
        
        # Verificar se a solução convergiu
        if np.linalg.norm(F_val, ord=2) < erro:
            print(f"Solução encontrada após {i+1} iterações.")
            print(x)
            return x

        # Atualizar x usando a fórmula de Newton
        delta_x = np.linalg.solve(J, F_val)
        x = x - delta_x

    print(f'Máximo de iterações atingido: {max_iter}.')
    return x

x0 = [0, 0, 0]
newton(funcao, jacobiana, x0)

newton_modificado(funcao, jacobiana, x0)