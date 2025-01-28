# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método de Newton-Raphson
===================================================

Este programa encontra a raiz de uma função contínua utilizando o Método de Newton-Raphson.

Funcionalidades:
1. Definição interativa da função f(x).
2. Definição da derivada f'(x).
3. Entrada do chute inicial x0.
4. Definição dos critérios de precisão e1 e e2.
5. Exibição detalhada de cada iteração do método.
6. Retorno da raiz aproximada com a precisão especificada.


"""

import math  # Importa o módulo math para funções matemáticas adicionais, se necessário

def f(x):
    """
    Define a função f(x) cuja raiz será buscada.

    Retorna:
        float: Valor de f(x)

    Nota:
        - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
        - Por exemplo, para f(x) = x^3 - 9x + 3, defina como abaixo.
    """
    return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)  # Exemplo de função. Modifique conforme necessário.

def df(x):
    """
    Define a derivada da função f(x).

    Retorna:
        float: Valor da derivada f'(x)

    Nota:
        - Modifique esta função conforme a derivada de f(x) definido acima.
        - Por exemplo, para f(x) = x^3 - 9x + 3, a derivada é f'(x) = 3x^2 - 9.
    """
    return 2 * (math.log(x)) * (x)**(math.log(x)-1) - (x**(3)) * (math.cos(x)) - (3*x**(2) * math.sin(x)) + 2 * x # Derivada da função f(x) = x^2 - 2. Modifique conforme necessário.

def newton_raphson(x0, e1, e2, max_iter=500):
    """
    Implementa o método de Newton-Raphson para encontrar a raiz de uma função f(x).

    Parâmetros:
        x0 (float): Chute inicial para a raiz.
        e1 (float): Precisão desejada para o valor da função, ou seja, |f(x)| < e1.
        e2 (float): Precisão desejada para a diferença entre iterações consecutivas, ou seja, |x1 - x0| < e2.
        max_iter (int): Número máximo de iterações para evitar loops infinitos.

    Retorna:
        float: Raiz aproximada de f(x).

    Levanta:
        ValueError: Se a derivada for zero em algum ponto durante as iterações.
        RuntimeError: Se o método não convergir dentro do número máximo de iterações.
    """
    # Verifica se o chute inicial já é uma solução suficientemente boa
    if abs(f(x0)) < e1:
        # Se o valor absoluto de f(x0) for menor que e1, x0 já é considerado uma boa aproximação para a raiz
        print(f"Chute inicial x0 = {x0} já satisfaz |f(x0)| < {e1}.")
        print(f"Raiz aproximada: {x0}\n")
        return x0  # Retorna o chute inicial como a raiz encontrada
    
    k = 0  # Inicializa o contador de iterações como 0

    print("\nIniciando o Método de Newton-Raphson...")
    print(f"Chute inicial: x0 = {x0}")
    print(f"Critérios de parada:")
    print(f"  - |f(x)| < {e1}")
    print(f"  - |x1 - x0| < {e2}")
    print(f"Máximo de iterações: {max_iter}\n")

    while k < max_iter:
        fx0 = f(x0)  # Calcula f(x0)
        dfx0 = df(x0)  # Calcula f'(x0)

        # Exibe os valores atuais de x0, f(x0) e f'(x0)
        print(f"Iteração {k}:")
        print(f"  x{k} = {x0}")
        print(f"  f(x{k}) = {fx0}")
        print(f"  f'(x{k}) = {dfx0}")

        # Verifica se a derivada é zero para evitar divisão por zero
        if dfx0 == 0:
            raise ValueError(f"A derivada é zero em x = {x0:.6f}. Método falhou.")

        # Calcula o próximo ponto x1 usando a fórmula de Newton-Raphson
        x1 = x0 - fx0 / dfx0
        print(f"  Próximo x = {x1}\n")

        # Verifica o critério de parada 1: |f(x1)| < e1
        if abs(f(x1)) < e1:
            print(f"Critério de parada atendido: |f(x1)| = {abs(f(x1))} < {e1}")
            print(f"Raiz aproximada: {x1}\n")
            return x1  # Retorna x1 como a raiz encontrada

        # Verifica o critério de parada 2: |x1 - x0| < e2
        if abs(x1 - x0) < e2:
            print(f"Critério de parada atendido: |x1 - x0| = {abs(x1 - x0)} < {e2}")
            print(f"Raiz aproximada: {x1}\n")
            return x1  # Retorna x1 como a raiz encontrada

        # Atualiza x0 para a próxima iteração
        x0 = x1
        k += 1  # Incrementa o contador de iterações

    # Se o método não convergir dentro do número máximo de iterações, levanta um erro
    raise RuntimeError(f"O método de Newton-Raphson não convergiu após {max_iter} iterações.")

def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Exibe uma mensagem de boas-vindas.
    2. Informa ao usuário sobre a função definida.
    3. Solicita ao usuário os critérios de precisão e1 e e2.
    4. Solicita ao usuário o chute inicial x0.
    5. Executa o Método de Newton-Raphson para encontrar a raiz.
    6. Exibe o resultado final.
    7. Termina o programa.
    """
    # Exibe uma mensagem de boas-vindas e informações iniciais
    print("===========================================")
    print("   CALCULADORA DE RAÍZES - NEWTON-RAPHSON")
    print("===========================================\n")

    # Informa ao usuário sobre a função definida
    print("Por favor, defina a função f(x) e sua derivada f'(x) no código.")
    print("Atualmente, a função está definida como:")
    print("f(x) = x^2 - 2")
    print("f'(x) = 2x")
    print("Se desejar modificar a função ou sua derivada, edite as funções f(x) e df(x) diretamente no código.\n")

    # Solicita ao usuário o chute inicial x0
    while True:
        try:
            x0 = float(input("Digite o chute inicial (x0) para iniciar as iterações: "))
            break  # Sai do loop se a entrada for válida
        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número válido.\n")

    # Solicita ao usuário a precisão desejada e1
    while True:
        try:
            e1 = float(input("Digite a precisão desejada para |f(x)| (e1) (exemplo: 1e-6): "))
            if e1 <= 0:
                # Verifica se a precisão é um número positivo
                print("A precisão e1 deve ser um número positivo. Tente novamente.\n")
                continue
            break  # Sai do loop se a entrada for válida
        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número válido.\n")

    # Solicita ao usuário a precisão desejada e2
    while True:
        try:
            e2 = float(input("Digite a precisão desejada para |x1 - x0| (e2) (exemplo: 1e-6): "))
            if e2 <= 0:
                # Verifica se a precisão é um número positivo
                print("A precisão e2 deve ser um número positivo. Tente novamente.\n")
                continue
            break  # Sai do loop se a entrada for válida
        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número válido.\n")

    # Executa o Método de Newton-Raphson para encontrar a raiz
    try:
        raiz = newton_raphson(x0, e1, e2)  # Chama a função newton_raphson com os parâmetros fornecidos
        print(f"Resultado: A raiz aproximada de f(x) é: {raiz}\n")  # Exibe a raiz aproximada encontrada
    except ValueError as ve:
        # Trata erros levantados pela função newton_raphson, como derivada zero
        print(f"Erro: {ve}\n")
    except RuntimeError as re:
        # Trata erros de não convergência após o número máximo de iterações
        print(f"Erro: {re}\n")

    # Exibe uma mensagem de encerramento
    print("===========================================")
    print("         FIM DA CALCULADORA DE RAÍZES")
    print("===========================================\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
