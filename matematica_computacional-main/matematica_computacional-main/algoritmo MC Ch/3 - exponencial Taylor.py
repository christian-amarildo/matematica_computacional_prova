# Importa a biblioteca `math`, que fornece funções matemáticas avançadas como fatoriais e exponenciais.
import math

# Define a função `calcular_ex_serie` para calcular e^x usando a série de Taylor.
def calcular_ex_serie(x, n):
    """
    Calcula e^x usando a série de Taylor com n termos.
    A série é dada por: e^x = Σ (x^k / k!) de k = 0 até k = n.
    """
    resultado = 0  # Inicializa o resultado como 0, que será acumulado.
    for k in range(n + 1):  # Itera de k = 0 até k = n (inclusive).
        # Calcula o termo atual da série: (x^k) / (k!)
        termo = (x ** k) / math.factorial(k)
        # Adiciona o termo ao resultado acumulado.
        resultado += termo
    # Retorna o valor final de e^x calculado com n termos.
    return resultado

# Define a função `calcular_ex_negativo` para lidar com valores negativos de x.
def calcular_ex_negativo(x, n):
    """
    Calcula e^x para x < 0 de duas formas:
    1. Usando o x diretamente na série de Taylor.
    2. Usando a relação e^(-x) = 1 / e^(x).
    """
    # Calcula e^x diretamente usando a série de Taylor.
    ex_direto = calcular_ex_serie(x, n)

    # Calcula e^x indiretamente: define y = -x e usa 1 / e^(-x).
    y = -x  # Converte x para positivo para facilitar o cálculo da série.
    ex_indireto = 1 / calcular_ex_serie(y, n)  # Aplica a relação inversa.

    # Retorna ambos os resultados: o direto e o indireto.
    return ex_direto, ex_indireto

# Define a função `testar_valores` para testar diferentes valores de x e n.
def testar_valores():
    # Exibe uma mensagem introdutória explicando o propósito do teste.
    print("Cálculo de e^x utilizando a série de Taylor\n")

    # Define uma lista de valores de x a serem testados (incluindo positivos e negativos).
    valores_x = [0, 1, -1, 2, -2, 5, -5]

    # Define uma lista de valores de n (número de termos na série).
    valores_n = [5, 10, 20]

    # Loop externo para iterar sobre cada valor de x.
    for x in valores_x:
        # Loop interno para iterar sobre cada valor de n para o x atual.
        for n in valores_n:
            # Exibe os valores atuais de x e n sendo testados.
            print(f"x = {x}, n = {n}")
            if x >= 0:  # Verifica se x é não-negativo.
                # Calcula e^x diretamente usando a série de Taylor.
                resultado = calcular_ex_serie(x, n)
                # Exibe o resultado formatado com 10 casas decimais.
                print(f"e^{x} (usando série): {resultado:.10f}")
            else:  # Se x for negativo, usa as duas abordagens.
                direto, indireto = calcular_ex_negativo(x, n)
                # Exibe o resultado direto da série de Taylor.
                print(f"e^{x} (usando série diretamente): {direto:.10f}")
                # Exibe o resultado usando a relação 1/e^(-x).
                print(f"e^{x} (usando 1/e^-x): {indireto:.10f}")
            # Adiciona uma linha em branco para separar os resultados.
            print()

# Define a função `calcular_ex_taylor` para calcular e^x sem overflow, usando tolerância.
def calcular_ex_taylor(x, epsilon=1e-15):
    """
    Calcula e^x usando a série de Taylor, parando quando o termo atual é menor que epsilon.
    """
    termo = 1  # Define o primeiro termo da série: x^0 / 0! = 1.
    soma = termo  # Inicializa a soma com o valor do primeiro termo.
    k = 1  # Define o índice do próximo termo (começando em 1).

    # Enquanto o valor absoluto do termo atual for maior que epsilon (tolerância), continua a soma.
    while abs(termo) > epsilon:
        # Calcula o próximo termo da série usando o termo anterior.
        termo = termo * x / k  # Isso evita o cálculo repetitivo de potências e fatoriais.
        soma += termo  # Adiciona o termo atual à soma acumulada.
        k += 1  # Incrementa o índice para o próximo termo.

    # Retorna o valor final da soma e o número total de termos usados.
    return soma, k - 1

# Bloco principal do programa: executa o código somente se for chamado diretamente.
if __name__ == "__main__":
    # Chama a função para testar os valores de x e n.
    testar_valores()

    # Define uma lista adicional de valores de x para teste com a função `calcular_ex_taylor`.
    valores_x = [0, 1, -1, 2, -2, 10, -10]
    epsilon = 1e-15  # Define a tolerância para o cálculo (precisão desejada).
    for x in valores_x:  # Itera sobre cada valor de x.
        # Calcula e^x usando a função `calcular_ex_taylor` e obtém o número de termos usados.
        resultado, n_termos = calcular_ex_taylor(x, epsilon)
        # Exibe o resultado com 15 casas decimais e o número de termos necessários.
        print(f"x = {x}, e^x = {resultado:.15f}, termos usados = {n_termos}")

"""
Análise dos Resultados:
=======================
1. Precisão com n:
   - Para valores de x próximos a 0, mesmo valores baixos de n fornecem resultados precisos.
   - Para valores maiores de |x|, o erro se torna significativo com n pequeno.

2. Cálculo com x < 0:
   - Usar 1/e^{-x} é geralmente mais preciso para valores negativos grandes (|x| alto),
     pois evita somas acumulativas que podem introduzir erros numéricos.

3. Erro relativo:
   - Comparando os métodos para x < 0, a diferença entre os dois métodos é pequena,
     mas perceptível quando n é baixo e x é grande em valor absoluto.

4. Vantagem da série de Taylor:
   - A série de Taylor é eficiente e fácil de implementar para calcular e^x,
     mas a precisão depende diretamente do número de termos (n).

5. Consideração para grandes valores de |x|:
   - Para valores muito grandes de |x|, a precisão numérica do ponto flutuante
     pode causar erros consideráveis. Nestes casos, métodos alternativos ou bibliotecas
     de precisão estendida podem ser necessários.
"""
