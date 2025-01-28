# Define uma função para demonstrar o erro de overflow.
def erro_overflow():
    # Importa o módulo `math` que contém funções matemáticas avançadas.
    import math
    try:
        # Tenta calcular o número `e^1000` (exponencial com base `e` elevado a 1000).
        grande_numero = math.exp(1000)  # O resultado esperado é um número muito grande, que pode causar um overflow.
        print(f"Número muito grande: {grande_numero}")  # Exibe o número calculado, se possível.
    except OverflowError:
        # Captura a exceção de overflow, que ocorre quando o número é muito grande para ser representado.
        print("Erro de Overflow detectado! O número é muito grande para ser representado.")  # Exibe uma mensagem informando o erro.

# Define uma função para demonstrar o erro de arredondamento.
def erro_arredondamento():
    # Representação imprecisa de números de ponto flutuante.
    # Python usa a especificação IEEE 754 para representar números de ponto flutuante, o que pode causar imprecisões.
    numero1 = 0.1  # Define o primeiro número de ponto flutuante como 0.1.
    numero2 = 0.2  # Define o segundo número de ponto flutuante como 0.2.
    resultado = numero1 + numero2  # Soma os dois números de ponto flutuante.
    # Exibe o resultado da soma e compara com o valor esperado (0.3).
    print(f"Esperado: 0.3, Obtido: {resultado}")
    # Explica que o erro ocorre devido à representação imprecisa dos números em ponto flutuante.
    print("Erro de arredondamento detectado devido à precisão limitada dos floats.")

# Verifica se o script está sendo executado diretamente (não como um módulo importado).
if __name__ == "__main__":
    # Exibe um título explicativo para o programa.
    print("Demonstrando erros de Overflow e Arredondamento\n")

    # Exibe o título da primeira demonstração: erro de overflow.
    print("1. Erro de Overflow:")
    # Chama a função que demonstra o erro de overflow.
    erro_overflow()

    # Adiciona uma linha em branco para separar as demonstrações.
    print("\n2. Erro de Arredondamento:")
    # Chama a função que demonstra o erro de arredondamento.
    erro_arredondamento()
