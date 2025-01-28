import random

# ==============================================
# Funções para Gerar Sistema Linear
# ==============================================

def gerar_matriz_diagonal_dominante(n):
    """Gera uma matriz nxn diagonalmente dominante"""
    matriz = []
    for i in range(n):
        linha = [random.uniform(-10, 10) for _ in range(n)]
        soma = sum(abs(v) for j, v in enumerate(linha) if j != i)
        linha[i] = soma + 10  # Garante diagonal dominante
        matriz.append(linha)
    return matriz

def multiplicar_matriz_vetor(A, x):
    """Multiplica matriz A pelo vetor x"""
    n = len(A)
    return [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]

# ==============================================
# Método Direto: Eliminação de Gauss
# ==============================================

def eliminacao_gaussiana(A, b):
    n = len(A)
    for k in range(n):
        # Pivoteamento parcial
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        A[k], A[max_row] = A[max_row], A[k]
        b[k], b[max_row] = b[max_row], b[k]
        
        # Eliminação
        for i in range(k+1, n):
            fator = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
            b[i] -= fator * b[k]
    return A, b

def substituicao_retroativa(A, b):
    n = len(A)
    x = [0] * n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(A[i][j]*x[j] for j in range(i+1, n)))/A[i][i]
    return x

def resolver_gauss(A, b):
    """Resolve sistema usando Eliminação de Gauss"""
    A_copy = [linha[:] for linha in A]
    b_copy = b[:]
    try:
        A_tri, b_tri = eliminacao_gaussiana(A_copy, b_copy)
        return substituicao_retroativa(A_tri, b_tri)
    except ZeroDivisionError:
        raise ValueError("Matriz singular")

# ==============================================
# Método Iterativo: Gauss-Seidel
# ==============================================

def gauss_seidel(A, b, erro=0.01, max_iter=1000):
    n = len(b)
    x = [0.0]*n
    for _ in range(max_iter):
        max_dif = 0
        for i in range(n):
            soma = b[i]
            for j in range(n):
                if j != i:
                    soma -= A[i][j] * x[j]
            novo_xi = soma / A[i][i]
            max_dif = max(max_dif, abs(novo_xi - x[i]))
            x[i] = novo_xi
        if max_dif < erro:
            return x, _+1
    return x, max_iter

# ==============================================
# Execução Principal
# ==============================================

def main():
    random.seed(42)  # Para reproducibilidade
    
    # Gerar sistema 6x6
    n = 6
    x_exato = [i+1 for i in range(n)]  # Solução conhecida
    A = gerar_matriz_diagonal_dominante(n)
    b = multiplicar_matriz_vetor(A, x_exato)
    
    # Resolver com método direto
    try:
        x_direto = resolver_gauss(A, b)
    except ValueError as e:
        print(f"Erro no método direto: {e}")
        return
    
    # Resolver com método iterativo
    x_iterativo, iteracoes = gauss_seidel(A, b)
    
    # Exibir resultados
    print("Solução Exata (usada para gerar o sistema):")
    print([f"{v:.4f}" for v in x_exato])
    
    print("\nSolução pelo Método Direto (Eliminação de Gauss):")
    print([f"{v:.4f}" for v in x_direto])
    
    print(f"\nSolução pelo Método Iterativo (Gauss-Seidel) após {iteracoes} iterações:")
    print([f"{v:.4f}" for v in x_iterativo])
    
    # Calcular erros
    erro_direto = max(abs(x_direto[i] - x_exato[i]) for i in range(n))
    erro_iterativo = max(abs(x_iterativo[i] - x_exato[i]) for i in range(n))
    
    print(f"\nErro máximo método direto: {erro_direto:.6f}")
    print(f"Erro máximo método iterativo: {erro_iterativo:.6f}")

if __name__ == "__main__":
    main()