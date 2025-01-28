import math

def norma(v):
    """Calcula a norma Euclidiana de um vetor."""
    return math.sqrt(sum(vi**2 for vi in v))

def resolver_sistema_linear(A, b):
    """
    Resolve o sistema linear Ax = b com pivoteamento parcial.
    Retorna a solução x ou levanta uma exceção se a matriz for singular.
    """
    n = len(A)
    A = [linha.copy() for linha in A]
    b = b.copy()
    pivots = list(range(n))

    for i in range(n):
        max_col = max(range(i, n), key=lambda j: abs(A[j][i]))
        if i != max_col:
            A[i], A[max_col] = A[max_col], A[i]
            b[i], b[max_col] = b[max_col], b[i]
            pivots[i], pivots[max_col] = pivots[max_col], pivots[i]

        if abs(A[i][i]) < 1e-15:
            raise ValueError("Matriz singular detectada")

        for j in range(i+1, n):
            fator = A[j][i] / A[i][i]
            b[j] -= fator * b[i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]

    x = [0.0]*n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
    
    return [x[pivots.index(i)] for i in range(n)]

def metodo_newton(F, J, x0, ε1=1e-6, ε2=1e-6, max_iter=100):
    """
    Resolve sistema não-linear F(x) = 0 usando o método de Newton.
    Retorna a solução, histórico de iterações e status de convergência.
    """
    historico = []
    x = x0.copy()
    convergiu = False
    
    for k in range(max_iter):
        Fx = F(x)
        norma_Fx = norma(Fx)
        historico.append({
            'iteração': k,
            'x': x.copy(),
            'F(x)': Fx.copy(),
            '||F(x)||': norma_Fx
        })

        if norma_Fx < ε1:
            convergiu = True
            break

        try:
            Jx = J(x)
            delta = resolver_sistema_linear(Jx, [-fi for fi in Fx])
        except Exception as e:
            historico.append({'erro': str(e)})
            break

        norma_delta = norma(delta)
        x = [xi + di for xi, di in zip(x, delta)]
        
        historico[-1]['Δx'] = delta.copy()
        historico[-1]['||Δx||'] = norma_delta

        if norma_delta < ε2:
            convergiu = True
            break

    return x, historico, convergiu

def imprimir_historico(historico):
    """Imprime o histórico de iterações de forma formatada."""
    for passo in historico:
        if 'erro' in passo:
            print(f"Erro: {passo['erro']}")
            break
        
        saida = f"Iteração {passo['iteração']}:\n"
        saida += f"x = {[round(v, 6) for v in passo['x']]}\n"
        saida += f"F(x) = {[round(v, 6) for v in passo['F(x)']]}\n"
        saida += f"||F(x)|| = {round(passo['||F(x)||'], 6)}\n"
        if 'Δx' in passo:
            saida += f"Δx = {[round(v, 6) for v in passo['Δx']]}\n"
            saida += f"||Δx|| = {round(passo['||Δx||'], 6)}"
        print(saida + "\n" + "-"*40)

# Exemplo de uso para o sistema proposto
if __name__ == "__main__":
    # Definir o sistema F(x) = 0
    def F(x):
        return [
            x[0]**2 + x[1]**2 - 2,
            math.exp(x[0]-1) + x[1]**3 - 2
        ]

    # Definir a Jacobiana J(x)
    def J(x):
        return [
            [2*x[0], 2*x[1]],
            [math.exp(x[0]-1), 3*x[1]**2]
        ]

    # Parâmetros do método
    x0 = [1.5, 0.8]  # Chute inicial
    ε = 0.001
    max_iter = 20

    # Executar o método de Newton
    solucao, historico, convergiu = metodo_newton(F, J, x0, ε, ε, max_iter)

    # Imprimir resultados
    print("Resolução do sistema não-linear:")
    print(f"Solução encontrada: {[round(v, 6) for v in solucao]}")
    print(f"Convergência: {'Sim' if convergiu else 'Não'}")
    print("\nHistórico completo das iterações:")
    imprimir_historico(historico)