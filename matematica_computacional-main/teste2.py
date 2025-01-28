import math  # Importa a biblioteca matemática, se necessário

def f(x):
    """
    Define a função f(x) = x^3 - 3x - 1
    
    Parâmetros:
        x (float): O valor de x onde a função será avaliada.
    
    Retorna:
        float: O valor de f(x).
    """
    return x**3 - 3*x -1

def bisseccao(a, b, e, max_iter=1000):
    """
    Método da Bissecção para encontrar raízes de f(x) no intervalo [a, b].
    
    Parâmetros:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        e (float): Precisão desejada.
        max_iter (int): Número máximo de iterações.
    
    Retorna:
        float: A raiz aproximada de f(x).
    """
    fa = f(a)
    fb = f(b)
    
    # Verifica se f(a) e f(b) têm sinais opostos
    if fa * fb > 0:
        print("f(a) e f(b) devem ter sinais opostos. O método da bissecção não pode ser aplicado neste intervalo.")
        print(f"f(a) = f({a}) = {fa}")
        print(f"f(b) = f({b}) = {fb}")
        return None
    
    print(f"Iniciando o Método da Bissecção com a={a}, b={b}, precisão={e}\n")
    
    for i in range(1, max_iter +1):
        c = (a + b) / 2  # Ponto médio do intervalo
        fc = f(c)
        
        print(f"Iteração {i}: a={a}, b={b}, c={c}, f(c)={fc}")
        
        # Verifica se o ponto médio é a raiz ou se a precisão foi alcançada
        if fc == 0 or (b - a)/2 < e:
            print("Convergência alcançada.")
            return c  # Raiz encontrada
        
        # Decide em qual subintervalo a raiz está
        if fa * fc < 0:
            b = c  # A raiz está no intervalo [a,c]
            fb = fc
        else:
            a = c  # A raiz está no intervalo [c,b]
            fa = fc
    
    print("Número máximo de iterações atingido sem convergência.")
    return c

def main():
    """
    Função principal para executar o método da Bissecção.
    """
    print("=== Método da Bissecção ===")
    
    # Definir o intervalo [a,b]
    a = -1.0
    b = 20.0  # Ajustado para [1,2] onde f(a) = -3 e f(b) =1
    
    # Definir a precisão desejada
    e = 1e-6
    
    # Chamar o método da Bissecção
    raiz = bisseccao(a, b, e)
    
    if raiz is not None:
        print(f"\nRaiz encontrada: {raiz}")
        print(f"f({raiz}) = {f(raiz)}")
    
    print("\n=== FIM ===")

if __name__ == "__main__":
    main()
