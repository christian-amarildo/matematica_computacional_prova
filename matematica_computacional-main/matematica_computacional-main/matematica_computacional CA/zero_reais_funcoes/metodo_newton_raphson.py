import math


def newton_raphson(f, f_linha, x0, erro):
    """
    f: função
    f_linha: derivada da função
    x0: chute inicial
    """
    i = 0
    x = x0

    while True:
        if f_linha(x) == 0:
            print("Derivada igual a 0, não foi possivel calcular a raíz")
            return
        x_novo = x - f(x) / f_linha(x)
        print(f"iteração {i}, x: {x}, f(x): {f(x)}, f'(x): {f_linha(x)}, x_novo: {x_novo}")

        if abs(x_novo - x) < erro:
            return x_novo
        x = x_novo
        i += 1

# f(x) = x**3 - 9*x + 3, f'(x) = 3*x**2 - 9
# newton_raphson(lambda x: x**3 - 9*x + 3, lambda x: 3*x**2 - 9, 2, 1e-9) # deu certo

# # f(x) = x**0.5 - 5*math.exp(-x), f'(x) = 1 / (2 * (x ** 0.5)) + 5*math.exp(-x)
# newton_raphson(lambda x: x**0.5 - 5*math.exp(-x), lambda x: 1 / (2 * (x ** 0.5)) + 5*math.exp(-x), 1, 1e-9) # deu certo

# f(x) = x * math.log10(x) - 1, f'(x) = math.log10(x) + 1/x
newton_raphson(lambda x: x * math.log10(x) - 1, lambda x: math.log10(x) + 1/math.log(10), 2.5, 1e-9) # deu certo