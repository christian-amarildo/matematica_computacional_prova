import math


def secante(f, x0, x1, erro):
    """
    f: função
    x0, x1: chutes iniciais
    """
    i = 0

    while True:        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"iteração {i}, x0: {x0}, x1: {x1}, f(x0): {f(x0)}, f(x1): {f(x1)}, x2: {x2}")

        if abs(x2 - x1) < erro:
            return x2
        
        x0 = x1
        x1 = x2
        i += 1

# f(x) = x**3 - 9*x + 3
# secante(lambda x: x**3 - 9*x + 3, -4, -2, 1e-9) # deu certo

# # # f(x) = x**0.5 - 5*math.exp(-x)
# secante(lambda x: x**0.5 - 5*math.exp(-x), 1, 2, 1e-9) # deu certo

# # f(x) = x * math.log10(x) - 1
secante(lambda x: x * math.log10(x) - 1, 2.3, 2.7, 1e-9) # deu certo