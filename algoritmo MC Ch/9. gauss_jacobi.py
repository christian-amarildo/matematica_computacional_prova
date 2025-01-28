# -*- coding: utf-8 -*-
"""
Calculadora de Sistemas Lineares pelo Método de Gauss-Jacobi
===========================================================

Este programa resolve sistemas de equações lineares da forma Ax = b utilizando o
Método de Gauss-Jacobi. O método é iterativo e depende de um chute inicial para
convergência.

Funcionalidades:
1. Definição da matriz de coeficientes A e do vetor de constantes b.
2. Entrada dos critérios de precisão e número máximo de iterações.
3. Execução do Método de Gauss-Jacobi com exibição detalhada de cada iteração.
4. Validação e tratamento de erros, como matrizes não quadradas ou divisão por zero.
5. Exibição da solução aproximada após convergência ou término das iterações.

Autor: ChatGPT
Data: 2025-01-27
"""

def gauss_jacobi(A, b, e, max_i):
    """
    Método iterativo de Gauss-Jacobi para resolver um sistema linear Ax = b.

    Parâmetros:
        A (list of list of floats): Matriz de coeficientes (n x n).
        b (list of floats): Vetor de constantes (tamanho n).
        e (float): Precisão desejada (erro máximo aceitável).
        max_i (int): Número máximo de iterações permitidas.

    Retorna:
        list of floats: Vetor solução x após a convergência ou após max_i iterações.
    """
    
    n = len(b)  # n é o número de equações, igual ao tamanho do vetor b.

    # Verificação se a matriz A é quadrada (n x n).
    for idx, row in enumerate(A):
        if len(row) != n:
            raise ValueError(f"A matriz deve ser quadrada. Linha {idx + 1} tem {len(row)} colunas.")

    # Inicializando o vetor de soluções com zeros.
    x = [0.0] * n  # x armazena a solução atual, iniciada com zeros.

    # Inicializando o vetor x_novo, que armazenará os novos valores calculados.
    x_novo = [0.0] * n  # x_novo irá armazenar a solução calculada na iteração atual.

    print("\n=== MÉTODO DE GAUSS-JACOBI ===\n")
    print("Sistema linear a ser resolvido:")
    for i in range(n):
        eq = ""
        for j in range(n):
            eq += f"{A[i][j]}x{j + 1} + "  # Constrói a parte esquerda da equação.
        eq = eq.rstrip(" + ") + f" = {b[i]}"  # Remove o último " + " e adiciona "= b[i]".
        print(eq)  # Imprime a equação.

    print(f"\nChute inicial: {x}")
    print(f"Critério de parada: Erro < {e}")
    print(f"Número máximo de iterações: {max_i}\n")

    # Loop principal que executa as iterações do método de Gauss-Jacobi.
    for k in range(1, max_i + 1):
        print(f"--- Iteração {k} ---")
        
        # Atualiza cada variável no vetor x_novo.
        for i in range(n):
            soma = b[i]  # Inicia a soma com o termo independente b[i].

            # Soma os produtos de A[i][j] * x[j] para todas as j ≠ i.
            for j in range(n):
                if i != j:
                    soma -= A[i][j] * x[j]  # Subtrai A[i][j] * x[j] da soma.

            # Calcula o novo valor para x[i] dividindo a soma pela diagonal A[i][i].
            if A[i][i] == 0:
                raise ZeroDivisionError(f"A diagonal A[{i}][{i}] é zero. Método falhou.")

            x_novo[i] = soma / A[i][i]  # Atualiza o valor de x_novo[i].

            print(f"x{ i +1 } (novo) = {x_novo[i]:.6f}")  # Exibe o novo valor calculado.

        # Calcula o erro total como a soma das diferenças absolutas entre x_novo e x.
        e_total = sum(abs(x_novo[i] - x[i]) for i in range(n))

        print(f"Erro total após a iteração {k}: {e_total:.6f}\n")

        # Verifica se o erro total está abaixo do critério de parada.
        if e_total < e:
            print("Convergência alcançada.")
            print(f"Solução aproximada após {k} iterações: {x_novo}\n")
            return x_novo  # Retorna a solução encontrada.

        # Atualiza o vetor x com os valores de x_novo para a próxima iteração.
        x = x_novo.copy()

    # Se o método não convergir dentro do número máximo de iterações, exibe uma mensagem.
    print("Número máximo de iterações atingido sem convergência.")
    print(f"Solução após {max_i} iterações: {x}\n")
    return x_novo  # Retorna a última aproximação encontrada.

def main():
    """
    Função principal que controla o fluxo do programa.
    
    Executa as seguintes etapas:
    1. Define a matriz de coeficientes A e o vetor de constantes b.
    2. Solicita ao usuário os critérios de precisão e número máximo de iterações.
    3. Executa o Método de Gauss-Jacobi para resolver o sistema.
    4. Exibe a solução encontrada.
    """
    # Exemplo de sistema linear 3x3:
    # 10x1 + 2x2 + x3 = 7
    # x1 + 5x2 + x3 = -8
    # 2x1 + 3x2 + 10x3 = 6
    A = [
        [10, 2, 1],
        [1, 5, 1],
        [2, 3, 10]
    ]
    
    # Vetor de constantes do sistema linear
    b = [7, -8, 6]
    
    print("=== RESOLUÇÃO DE SISTEMAS LINEARES COM GAUSS-JACOBI ===\n")
    
    # Define a precisão desejada para o erro
    while True:
        try:
            e = float(input("Digite a precisão desejada (erro máximo, por exemplo, 1e-6): "))
            if e <= 0:
                print("A precisão deve ser um número positivo. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.\n")
    
    # Define o número máximo de iterações permitidas
    while True:
        try:
            max_i = int(input("Digite o número máximo de iterações permitidas (por exemplo, 100): "))
            if max_i <= 0:
                print("O número máximo de iterações deve ser um inteiro positivo. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.\n")
    
    # Executa o Método de Gauss-Jacobi
    try:
        solução = gauss_jacobi(A, b, e, max_i)  # Chama a função gauss_jacobi com os parâmetros fornecidos.
        print("=== SOLUÇÃO DO SISTEMA ===")
        for i, valor in enumerate(solução, start=1):
            print(f"x{i} = {valor:.6f}")  # Exibe cada variável com 6 casas decimais.
    except ZeroDivisionError as zde:
        # Trata o caso onde ocorre divisão por zero durante as iterações.
        print(f"\nErro: {zde}\n")
    except ValueError as ve:
        # Trata erros relacionados à estrutura da matriz.
        print(f"\nErro: {ve}\n")
    except Exception as e:
        # Trata quaisquer outros erros inesperados.
        print(f"\nOcorreu um erro inesperado: {e}\n")
    
    print("\n=== FIM DA RESOLUÇÃO ===")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
