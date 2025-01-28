# Define a função `precisao_maquina` que calcula a precisão da máquina.
def precisao_maquina(referencia=1):
    """
    Calcula a precisão da máquina baseada no algoritmo descrito.
    - referência: valor de referência para a comparação no passo 2.
    """
    A = 1.0  # Inicializa A como 1.0, o valor inicial da precisão em ponto flutuante.
    s = referencia + A  # Soma a referência com A para verificar a alteração no valor.
    while s > referencia:  # Enquanto a soma ainda for maior que a referência...
        A = A / 2  # Divide A por 2 para encontrar um valor menor.
        s = referencia + A  # Atualiza a soma para verificar se A ainda afeta a referência.
    precisao = 2 * A  # Multiplica o último valor de A por 2 para obter a menor precisão detectável.
    return precisao  # Retorna a precisão calculada.

# Define a função `testar_precisao` para testar a precisão da máquina em diferentes condições.
def testar_precisao():
    print("Teste da Precisão da Máquina:\n")  # Mensagem inicial explicativa.

    # a) Teste para precisão simples.
    print("Teste com precisão simples:")  # Indica que o teste será com a precisão padrão.
    precisao_simples = precisao_maquina()  # Calcula a precisão usando o valor padrão de referência (1.0).
    print(f"Precisão simples (referência = 1): {precisao_simples:.10e}")  # Exibe o resultado formatado em notação científica.

    # b) Teste para precisão dupla (simulada usando numpy).
    print("\nTeste com precisão dupla (simulada):")  # Mensagem indicando o próximo teste.
    import numpy as np  # Importa o módulo numpy para usar tipos de ponto flutuante específicos.
    A = np.float64(1.0)  # Inicializa A com o tipo float64 para maior precisão.
    referencia = 1.0  # Define a referência como 1.0.
    s = referencia + A  # Soma a referência com A.
    while s > referencia:  # Enquanto a soma for maior que a referência...
        A = A / 2  # Divide A por 2 para encontrar a menor alteração detectável.
        s = referencia + A  # Atualiza a soma.
    precisao_dupla = 2 * A  # Calcula a precisão como o dobro do último valor de A.
    print(f"Precisão dupla (referência = 1): {precisao_dupla:.20e}")  # Exibe o resultado formatado com maior precisão.

    # c.1) Teste para valores diferentes de referência.
    valores_referencia = [10, 17, 100, 184, 1000, 1575, 10000, 17893]  # Lista de valores de referência para teste.
    print("\nTeste com valores de referência diferentes:")  # Mensagem indicando os testes com valores variados.
    for ref in valores_referencia:  # Itera sobre cada valor na lista de referências.
        prec = precisao_maquina(ref)  # Calcula a precisão para a referência atual.
        print(f"Referência: {ref}, Precisão: {prec:.10e}")  # Exibe o valor da referência e a precisão calculada.

# Bloco principal que executa o código apenas se o arquivo for executado diretamente.
if __name__ == "__main__":
    testar_precisao()  # Chama a função para realizar todos os testes.

"""
Análise do Código:
===================
1. Função `precisao_maquina`:
   - Baseada no conceito de precisão da máquina, a função detecta o menor valor que,
     somado à referência, ainda resulta em uma alteração perceptível no valor.

2. Passo-a-passo do algoritmo:
   - Inicializa o valor A com 1.0 e soma à referência.
   - Divide A sucessivamente por 2 até que a soma não afete mais a referência.
   - Retorna o dobro do último valor de A como a menor unidade significativa.

3. Teste com precisão simples:
   - A precisão padrão do Python (tipo float) é testada com a referência 1.0.
   - Essa precisão é equivalente à precisão dupla na maioria das implementações modernas.

4. Teste com precisão dupla:
   - Simula maior precisão usando o tipo float64 da biblioteca numpy.
   - Permite uma comparação com a precisão padrão.

5. Teste para valores de referência diferentes:
   - Avalia o impacto de usar referências maiores ou menores no cálculo.
   - Mostra que a precisão da máquina é relativa e depende da capacidade de distinguir diferenças
     proporcionais ao valor de referência.

6. Notação científica:
   - Os resultados são exibidos em notação científica para maior clareza, especialmente para valores muito pequenos.

Conclusão:
- O algoritmo ilustra como a precisão de ponto flutuante é limitada pela arquitetura do sistema.
- Diferentes referências não afetam significativamente o cálculo, indicando que a precisão depende mais do hardware.
"""
