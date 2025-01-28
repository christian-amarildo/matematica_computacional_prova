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
    f'(x) = 2 * log(x) * x^(log(x) - 1) - x^3 * cos(x) - 3x^2 * sin(x) + 2x
    """
    if x <= 0:
        raise ValueError("x deve ser maior que 0 para calcular o logaritmo natural.")
    return 2 * math.log(x) * x ** (math.log(x) - 1) - x**3 * math.cos(x) - 3 * x**2 * math.sin(x) + 2 * x

# Definição da derivada segunda f''(x)
def d2f(x):
    """
    Define a derivada segunda da função f(x).
    f''(x) = x(x^2 - 6)sin(x) - 6x^2 cos(x) + (2(2log^2(x) x^log(x) - log(x)x^log(x) + x^log(x) + x^2) x^2)
    """
    if x <= 0:
        raise ValueError("x deve ser maior que 0 para calcular o logaritmo natural.")
    return x * (x**2 - 6) * math.sin(x) - 6 * x**2 * math.cos(x) + 2 * (2 * math.log(x)**2 * x**math.log(x) - math.log(x) * x**math.log(x) + x**math.log(x) + x**2) * x**2

# Método da Bissecção
def bisseccao(a, b, e, max_iter=1000):
    """
    Método da Bissecção para encontrar raízes de f(x) no intervalo [a, b].
    """
    if a <= 0 or b <= 0:
        return None, 0  # Retorna None se o intervalo contiver valores inválidos
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        return None, 0  # Retorna None se não houver garantia de raiz no intervalo
    
    iteracoes = 0
    while abs(b - a) > e and iteracoes < max_iter:
        c = (a + b) / 2
        fc = f(c)
        
        if fc == 0:
            return c, iteracoes
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iteracoes += 1
    
    return (a + b) / 2, iteracoes

# Método de Newton-Raphson
def newton_raphson(x0, e, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar raízes de f(x).
    """
    if x0 <= 0:
        return None, 0  # Retorna None se o chute inicial for inválido
    
    iteracoes = 0
    while iteracoes < max_iter:
        fx0 = f(x0)
        dfx0 = df(x0)
        
        if dfx0 == 0:
            return None, iteracoes  # Retorna None se a derivada for zero
        
        x1 = x0 - fx0 / dfx0
        
        if x1 <= 0:
            return None, iteracoes  # Retorna None se x1 for inválido
        
        if abs(x1 - x0) < e:
            return x1, iteracoes
        
        x0 = x1
        iteracoes += 1
    
    return None, iteracoes  # Retorna None se não convergir

# Método da Secante
def secante(x0, x1, e, max_iter=1000):
    """
    Método da Secante para encontrar raízes de f(x).
    """
    if x0 <= 0 or x1 <= 0:
        return None, 0  # Retorna None se os chutes iniciais forem inválidos
    
    iteracoes = 0
    while iteracoes < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        
        if fx1 - fx0 == 0:
            return None, iteracoes  # Retorna None se houver divisão por zero
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        if x2 <= 0:
            return None, iteracoes  # Retorna None se x2 for inválido
        
        if abs(x2 - x1) < e:
            return x2, iteracoes
        
        x0, x1 = x1, x2
        iteracoes += 1
    
    return None, iteracoes  # Retorna None se não convergir

# Método de Ponto Fixo
def ponto_fixo(g, x0, e, max_iter=1000):
    """
    Método de Ponto Fixo para encontrar raízes de f(x).
    """
    if x0 <= 0:
        return None, 0  # Retorna None se o chute inicial for inválido
    
    iteracoes = 0
    while iteracoes < max_iter:
        x1 = g(x0)
        
        if x1 <= 0:
            return None, iteracoes  # Retorna None se x1 for inválido
        
        if abs(x1 - x0) < e:
            return x1, iteracoes
        
        x0 = x1
        iteracoes += 1
    
    return None, iteracoes  # Retorna None se não convergir

# Método da Posição Falsa
def posicao_falsa(a, b, e, max_iter=1000):
    """
    Método da Posição Falsa para encontrar raízes de f(x).
    """
    if a <= 0 or b <= 0:
        return None, 0  # Retorna None se o intervalo contiver valores inválidos
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        return None, 0  # Retorna None se não houver garantia de raiz no intervalo
    
    iteracoes = 0
    while abs(b - a) > e and iteracoes < max_iter:
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        if fc == 0:
            return c, iteracoes
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
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

        if metodo.__name__ in ["bisseccao", "posicao_falsa"]:
            raiz, iteracoes = metodo(a_sub, b_sub, e, **kwargs)
        elif metodo.__name__ == "newton_raphson":
            x0 = (a_sub + b_sub) / 2  # Chute inicial no meio do subintervalo
            raiz, iteracoes = metodo(x0, e, **kwargs)
        elif metodo.__name__ == "secante":
            x0, x1 = a_sub, b_sub  # Chutes iniciais nos limites do subintervalo
            raiz, iteracoes = metodo(x0, x1, e, **kwargs)
        elif metodo.__name__ == "ponto_fixo":
            x0 = (a_sub + b_sub) / 2  # Chute inicial no meio do subintervalo
            raiz, iteracoes = metodo(kwargs["g"], x0, e, **kwargs)

        if raiz is not None:
            raizes.append((raiz, iteracoes))
            iteracoes_totais += iteracoes

    return raizes, iteracoes_totais

# Função principal
def main():
    # Intervalo e precisão
    intervalo = (1.0, 20.0)
    e = 1e-6
    num_subintervalos = 100  # Número de subintervalos para busca de raízes

    # Método da Bissecção
    print("Método da Bissecção:")
    raizes_bisseccao, iter_bisseccao = encontrar_raizes(bisseccao, intervalo, e, num_subintervalos)
    for raiz, iteracoes in raizes_bisseccao:
        print(f"Raiz = {raiz}, Iterações = {iteracoes}")
    print(f"Iterações totais: {iter_bisseccao}\n")

    # Método de Newton-Raphson
    print("Método de Newton-Raphson:")
    raizes_newton, iter_newton = encontrar_raizes(newton_raphson, intervalo, e, num_subintervalos)
    for raiz, iteracoes in raizes_newton:
        print(f"Raiz = {raiz}, Iterações = {iteracoes}")
    print(f"Iterações totais: {iter_newton}\n")

    # Método da Secante
    print("Método da Secante:")
    raizes_secante, iter_secante = encontrar_raizes(secante, intervalo, e, num_subintervalos)
    for raiz, iteracoes in raizes_secante:
        print(f"Raiz = {raiz}, Iterações = {iteracoes}")
    print(f"Iterações totais: {iter_secante}\n")

    # Método de Ponto Fixo
    print("Método de Ponto Fixo:")
    def g(x):
        return x - f(x) / df(x)  # Função g(x) para o método de ponto fixo
    raizes_ponto_fixo, iter_ponto_fixo = encontrar_raizes(ponto_fixo, intervalo, e, num_subintervalos, g=g)
    for raiz, iteracoes in raizes_ponto_fixo:
        print(f"Raiz = {raiz}, Iterações = {iteracoes}")
    print(f"Iterações totais: {iter_ponto_fixo}\n")

    # Método da Posição Falsa
    print("Método da Posição Falsa:")
    raizes_posicao_falsa, iter_posicao_falsa = encontrar_raizes(posicao_falsa, intervalo, e, num_subintervalos)
    for raiz, iteracoes in raizes_posicao_falsa:
        print(f"Raiz = {raiz}, Iterações = {iteracoes}")
    print(f"Iterações totais: {iter_posicao_falsa}\n")

if __name__ == "__main__":
    main()
