import math

# Definição da função f(x)
def f(x):
    """
    Define a função f(x) = x^log(x) + x^2 - x^3 * sin(x).
    """
    if x <= 0:
        raise ValueError("x deve ser maior que 0 para calcular o logaritmo natural.")
    return x ** (math.log(x)) + x**2 - x**3 * math.sin(x)

# Definição da derivada f'(x)
def df(x):
    """
    Define a derivada da função f(x).
    """
    if x <= 0:
        raise ValueError("x deve ser maior que 0 para calcular o logaritmo natural.")
    return 2 * math.log(x) * x ** (math.log(x) - 1) - x**3 * math.cos(x) - 3 * x**2 * math.sin(x) + 2 * x

# Método da Bissecção
def bisseccao(a, b, e, max_iter=1000):
    """
    Método da Bissecção para encontrar raízes de f(x) no intervalo [a, b].
    """
    if a <= 0 or b <= 0:
        return None, 0
    
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        return None, 0
    
    iteracoes = 0
    while abs(b - a) > e and iteracoes < max_iter:
        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c, iteracoes
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        iteracoes += 1
    
    return (a + b) / 2, iteracoes

# Método de Newton-Raphson
def newton_raphson(x0, e, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar raízes de f(x).
    """
    if x0 <= 0:
        return None, 0
    
    iteracoes = 0
    while iteracoes < max_iter:
        fx0, dfx0 = f(x0), df(x0)
        if dfx0 == 0:
            return None, iteracoes
        
        x1 = x0 - fx0 / dfx0
        if x1 <= 0 or abs(x1 - x0) < e:
            return x1, iteracoes + 1
        
        x0 = x1
        iteracoes += 1
    
    return None, iteracoes

# Método da Secante
def secante(x0, x1, e, max_iter=1000):
    """
    Método da Secante para encontrar raízes de f(x).
    """
    if x0 <= 0 or x1 <= 0:
        return None, 0
    
    iteracoes = 0
    while iteracoes < max_iter:
        fx0, fx1 = f(x0), f(x1)
        if fx1 - fx0 == 0:
            return None, iteracoes
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        if x2 <= 0 or abs(x2 - x1) < e:
            return x2, iteracoes + 1
        
        x0, x1 = x1, x2
        iteracoes += 1
    
    return None, iteracoes

# Método de Ponto Fixo
def ponto_fixo(g, x0, e, max_iter=1000):
    """
    Método de Ponto Fixo para encontrar raízes de f(x).
    """
    if x0 <= 0:
        return None, 0
    
    iteracoes = 0
    while iteracoes < max_iter:
        x1 = g(x0)
        if x1 <= 0 or abs(x1 - x0) < e:
            return x1, iteracoes + 1
        
        x0 = x1
        iteracoes += 1
    
    return None, iteracoes

# Método da Posição Falsa
def posicao_falsa(a, b, e, max_iter=1000):
    """
    Método da Posição Falsa para encontrar raízes de f(x).
    """
    if a <= 0 or b <= 0:
        return None, 0
    
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        return None, 0
    
    iteracoes = 0
    while abs(b - a) > e and iteracoes < max_iter:
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if fc == 0:
            return c, iteracoes
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        iteracoes += 1
    
    return (a + b) / 2, iteracoes

# Função para encontrar múltiplas raízes
def encontrar_raizes(metodo, intervalo, e, num_subintervalos=100, **kwargs):
    """
    Encontra múltiplas raízes de f(x) usando um método numérico.
    """
    a, b = intervalo
    subintervalo_tamanho = (b - a) / num_subintervalos
    raizes = []
    iteracoes_totais = 0

    for i in range(num_subintervalos):
        a_sub = a + i * subintervalo_tamanho
        b_sub = a + (i + 1) * subintervalo_tamanho

        try:
            if metodo.__name__ in ["bisseccao", "posicao_falsa"]:
                raiz, iteracoes = metodo(a_sub, b_sub, e, **kwargs)
            elif metodo.__name__ == "newton_raphson":
                x0 = (a_sub + b_sub) / 2
                raiz, iteracoes = metodo(x0, e, **kwargs)
            elif metodo.__name__ == "secante":
                x0, x1 = a_sub, b_sub
                raiz, iteracoes = metodo(x0, x1, e, **kwargs)
            elif metodo.__name__ == "ponto_fixo":
                x0 = (a_sub + b_sub) / 2
                g = kwargs.get("g")
                if not g:
                    raise ValueError("Função 'g' não fornecida para o método de ponto fixo.")
                # Remove 'g' de kwargs para evitar duplicação
                kwargs_sem_g = {k: v for k, v in kwargs.items() if k != "g"}
                raiz, iteracoes = metodo(g, x0, e, **kwargs_sem_g)
            else:
                continue

            if raiz is not None:
                raizes.append((raiz, iteracoes))
                iteracoes_totais += iteracoes

        except ValueError as ve:
            continue  # Ignora subintervalos inválidos

    return raizes, iteracoes_totais

# Função principal
def main():
    intervalo = (1.0, 20.0)
    e = 1e-6
    num_subintervalos = 100

    # Método da Bissecção
    print("Método da Bissecção:")
    raizes, iteracoes = encontrar_raizes(bisseccao, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método de Newton-Raphson
    print("Método de Newton-Raphson:")
    raizes, iteracoes = encontrar_raizes(newton_raphson, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método da Secante
    print("Método da Secante:")
    raizes, iteracoes = encontrar_raizes(secante, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método de Ponto Fixo
    print("Método de Ponto Fixo:")
    def g(x):
        return x - f(x) / df(x)  # Função de iteração
    raizes, iteracoes = encontrar_raizes(ponto_fixo, intervalo, e, num_subintervalos, g=g)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

    # Método da Posição Falsa
    print("Método da Posição Falsa:")
    raizes, iteracoes = encontrar_raizes(posicao_falsa, intervalo, e, num_subintervalos)
    for raiz, it in raizes:
        print(f"Raiz: {raiz:.6f}, Iterações: {it}")
    print(f"Iterações totais: {iteracoes}\n")

if __name__ == "__main__":
    main()