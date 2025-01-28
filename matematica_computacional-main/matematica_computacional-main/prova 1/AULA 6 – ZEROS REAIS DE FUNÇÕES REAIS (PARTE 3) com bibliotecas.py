import numpy as np
import math
import matplotlib.pyplot as plt

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """Método de Newton-Raphson para encontrar raízes de funções."""
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if abs(dfx) < 1e-12:  # Verificar divisão por zero
            raise ValueError("Derivada próxima de zero, método pode não convergir.")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1, i + 1
        x0 = x1
    raise ValueError("Método não convergiu em {} iterações.".format(max_iter))

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """Método da Secante para encontrar raízes de funções."""
    for i in range(max_iter):
        fx0, fx1 = f(x0), f(x1)
        if abs(fx1 - fx0) < 1e-12:  # Verificar divisão por zero
            raise ValueError("Diferença muito pequena entre os valores de f(x), método pode não convergir.")
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if abs(x2 - x1) < tol:
            return x2, i + 1
        x0, x1 = x1, x2
    raise ValueError("Método não convergiu em {} iterações.".format(max_iter))

def fixed_point_iteration(phi, x0, tol=1e-6, max_iter=100):
    """Método do Ponto Fixo para encontrar raízes de funções."""
    for i in range(max_iter):
        x1 = phi(x0)
        if abs(x1 - x0) < tol:
            return x1, i + 1
        x0 = x1
    raise ValueError("Método não convergiu em {} iterações.".format(max_iter))

# Funções para teste
functions = [
    lambda x: x**6 - x - 1,  # Polinômio de grau > 5
    lambda x: np.log(x) - 2,
    lambda x: np.exp(x) - 3,
    lambda x: np.sin(x) - 0.5,
    lambda x: x**2 - 2
]

derivatives = [
    lambda x: 6 * x**5 - 1,  # Derivada do polinômio
    lambda x: 1 / x,
    lambda x: np.exp(x),
    lambda x: np.cos(x),
    lambda x: 2 * x
]

intervals = [(1, 2), (1, 4), (0, 2), (0, np.pi), (1, 2)]

# Teste dos métodos
results = []
for i, (f, df, interval) in enumerate(zip(functions, derivatives, intervals)):
    x0 = interval[0]
    x1 = interval[1]

    # Método de Newton-Raphson
    try:
        root_nr, iter_nr = newton_raphson(f, df, x0)
    except ValueError as e:
        root_nr, iter_nr = None, str(e)

    # Método da Secante
    try:
        root_sec, iter_sec = secant_method(f, x0, x1)
    except ValueError as e:
        root_sec, iter_sec = None, str(e)

    # Método do Ponto Fixo (apenas se phi(x) for conhecida)
    phi = lambda x: x - f(x)  # Forma geral para phi(x)
    try:
        root_fp, iter_fp = fixed_point_iteration(phi, x0)
    except ValueError as e:
        root_fp, iter_fp = None, str(e)

    results.append((i + 1, root_nr, iter_nr, root_sec, iter_sec, root_fp, iter_fp))

# Exibição dos resultados
def print_table(results):
    print("\nResultados dos Métodos de Refinamento:\n")
    print("Função | Newton-Raphson      | Secante             | Ponto Fixo")
    print("        | Raiz       Iterações | Raiz       Iterações | Raiz       Iterações")
    print("----------------------------------------------------------------------")
    for res in results:
        idx, root_nr, iter_nr, root_sec, iter_sec, root_fp, iter_fp = res
        print(
            f" {idx:<6} | {root_nr:<10} {iter_nr:<10} | {root_sec:<10} {iter_sec:<10} | {root_fp:<10} {iter_fp:<10}"
        )

print_table(results)
