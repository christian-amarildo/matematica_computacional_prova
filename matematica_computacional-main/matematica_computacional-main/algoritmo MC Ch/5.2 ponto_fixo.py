# -*- coding: utf-8 -*-
"""
Calculadora de Raízes pelo Método de Ponto Fixo
=============================================

Este programa encontra a raiz de uma função contínua utilizando o Método de Ponto Fixo.

Funcionalidades:
1. Definição interativa da função g(x).
2. Entrada do ponto inicial x0.
3. Definição do critério de precisão.
4. Exibição detalhada de cada iteração do método.
5. Retorno da raiz aproximada com a precisão especificada.

Autor: ChatGPT
Data: 2025-01-27
"""

import math  # Importa o módulo math para funções matemáticas adicionais

def g(x):
    """
    Define a função g(x) utilizada no Método de Ponto Fixo.
    
    Parâmetros:
        x (float): O valor de x onde a função será avaliada.
    
    Retorna:
        float: O valor de g(x).
    
    Nota:
        - Modifique esta função conforme necessário para diferentes problemas.
        - Certifique-se de que a função g(x) está na forma x = g(x).
        - Exemplo:
            Para f(x) = x^3 - 9x + 3, uma possível g(x) é g(x) = (9x - 3)^(1/3)
    """
    # Exemplo de g(x). Modifique conforme necessário.
    # Vamos usar g(x) = (9*x - 3) ** (1/3) para resolver f(x) = x^3 - 9x + 3
    try:
        return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)  # Modifique esta linha conforme a função desejada
    
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero ocorreu ao calcular g(x).")
    except OverflowError:
        raise OverflowError("Overflow ocorreu ao calcular g(x).")
    except ValueError:
        raise ValueError(f"Valor inválido calculado em g(x) para x = {x}.")

def metodo_ponto_fixo(g_func, x0, epsilon=1e-6, max_iter=1000):
    """
    Implementa o Método de Ponto Fixo para encontrar a raiz de uma função f(x).

    Parâmetros:
        g_func (function): Função g(x) utilizada na iteração, tal que x = g(x).
        x0 (float): Ponto inicial para iniciar as iterações.
        epsilon (float): Critério de parada baseado na diferença entre iterações consecutivas.
        max_iter (int): Número máximo de iterações para evitar loops infinitos.

    Retorna:
        tuple: (raiz aproximada, número de iterações)

    Levanta:
        ValueError: Se o método não converge dentro do número máximo de iterações.
    """
    iteracao = 0  # Inicializa o contador de iterações
    x_atual = x0  # Define o ponto inicial

    print("\nIniciando o Método de Ponto Fixo...")
    print(f"Ponto inicial: x0 = {x_atual}")
    print(f"Critério de parada (erro): {epsilon}")
    print(f"Máximo de iterações: {max_iter}\n")

    while iteracao < max_iter:
        try:
            x_novo = g_func(x_atual)  # Calcula x_{n+1} = g(x_n)
        except Exception as e:
            # Trata quaisquer erros durante o cálculo de g(x)
            print(f"Erro na iteração {iteracao}: {e}")
            raise

        diff = abs(x_novo - x_atual)  # Calcula a diferença entre iterações
        print(f"Iteração {iteracao}: x = {x_atual:.10f}, g(x) = {x_novo:.10f}, |g(x) - x| = {diff:.10f}")

        if diff < epsilon:
            # Critério de parada atendido
            print("\nConvergência alcançada pelo Método de Ponto Fixo.\n")
            return (x_novo, iteracao)

        # Atualiza o ponto atual para a próxima iteração
        x_atual = x_novo
        iteracao += 1  # Incrementa o contador de iterações

    # Se o método não convergir dentro do número máximo de iterações
    raise ValueError("O método de ponto fixo não convergiu dentro do número máximo de iterações.")

def main():
    """
    Função principal que controla o fluxo do programa.

    Executa as seguintes etapas:
    1. Exibe uma mensagem de boas-vindas.
    2. Solicita ao usuário a definição da função g(x).
    3. Solicita ao usuário o ponto inicial x0.
    4. Solicita ao usuário o critério de precisão.
    5. Executa o Método de Ponto Fixo para encontrar a raiz.
    6. Exibe o resultado final.
    7. Termina o programa.
    """
    # Exibe uma mensagem de boas-vindas e informações iniciais
    print("===========================================")
    print("      CALCULADORA DE RAÍZES - PONTO FIXO")
    print("===========================================\n")

    # Informa ao usuário sobre a função g(x)
    print("Por favor, defina a função g(x) utilizada no Método de Ponto Fixo.")
    print("A função g(x) deve estar isolada em x, ou seja, na forma x = g(x).")
    print("Exemplos:")
    print("1. Para f(x) = x^3 - 9x + 3, uma possível g(x) é g(x) = (9x - 3)^(1/3)")
    print("2. Para f(x) = x * log10(x) - 1, uma possível g(x) é g(x) = x - 1.3*(x * log10(x) - 1)\n")

    print("Por favor, edite a função 'g(x)' diretamente no código para resolver o seu problema específico.\n")

    # Solicita ao usuário o ponto inicial x0
    while True:
        try:
            x0_input = input("Digite o ponto inicial (x0) para iniciar as iterações: ")
            x0 = float(x0_input)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para x0.\n")

    # Solicita ao usuário a precisão desejada
    while True:
        try:
            epsilon_input = input("Digite a precisão desejada para a convergência (exemplo: 1e-6): ")
            epsilon = float(epsilon_input)
            if epsilon <= 0:
                print("A precisão deve ser um número positivo. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para a precisão.\n")

    # Define o número máximo de iterações para evitar loops infinitos
    max_iter = 1000  # Você pode ajustar esse valor conforme necessário

    # Executa o Método de Ponto Fixo para encontrar a raiz
    try:
        raiz, iteracoes = metodo_ponto_fixo(g, x0, epsilon, max_iter)
        print(f"Resultado: A raiz aproximada de f(x) pelo Método de Ponto Fixo é: {raiz:.10f}")
    except ValueError as ve:
        # Trata erros como falta de convergência
        print(f"\nErro: {ve}")
    except Exception as ex:
        # Trata quaisquer outros erros inesperados
        print(f"\nOcorreu um erro inesperado: {ex}")

    # Exibe uma mensagem de encerramento
    print("===========================================")
    print("       FIM DA CALCULADORA DE RAÍZES")
    print("===========================================\n")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
