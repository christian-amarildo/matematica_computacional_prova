import math

def bisseccao(f, a, b, erro):
    """
    f: função
    a, b: intervalo para procurar uma raiz 
    """
    i = 0
    ai = a
    bi = b

    while abs(bi-ai) > erro:
        c = (ai+bi) / 2
        print(f"a{i}: {ai}, b{i}: {bi}, c: {c}")
        if f(ai) * f(c) < 0:
            bi = c
        else:
            ai = c
        i += 1
    
    return (ai+bi)/2

# bisseccao(lambda x: x**3 - 9*x + 3, -4, -2, 1e-9)
# bisseccao(lambda x: x ** (0.5) - 5*math.exp(-x), 1, 2, 1e-9)
bisseccao(lambda x: x*math.log10(x) - 1, 2, 3, 1e-9)
