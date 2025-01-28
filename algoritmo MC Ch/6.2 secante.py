# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método da Secante
============================================

Este programa encontra a raiz de uma função contínua utilizando o Método da Secante.

Funcionalidades:
1. Definição interativa da função f(x).
2. Entrada dos chutes iniciais x0 e x1.
3. Definição dos critérios de precisão e1 e e2.
4. Exibição detalhada de cada iteração do método.
5. Retorno da raiz aproximada com a precisão especificada.


"""

import math  # Importa a biblioteca matemática para usar funções como a exponencial (math.e) e o cosseno (math.cos).

def f(x):
    """
    Define a função f(x) cuja raiz será buscada.

    Retorna:
        float: Valor de f(x)

    Nota:
        - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
        - Exemplo atual: f(x) = e^(-x^2) - cos(x)
    """
    return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)  # Retorna o valor de f(x).

def secante(x0, x1, e1, e2, max_iter=1000):
    """
    Implementa o Método da Secante para encontrar a raiz de uma função f(x).

    Parâmetros:
        x0 (float): Primeiro chute inicial para a raiz.
        x1 (float): Segundo chute inicial para a raiz.
        e1 (float): Precisão desejada para o valor da função, ou seja, |f(x)| < e1.
        e2 (float): Precisão desejada para a diferença entre iterações consecutivas, ou seja, |x2 - x1| < e2.
        max_iter (int): Número máximo de iterações para evitar loops infinitos.

    Retorna:
        float: Raiz aproximada de f(x).

    Levanta:
        ValueError: Se f(x0) * f(x1) >= 0, indicando que não há garantia de raiz no intervalo.
        RuntimeError: Se o método não convergir dentro do número máximo de iterações.
    """

    # Calcula f(x0) e f(x1) para verificar a condição inicial do método
    fx0 = f(x0)  # Valor da função no primeiro chute
    fx1 = f(x1)  # Valor da função no segundo chute

    # Exibe os valores iniciais dos chutes e seus respectivos f(x)
    print(f"Verificando os chutes iniciais:")
    print(f"f({x0}) = {fx0}")
    print(f"f({x1}) = {fx1}\n")

    # Verifica se os chutes iniciais satisfazem a condição f(x0) * f(x1) < 0
    # Esta condição garante que há pelo menos uma raiz no intervalo [x0, x1]
    if fx0 * fx1 >= 0:
        raise ValueError("Os chutes iniciais não satisfazem f(x0) * f(x1) < 0. Método da Secante não pode ser aplicado.")

    # Inicializa o contador de iterações
    k = 0

    # Informa o início do método e os critérios de parada
    print("Iniciando o Método da Secante...")
    print(f"Chutes iniciais: x0 = {x0}, x1 = {x1}")
    print(f"Critérios de parada:")
    print(f"  - |f(x)| < {e1}")
    print(f"  - |x2 - x1| < {e2}")
    print(f"Máximo de iterações: {max_iter}\n")

    # Loop principal do método da Secante
    while k < max_iter:
        # Calcula o denominador da fórmula da Secante para evitar divisão por zero
        denominador = fx1 - fx0

        # Verifica se o denominador é zero para evitar erro de divisão
        if denominador == 0:
            raise ValueError(f"Divisão por zero na iteração {k}. Método da Secante falhou.")

        # Calcula o próximo ponto x2 usando a fórmula da Secante
        x2 = x1 - (fx1 * (x1 - x0)) / denominador

        # Calcula f(x2) para verificar os critérios de parada
        fx2 = f(x2)

        # Exibe os detalhes da iteração atual
        print(f"Iteração {k}:")
        print(f"  x{k} = {x0}")
        print(f"  x{k+1} = {x1}")
        print(f"  x{k+2} = {x2}")
        print(f"  f(x{k+2}) = {fx2}\n")

        # Verifica o primeiro critério de parada: |f(x2)| < e1
        if abs(fx2) < e1:
            print(f"Critério de parada atendido: |f(x2)| = {abs(fx2)} < {e1}")
            print(f"Raiz aproximada encontrada: {x2}\n")
            return x2  # Retorna a raiz encontrada

        # Verifica o segundo critério de parada: |x2 - x1| < e2
        if abs(x2 - x1) < e2:
            print(f"Critério de parada atendido: |x2 - x1| = {abs(x2 - x1)} < {e2}")
            print(f"Raiz aproximada encontrada: {x2}\n")
            return x2  # Retorna a raiz encontrada

        # Atualiza os valores de x0 e x1 para a próxima iteração
        x0, x1 = x1, x2
        fx0, fx1 = fx1, fx2

        # Incrementa o contador de iterações
        k += 1

    # Se o método não convergir dentro do número máximo de iterações, levanta um erro
    raise RuntimeError(f"O método da Secante não convergiu após {max_iter} iterações.")

def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Exibe uma mensagem de boas-vindas.
    2. Informa ao usuário sobre a função definida.
    3. Solicita ao usuário os chutes iniciais x0 e x1.
    4. Solicita ao usuário os critérios de precisão e1 e e2.
    5. Executa o Método da Secante para encontrar a raiz.
    6. Exibe o resultado final.
    7. Termina o programa.
    """

    # Exibe uma mensagem de boas-vindas e informações iniciais
    print("===========================================")
    print("       CALCULADORA DE RAÍZES - SECANTE")
    print("===========================================\n")

    # Informa ao usuário sobre a função definida
    print("Por favor, defina a função f(x) no código.")
    print("Atualmente, a função está definida como:")
    print("f(x) = e^(-x^2) - cos(x)")
    print("Se desejar modificar a função, edite a função f(x) diretamente no código.\n")

    # Solicita ao usuário os chutes iniciais x0 e x1
    while True:
        try:
            # Solicita o primeiro chute inicial x0
            x0 = float(input("Digite o primeiro chute inicial (x0): "))
            # Solicita o segundo chute inicial x1
            x1 = float(input("Digite o segundo chute inicial (x1): "))
            break  # Sai do loop se as entradas forem válidas
        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite números válidos para os chutes iniciais.\n")

    # Solicita ao usuário a precisão desejada e1
    while True:
        try:
            # Solicita a precisão para |f(x)|
            e1 = float(input("Digite a precisão desejada para |f(x)| (e1) (exemplo: 1e-6): "))
            if e1 <= 0:
                # Verifica se a precisão é um número positivo
                print("A precisão e1 deve ser um número positivo. Tente novamente.\n")
                continue
            break  # Sai do loop se a entrada for válida
        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número válido para e1.\n")

    # Solicita ao usuário a precisão desejada e2
    while True:
        try:
            # Solicita a precisão para |x2 - x1|
            e2 = float(input("Digite a precisão desejada para |x2 - x1| (e2) (exemplo: 1e-6): "))
            if e2 <= 0:
                # Verifica se a precisão é um número positivo
                print("A precisão e2 deve ser um número positivo. Tente novamente.\n")
                continue
            break  # Sai do loop se a entrada for válida
        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número válido para e2.\n")

    # Informa ao usuário que o método será iniciado
    print("\nExecutando o Método da Secante...\n")

    # Executa o Método da Secante para encontrar a raiz da função f(x)
    try:
        raiz = secante(x0, x1, e1, e2)  # Chama a função secante com os parâmetros fornecidos
        print(f"Resultado: A raiz aproximada de f(x) é: {raiz}\n")  # Exibe a raiz aproximada encontrada
    except ValueError as ve:
        # Trata erros levantados pela função secante, como chutes iniciais inválidos
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
