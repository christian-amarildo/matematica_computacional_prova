# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método da Bissecção
=============================================

Este programa encontra a raiz de uma função contínua utilizando o Método da Bissecção.

Funcionalidades:
1. Definição interativa da função f(x).
2. Entrada dos limites do intervalo [a, b].
3. Definição da precisão desejada.
4. Exibição detalhada de cada iteração do método.
5. Retorno da raiz aproximada com a precisão especificada.


"""

import math  # Importa a biblioteca matemática para funções como logaritmo e seno

def f(x):
    """
    Define a função f(x) cuja raiz será buscada.

    Parâmetros:
        x (float): O valor de x onde a função será avaliada.

    Retorna:
        float: O valor de f(x).

    Nota:
        - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
        - Exemplo de função correta:
            f(x) = x * ln(x) + x^2 - x^3 * sin(x)
    """
    if x <= 0:
        # Levanta uma exceção se x for menor ou igual a 0, pois logaritmo natural não está definido para x <= 0
        raise ValueError("x deve ser maior que 0 para calcular x * ln(x).")
    # Retorna o valor da função f(x)
    return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)  # Exemplo de função. Modifique conforme necessário.

def bisseccao(a, b, e, max_iter=1000):
    """
    Método da Bissecção para encontrar a raiz de f(x) no intervalo [a, b].

    Parâmetros:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        e (float): Precisão desejada para o cálculo.
        max_iter (int): Número máximo de iterações permitidas.

    Retorna:
        tuple: (raiz aproximada, número de iterações)

    Levanta:
        ValueError: Se f(a) * f(b) >= 0, indicando que não há garantia de raiz no intervalo.
    """

    # Calcula f(a) e f(b) para verificar a condição inicial
    fa = f(a)  # Valor da função no limite inferior
    fb = f(b)  # Valor da função no limite superior

    # Exibe os valores iniciais de f(a) e f(b)
    print(f"Verificando o intervalo inicial:")
    print(f"f(a) = f({a}) = {fa}")
    print(f"f(b) = f({b}) = {fb}\n")

    # Verifica se f(a) e f(b) têm sinais opostos
    if fa * fb >= 0:
        # Se não tiverem sinais opostos, o método da Bissecção não pode ser aplicado
        raise ValueError(f"O método da Bissecção não pode ser aplicado no intervalo [{a}, {b}].\n"
                         f"f(a) = f({a}) = {fa} e f(b) = f({b}) = {fb} não têm sinais opostos.")

    # Inicializa o contador de iterações
    iteracao = 1

    # Define os limites atuais do intervalo como a e b
    ai = a  # Limite inferior atual
    bi = b  # Limite superior atual

    # Exibe informações iniciais sobre o método
    print("Iniciando o Método da Bissecção:")
    print(f"Função definida: f(x) = x * ln(x) + x^2 - x^3 * sin(x)")
    print(f"Intervalo inicial: [{ai}, {bi}]")
    print(f"Precisão desejada: {e}\n")

    # Loop principal do método da Bissecção
    while abs(bi - ai) > e:
        # Calcula o ponto médio do intervalo atual
        ci = (ai + bi) / 2
        fci = f(ci)  # Calcula f(ci)

        # Exibe os detalhes da iteração atual
        print(f"Iteração {iteracao}:")
        print(f"  a{iteracao} = {ai}")        # Limite inferior atual
        print(f"  b{iteracao} = {bi}")        # Limite superior atual
        print(f"  c{iteracao} = {ci}")        # Ponto médio atual
        print(f"  f(c{iteracao}) = {fci}")    # Valor da função no ponto médio

        # Verifica se f(ci) é exatamente zero ou se a precisão foi alcançada
        if fci == 0 or (bi - ai) / 2 < e:
            # Se sim, a raiz foi encontrada dentro da precisão desejada
            print("\nConvergência alcançada pelo Método da Bissecção.\n")
            return (ci, iteracao)  # Retorna a raiz aproximada e o número de iterações

        # Decide em qual subintervalo a raiz está localizada
        if fa * fci < 0:
            # Se f(a) e f(ci) têm sinais opostos, a raiz está no intervalo [ai, ci]
            bi = ci          # Atualiza o limite superior para o ponto médio
            fb = fci         # Atualiza f(bi) para o novo limite superior
            print(f"  A raiz está no intervalo [{ai}, {ci}].\n")
        else:
            # Caso contrário, a raiz está no intervalo [ci, bi]
            ai = ci          # Atualiza o limite inferior para o ponto médio
            fa = fci         # Atualiza f(ai) para o novo limite inferior
            print(f"  A raiz está no intervalo [{ci}, {bi}].\n")

        # Incrementa o contador de iterações
        iteracao += 1

        # Verifica se o número máximo de iterações foi atingido
        if iteracao > max_iter:
            # Se sim, informa que o método atingiu o máximo de iterações sem convergência
            print("Número máximo de iterações atingido sem convergência pelo Método da Bissecção.\n")
            return (ci, iteracao - 1)  # Retorna a última aproximação e o número de iterações realizadas

    # Calcula a raiz aproximada como o ponto médio final do intervalo
    raiz_aproximada = (ai + bi) / 2
    # Exibe os resultados finais após a conclusão do método
    print(f"Raiz aproximada após {iteracao - 1} iterações: {raiz_aproximada}")
    print(f"Intervalo final: [{ai}, {bi}]")
    print(f"f({raiz_aproximada}) = {f(raiz_aproximada)}\n")

    # Retorna a raiz aproximada encontrada e o número de iterações
    return (raiz_aproximada, iteracao - 1)

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
    print("f(x) = x * ln(x) + x^2 - x^3 * sin(x)")
    print("Se desejar modificar a função, edite a função f(x) diretamente no código.\n")

    # Solicita ao usuário os limites do intervalo [a, b]
    while True:
        try:
            # Solicita o limite inferior do intervalo
            a_input = input("Digite o limite inferior do intervalo (a): ")
            a = float(a_input)  # Converte a entrada para float

            # Solicita o limite superior do intervalo
            b_input = input("Digite o limite superior do intervalo (b): ")
            b = float(b_input)  # Converte a entrada para float

            # Verifica se a <= b
            if a >= b:
                # Se não, informa ao usuário e reinicia o loop para nova entrada
                print("O limite inferior deve ser menor que o limite superior. Tente novamente.\n")
                continue  # Reinicia o loop para nova entrada

            # Calcula f(a) e f(b) para verificar a condição do método da Bissecção
            fa = f(a)
            fb = f(b)

            # Verifica se f(a) e f(b) têm sinais opostos
            if fa * fb >= 0:
                # Se não tiverem sinais opostos, informa ao usuário e reinicia o loop
                print("f(a) e f(b) devem ter sinais opostos. O método da Bissecção não pode ser aplicado neste intervalo.\n")
                print(f"f(a) = f({a}) = {fa}")
                print(f"f(b) = f({b}) = {fb}\n")
                continue  # Reinicia o loop para nova entrada

            # Se tudo estiver correto, sai do loop
            break

        except ValueError as ve:
            # Trata casos onde a entrada não é um número válido ou x <= 0
            print(f"Entrada inválida: {ve}. Por favor, digite números válidos e x > 0.\n")

    # Solicita ao usuário a precisão desejada para o cálculo
    while True:
        try:
            # Solicita a precisão desejada
            e_input = input("Digite a precisão desejada (por exemplo, 0.000001): ")
            e = float(e_input)  # Converte a entrada para float

            # Verifica se a precisão é um número positivo
            if e <= 0:
                # Se não, informa ao usuário e reinicia o loop para nova entrada
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
        raiz, iteracoes = bisseccao(a, b, e)
        # Exibe a raiz aproximada encontrada
        print(f"Raiz encontrada: {raiz}")
        print(f"f({raiz}) = {f(raiz)}")
        print(f"Número de iterações realizadas: {iteracoes}\n")
    except ValueError as ve:
        # Trata erros levantados pela função bisseccao
        print(f"Erro: {ve}\n")
    except Exception as ex:
        # Trata quaisquer outros erros inesperados
        print(f"Ocorreu um erro inesperado: {ex}\n")

    # Exibe uma mensagem de encerramento
    print("===========================================")
    print("       FIM DA CALCULADORA DE RAÍZES")
    print("===========================================\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa