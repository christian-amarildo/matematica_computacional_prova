import math


def posicao_falsa(f, a, b, erro):
    """
    f: função
    a, b: intervalo para procurar uma raiz 
    """
    i = 0

    while abs(b-a) > erro:
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(f"a{i}: {a}, b{i}: {b}, x: {x}")

        if abs(f(x)) < erro:
            return x

        if f(a) * f(x) > 0:
            a = x
        else:
            b = x
        i += 1

    return (a+b)/2

# posicao_falsa(lambda x: x**3 - 9*x + 3, -4, -2, 1e-9)
# posicao_falsa(lambda x: x ** (0.5) - 5*math.exp(-x), 1, 2, 1e-9)
posicao_falsa(lambda x: x*math.log10(x) - 1, 2, 3, 1e-9)