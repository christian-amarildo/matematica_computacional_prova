import math


def ponto_fixo(g, x0, erro):
    """
    g: função com o x isolado
    a, b: intervalo para procurar uma raiz 
    """
    i = 0
    x = x0
    while True:
        x_novo = g(x)
        print(f"iteração {i}, x: {x}, g(x): {x_novo}")

        if abs(x_novo - x) < erro:
            return x_novo
        x = x_novo
        i += 1

# f(x) = x**3 - 9*x + 3, g(x) = (9*x - 3) ** (1/3)
# ponto_fixo(lambda x: (9*x - 3) ** (1/3), 2, 1e-9) # deu certo

# f(x) = x ** (0.5) - 5*math.exp(-x), g(x) = (5*math.exp(-x))**2
# ponto_fixo(lambda x: (5*math.exp(-x))**2, 1.5, 1e-9) # looping

# f(x) = x*math.log10(x) - 1, g(x) = 1 / math.log10(x)
# ponto_fixo(lambda x: 10 ** (1/x), 2, 1e-9) # deu certo

ponto_fixo(lambda x: x - 1.3*(x * math.log10(x) - 1), 2.5, 1e-9) # deu certo