# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método da Posição Falsa
==================================================

Este programa encontra a raiz de uma função contínua utilizando o Método da Posição Falsa.

Funcionalidades:
1. Definição interativa da função f(x).
2. Entrada dos limites do intervalo [a, b].
3. Definição dos critérios de precisão.
4. Exibição detalhada de cada iteração do método.
5. Retorno da raiz aproximada com a precisão especificada.


"""
import math
from math import e  # Importa a constante matemática 'e' (base do logaritmo natural) do módulo math.

# Define a função cuja raiz será buscada
def f(x):
    """
    Define a função f(x) cuja raiz será buscada.

    Retorna:
        float: Valor de f(x)

    Nota:
        - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
        - Por exemplo, para f(x) = e^(-2x) - x^2, defina como abaixo.
    """
    return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)  # Exemplo de função. Modifique conforme necessário.

# Define a função que implementa o método da posição falsa
def posicao_falsa(a, b, e1, e2):
    """
    Método da posição falsa para encontrar a raiz de uma função f(x) no intervalo [a, b].

    Parâmetros:
        a (float): Limite inferior do intervalo inicial.
        b (float): Limite superior do intervalo inicial.
        e1 (float): Critério de parada baseado na largura do intervalo.
        e2 (float): Critério de parada baseado na proximidade de f(x) de 0.

    Retorna:
        float: Raiz aproximada de f(x) no intervalo [a, b].

    Levanta:
        ValueError: Se f(a) * f(b) >= 0, indicando que não há garantia de raiz no intervalo.
    """

    # Calcula f(a) e f(b) para verificar a condição inicial
    fa = f(a)  # Valor da função no limite inferior
    fb = f(b)  # Valor da função no limite superior

    # Exibe os valores iniciais de f(a) e f(b)
    print(f"Verificando o intervalo inicial:")
    print(f"f(a) = f({a}) = {fa}")
    print(f"f(b) = f({b}) = {fb}")

    # Verifica se a condição f(a) * f(b) < 0 é satisfeita
    if fa * fb >= 0:
        # Se não for, o método da posição falsa não pode ser aplicado neste intervalo
        raise ValueError("O método da posição falsa falhou. f(a) e f(b) devem ter sinais opostos.")

    # Inicializa o contador de iterações
    k = 1

    # Exibe os valores iniciais do intervalo
    print("\nIniciando o Método da Posição Falsa:")
    print(f"Função definida: f(x) = e^(-2x) - x^2")
    print(f"Intervalo inicial: [{a}, {b}]")
    print(f"Critérios de parada:")
    print(f"  - Largura do intervalo < {e1}")
    print(f"  - |f(x)| < {e2}\n")

    # Verifica se o intervalo inicial já atende aos critérios de parada
    if abs(b - a) < e1:
        # Se o valor de f(a) for suficientemente próximo de 0, retorna a como a raiz
        if abs(fa) < e2:
            print("O intervalo inicial já atende aos critérios de parada.")
            print(f"Raiz aproximada: {a}\n")
            return a
        # Se o valor de f(b) for suficientemente próximo de 0, retorna b como a raiz
        elif abs(fb) < e2:
            print("O intervalo inicial já atende aos critérios de parada.")
            print(f"Raiz aproximada: {b}\n")
            return b
        # Caso contrário, retorna o ponto médio do intervalo como aproximação da raiz
        else:
            x_medio = (a + b) / 2
            print("O intervalo inicial já atende ao critério de largura, mas |f(x)| >= e2.")
            print(f"Raiz aproximada (ponto médio): {x_medio}\n")
            return x_medio

    # Loop para executar o método da posição falsa até atingir os critérios de parada
    while True:
        # Calcula o ponto de posição falsa usando a fórmula específica do método
        # x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        numerador = a * fb - b * fa  # Calcula o numerador da fórmula
        denominador = fb - fa        # Calcula o denominador da fórmula
        x = numerador / denominador  # Calcula o ponto de posição falsa

        # Calcula f(x)
        fx = f(x)  # Valor da função no ponto x

        # Exibe os detalhes da iteração atual
        print(f"Iteração {k}:")
        print(f"  a{k} = {a}")
        print(f"  b{k} = {b}")
        print(f"  x{k} = {x}")
        print(f"  f(x{k}) = {fx}")

        # Verifica se |f(x)| é menor que e2 (critérios de parada)
        if abs(fx) < e2:
            # Se sim, retorna x como a raiz encontrada
            print(f"  |f(x{k})| < {e2}. Critério de parada atendido.\n")
            print(f"Raiz aproximada após {k} iterações: {x}\n")
            return x

        # Atualiza os limites do intervalo [a, b] com base no sinal de f(x)
        if fa * fx > 0:
            # Se f(a) e f(x) têm o mesmo sinal, a raiz está no intervalo [x, b]
            a = x  # Atualiza o limite inferior para x
            fa = fx  # Atualiza f(a) para f(x)
            print(f"  f(a) * f(x{k}) > 0. A raiz está no intervalo [{a}, {b}].\n")
        else:
            # Caso contrário, a raiz está no intervalo [a, x]
            b = x  # Atualiza o limite superior para x
            fb = fx  # Atualiza f(b) para f(x)
            print(f"  f(a) * f(x{k}) <= 0. A raiz está no intervalo [{a}, {b}].\n")

        # Verifica se a largura do intervalo é menor que e1 (critérios de parada)
        if abs(b - a) < e1:
            # Se sim, retorna x como a raiz aproximada
            print(f"  Largura do intervalo < {e1}. Critério de parada atendido.\n")
            print(f"Raiz aproximada após {k} iterações: {x}\n")
            return x

        # Incrementa o contador de iterações
        k += 1

# Define a função principal que controla o fluxo do programa
def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Exibe uma mensagem de boas-vindas.
    2. Informa ao usuário sobre a função definida.
    3. Solicita ao usuário os limites do intervalo [a, b].
    4. Solicita ao usuário os critérios de precisão e1 e e2.
    5. Executa o Método da Posição Falsa para encontrar a raiz.
    6. Exibe o resultado final.
    7. Termina o programa.
    """
    # Exibe uma mensagem de boas-vindas e informações iniciais
    print("===========================================")
    print("     CALCULADORA DE RAÍZES - POSIÇÃO FALSA")
    print("===========================================\n")

    # Informa ao usuário sobre a função definida
    print("Por favor, defina a função f(x) cuja raiz deseja encontrar.")
    print("Atualmente, a função está definida como:")
    print("f(x) = e^(-2x) - x^2")
    print("Se desejar modificar a função, edite a função f(x) diretamente no código.\n")

    # Solicita ao usuário os limites do intervalo [a, b]
    while True:
        try:
            # Solicita o limite inferior do intervalo
            a = float(input("Digite o limite inferior do intervalo (a): "))
            # Solicita o limite superior do intervalo
            b = float(input("Digite o limite superior do intervalo (b): "))

            # Verifica se a <= b
            if a >= b:
                print("O limite inferior deve ser menor que o limite superior. Tente novamente.\n")
                continue  # Reinicia o loop para nova entrada

            # Calcula f(a) e f(b) para verificar a condição do método da posição falsa
            fa = f(a)
            fb = f(b)

            # Verifica se f(a) e f(b) têm sinais opostos
            if fa * fb >= 0:
                print("f(a) e f(b) devem ter sinais opostos. O método da posição falsa não pode ser aplicado neste intervalo.\n")
                print(f"f(a) = f({a}) = {fa}")
                print(f"f(b) = f({b}) = {fb}\n")
                continue  # Reinicia o loop para nova entrada

            # Se tudo estiver correto, sai do loop
            break

        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite números válidos.\n")

    # Solicita ao usuário os critérios de precisão e1 e e2
    while True:
        try:
            # Solicita a precisão para a largura do intervalo
            e1 = float(input("Digite a precisão para a largura do intervalo (e1) (exemplo: 1e-6): "))
            # Solicita a precisão para |f(x)|
            e2 = float(input("Digite a precisão para |f(x)| (e2) (exemplo: 1e-6): "))

            # Verifica se as precisões são números positivos
            if e1 <= 0 or e2 <= 0:
                print("As precisões e1 e e2 devem ser números positivos. Tente novamente.\n")
                continue  # Reinicia o loop para nova entrada

            # Se tudo estiver correto, sai do loop
            break

        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite números válidos.\n")

    # Executa o Método da Posição Falsa para encontrar a raiz
    try:
        # Chama a função posicao_falsa com os parâmetros fornecidos
        raiz = posicao_falsa(a, b, e1, e2)
        # Exibe a raiz aproximada encontrada
        print(f"A raiz aproximada de f(x) no intervalo [{a}, {b}] é: {raiz}")
    except ValueError as ve:
        # Trata erros levantados pela função posicao_falsa
        print(f"Erro: {ve}")

    # Exibe uma mensagem de encerramento
    print("===========================================")
    print("       FIM DA CALCULADORA DE RAÍZES")
    print("===========================================\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
