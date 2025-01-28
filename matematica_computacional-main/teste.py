# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método da Bissecção
==============================================

Este programa encontra a raiz de uma função contínua utilizando o Método da Bissecção.

Funcionalidades:
1. Definição interativa da função f(x).
2. Entrada dos limites do intervalo [a, b].
3. Definição da precisão desejada.
4. Exibição detalhada de cada iteração do método.
5. Retorno da raiz aproximada com a precisão especificada.

"""

# Importa o módulo math para funções matemáticas adicionais, se necessário
import math

# Define a função f(x) cuja raiz será buscada
def f(x):
    """
    Define a função f(x) cuja raiz será buscada.

    Retorna:
        float: Valor de f(x)
    
    Nota:
        - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
        - Por exemplo, para f(x) = x^3 - 3x - 1, defina como abaixo.
    """
    return x ** (math.log(x)) + x**2 - x**3 * math.sin(x) # Exemplo de função. Modifique conforme necessário.

# Define o Método da Bissecção para encontrar a raiz de f(x) em [a, b]
def bisseccao(a, b, e):
    """
    Método da Bissecção para encontrar a raiz de f(x) em [a, b].

    Parâmetros:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        e (float): Precisão desejada para o cálculo.

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
        # Se não for, o método da bissecção não pode ser aplicado neste intervalo
        raise ValueError("O método da bissecção falhou. f(a) e f(b) devem ter sinais opostos.")

    # Inicializa o contador de iterações
    i = 1

    # Define os limites atuais do intervalo como a e b
    ai = a  # Limite inferior atual
    bi = b  # Limite superior atual

    # Exibe os valores iniciais do intervalo
    print("\nIniciando o Método da Bissecção:")
    print(f"Função definida: f(x) = {f.__doc__.strip().splitlines()[0]}")
    print(f"Intervalo inicial: [{ai}, {bi}]")
    print(f"Precisão desejada: {e}\n")

    # Loop que executa as iterações do método da bissecção
    while abs(bi - ai) > e:
        # Calcula o ponto médio do intervalo atual
        xi = (ai + bi) / 2  # Ponto médio

        # Calcula f(xi)
        fxi = f(xi)  # Valor da função no ponto médio

        # Exibe os detalhes da iteração atual
        print(f"Iteração {i}:")
        print(f"  a{i} = {ai}")  # Limite inferior atual
        print(f"  b{i} = {bi}")  # Limite superior atual
        print(f"  x{i} = {xi}")  # Ponto médio atual
        print(f"  f(x{i}) = {fxi}")  # Valor da função no ponto médio

        # Determina em qual subintervalo a raiz está localizada
        if f(ai) * fxi < 0:
            # Se f(a) e f(xi) têm sinais opostos, a raiz está no subintervalo [ai, xi]
            bi = xi  # Atualiza o limite superior para o ponto médio
            print(f"  A raiz está no intervalo [{ai}, {xi}].\n")
        else:
            # Caso contrário, a raiz está no subintervalo [xi, bi]
            ai = xi  # Atualiza o limite inferior para o ponto médio
            print(f"  A raiz está no intervalo [{xi}, {bi}].\n")

        # Incrementa o contador de iterações
        i += 1

    # Calcula a raiz aproximada como o ponto médio final
    raiz_aproximada = (ai + bi) / 2

    # Exibe os resultados finais após a conclusão do método
    print(f"Raiz aproximada após {i-1} iterações: {raiz_aproximada}")
    print(f"Intervalo final: [{ai}, {bi}]")
    print(f"f({raiz_aproximada}) = {f(raiz_aproximada)}\n")

    # Retorna a raiz aproximada encontrada
    return raiz_aproximada

# Define a função principal que controla o fluxo do programa
def main():
    """
    Função principal que controla o fluxo do programa.
    
    Executa as seguintes etapas:
    1. Exibe uma mensagem de boas-vindas.
    2. Informa ao usuário sobre a função definida.
    3. Solicita ao usuário os limites do intervalo [a, b].
    4. Solicita ao usuário a precisão desejada.
    5. Executa o Método da Bissecção para encontrar a raiz.
    6. Exibe o resultado final.
    7. Termina o programa.
    """
    # Exibe uma mensagem de boas-vindas e informações iniciais
    print("===========================================")
    print("   CALCULADORA DE RAÍZES - BISSECCÃO")
    print("===========================================\n")

    # Informa ao usuário sobre a função definida
    print("Por favor, defina a função f(x) cuja raiz deseja encontrar.")
    print("Atualmente, a função está definida como:")
    print("f(x) = x^3 - 3x - 1")
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

            # Calcula f(a) e f(b) para verificar a condição do método da bissecção
            fa = f(a)
            fb = f(b)

            # Verifica se f(a) e f(b) têm sinais opostos
            if fa * fb >= 0:
                print("f(a) e f(b) devem ter sinais opostos. O método da bissecção não pode ser aplicado neste intervalo.\n")
                print(f"f(a) = f({a}) = {fa}")
                print(f"f(b) = f({b}) = {fb}\n")
                continue  # Reinicia o loop para nova entrada

            # Se tudo estiver correto, sai do loop
            break

        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite números válidos.\n")

    # Solicita ao usuário a precisão desejada para o cálculo
    while True:
        try:
            # Solicita a precisão desejada
            e = float(input("Digite a precisão desejada (exemplo: 0.001): "))
            
            # Verifica se a precisão é um número positivo
            if e <= 0:
                print("A precisão deve ser um número positivo. Tente novamente.\n")
                continue  # Reinicia o loop para nova entrada

            # Se tudo estiver correto, sai do loop
            break

        except ValueError:
            # Trata casos onde a entrada não é um número válido
            print("Entrada inválida. Por favor, digite um número válido.\n")

    # Executa o Método da Bissecção para encontrar a raiz
    try:
        # Chama a função bisseccao com os parâmetros fornecidos
        raiz = bisseccao(a, b, e)
        # Exibe a raiz aproximada encontrada
        print(f"A raiz aproximada de f(x) no intervalo [{a}, {b}] é: {raiz}")
    except ValueError as ve:
        # Trata erros levantados pela função bisseccao
        print(f"Erro: {ve}")

    # Exibe uma mensagem de encerramento
    print("===========================================")
    print("       FIM DA CALCULADORA DE RAÍZES")
    print("===========================================\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
