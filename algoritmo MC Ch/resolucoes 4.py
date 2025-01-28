# Erro de Domínio do Logaritmo (x ≤ 0)

# Resolução: Verifique se x está sempre maior que 0 antes de calcular math.log(x). Isso pode ser feito adicionando uma verificação dentro da função f(x) que levanta uma exceção ou retorna um valor específico quando x ≤ 0.


# def f(x):
#     if x <= 0:
#         raise ValueError("x deve ser maior que 0 para calcular x * ln(x).")
#     return x * math.log(x) + x**2 - x**3 * math.sin(x)
# Função Não Definida ou Discontinuidades

# Resolução: Assegure-se de que a função f(x) está definida e contínua no intervalo escolhido. Revise a função para evitar divisões por zero, logaritmos de números negativos ou quaisquer outras operações que possam causar descontinuidades.


# def f(x):
#     try:
#         return x * math.log(x) + x**2 - x**3 * math.sin(x)
#     except Exception as ex:
#         raise ValueError(f"Erro ao avaliar f(x) em x={x}: {ex}")
# Equações com Múltiplas Raízes no Intervalo

# Resolução: Divida o intervalo principal em subintervalos menores e aplique o Método da Bissecção em cada subintervalo onde f(a) e f(b) têm sinais opostos. Isso ajuda a identificar e encontrar cada raiz individualmente.


# def encontrar_subintervalos(a, b, passo=1.0):
#     subintervalos = []
#     inicio = a
#     while inicio < b:
#         fim = inicio + passo
#         if fim > b:
#             fim = b
#         try:
#             fa = f(inicio)
#             fb = f(fim)
#             if fa * fb < 0:
#                 subintervalos.append((inicio, fim))
#         except ValueError:
#             pass
#         inicio = fim
#     return subintervalos
# Ausência de Raiz no Intervalo Escolhido

# Resolução: Antes de aplicar o método, verifique se f(a) e f(b) têm sinais opostos. Se não tiverem, escolha um intervalo diferente ou informe ao usuário que não há garantia de raiz no intervalo atual.


# if fa * fb >= 0:
#     raise ValueError("O método da Bissecção não pode ser aplicado neste intervalo.")
# Sinais Não Opostos em f(a) e f(b)

# Resolução: Similar à resolução anterior, verifique os sinais antes de iniciar o método. Se não forem opostos, ajuste os limites do intervalo ou divida-o em subintervalos menores para encontrar um onde os sinais sejam opostos.


# if fa * fb >= 0:
#     print("Sinais não opostos. Ajustando o intervalo...")
#     # Implementar lógica para ajustar o intervalo ou dividir em subintervalos
# Funções Oscilatórias ou Não Monotônicas

# Resolução: Divida o intervalo em subintervalos menores onde a função seja mais bem comportada (monotônica). Isso facilita a aplicação do Método da Bissecção, evitando oscilações que podem complicar a convergência.


# subintervalos = encontrar_subintervalos(a, b, passo=0.5)
# Precisão Insuficiente ou Excesso de Iterações

# Resolução: Defina uma precisão adequada (e) e um número razoável de iterações máximas (max_iter). Ajuste esses parâmetros conforme a complexidade da função e o intervalo escolhido.


# e = 1e-6  # Precisão desejada
# max_iter = 1000  # Número máximo de iterações
# Divisão por Zero Durante os Cálculos

# Resolução: Embora o Método da Bissecção geralmente não envolva divisões, garanta que a função f(x) não realiza operações que possam resultar em divisão por zero. Adicione verificações dentro de f(x) para evitar isso.


# def f(x):
#     if x == 0:
#         raise ValueError("x não pode ser zero para evitar divisão por zero.")
#     return x * math.log(x) + x**2 - x**3 * math.sin(x)
# Erros de Arredondamento e Precisão de Ponto Flutuante

# Resolução: Utilize bibliotecas como decimal para maior precisão se necessário. Entretanto, para a maioria dos casos, a precisão padrão do  é suficiente.


# import decimal
# from decimal import Decimal, getcontext

# getcontext().prec = 15  # Define a precisão

# def f(x):
#     x = Decimal(x)
#     return x * x.ln() + x**2 - x**3 * Decimal(math.sin(float(x)))
# Overflow ou Underflow Numérico

# Resolução: Monitore os valores de x e f(x) para garantir que não excedam os limites numéricos do . Ajuste o intervalo ou a função se necessário.


# try:
#     resultado = f(x)
# except OverflowError:
#     raise OverflowError(f"Overflow detectado em x={x}.")
# Definição Incorreta da Função f(x)

# Resolução: Revise a implementação de f(x) para garantir que ela corresponda à equação matemática desejada. Teste a função com valores conhecidos para verificar sua correção.


# # Teste básico
# assert f(1.0) == x * math.log(x) + x**2 - x**3 * math.sin(x), "Definição incorreta de f(x)"
# Tratamento Inadequado de Casos de Bordas (f(a) = 0 ou f(b) = 0)

# Resolução: Adicione verificações no início do método para tratar casos onde f(a) == 0 ou f(b) == 0, retornando imediatamente a raiz encontrada.


# if fa == 0:
#     print(f"x = {a} é uma raiz.")
#     return (a, iteracao)
# if fb == 0:
#     print(f"x = {b} é uma raiz.")
#     return (b, iteracao)
# Perda de Significado Numérico em Operações Subtrativas

# Resolução: Minimize subtrações de números de ordem diferente para evitar erros de precisão. Use funções auxiliares ou bibliotecas de precisão quando necessário.


# # Utilize Decimal para subtrações precisas
# from decimal import Decimal
# def f(x):
#     x = Decimal(x)
#     return x * x.ln() + x**2 - x**3 * Decimal(math.sin(float(x)))
# Intervalos Muito Grandes ou Muito Pequenos Impactando a Convergência

# Resolução: Ajuste o tamanho do intervalo e o passo de divisão de subintervalos para equilibrar a velocidade de convergência e a precisão. Evite intervalos excessivamente grandes que possam levar a muitas iterações.


# passo = 0.5  # Tamanho do passo para dividir o intervalo
# subintervalos = encontrar_subintervalos(a, b, passo)
# Implementação Incorreta do Algoritmo de Bissecção

# Resolução: Revise cada passo do algoritmo para garantir que ele segue corretamente os princípios do Método da Bissecção. Teste o método com funções conhecidas para validar a implementação.


# # Teste com f(x) = x^2 - 4 em [1, 3]
# def f_teste(x):
#     return x**2 - 4
# assert bisseccao(1, 3, 1e-6)[0] == 2.0, "Implementação incorreta do Método da Bissecção"
# Falha na Atualização dos Limites do Intervalo Corretamente

# Resolução: Assegure-se de que, após cada iteração, apenas um dos limites (a ou b) é atualizado corretamente com base no sinal de f(c).


# if fa * fci < 0:
#     bi = ci
#     fb = fci
# else:
#     ai = ci
#     fa = fci
# Interrupção Prematura ou Não Prematura do Loop de Iterações

# Resolução: Garanta que as condições de parada (raiz encontrada ou precisão alcançada) estão corretamente implementadas para evitar que o loop termine antes do esperado ou nunca termine.


# if fci == 0 or (bi - ai) / 2 < e:
#     return (ci, iteracao)
# Limitação do Número Máximo de Iterações Sem Convergência

# Resolução: Defina um número razoável de iterações máximas (max_iter) e informe ao usuário se o método não convergir dentro desse limite, possivelmente ajustando os parâmetros ou escolhendo um intervalo diferente.


# if iteracao > max_iter:
#     print("Número máximo de iterações atingido sem convergência.")
#     return (ci, iteracao - 1)
# Erro na Cálculo do Ponto Médio do Intervalo

# Resolução: Verifique a fórmula usada para calcular o ponto médio e assegure-se de que está correta. Utilize operadores de ponto flutuante para precisão adequada.


# ci = (ai + bi) / 2
# Incompatibilidade entre a Função e os Critérios de Convergência

# Resolução: Assegure-se de que os critérios de convergência (precisão e e número de iterações) são apropriados para a função e o intervalo escolhido. Ajuste-os conforme necessário.


# e = 1e-6  # Ajuste conforme a necessidade
# max_iter = 1000  # Ajuste conforme a complexidade da função
# Uso Incorreto de Funções Matemáticas (e.g., ângulos em graus vs. radianos)

# Resolução: Certifique-se de que os argumentos para funções como math.sin estão em radianos. Converta graus para radianos se necessário.


# def f(x):
#     if x <= 0:
#         raise ValueError("x deve ser maior que 0 para calcular x * ln(x).")
#     return x * math.log(x) + x**2 - x**3 * math.sin(math.radians(x))  # Converte graus para radianos
# Falta de Validação das Entradas do Usuário

# Resolução: Implemente verificações robustas para garantir que as entradas do usuário (limites do intervalo e precisão) são válidas e dentro dos parâmetros esperados.


# try:
#     a = float(input("Digite o limite inferior do intervalo (a): "))
#     b = float(input("Digite o limite superior do intervalo (b): "))
#     if a >= b:
#         raise ValueError("a deve ser menor que b.")
#     e = float(input("Digite a precisão desejada (por exemplo, 0.000001): "))
#     if e <= 0:
#         raise ValueError("Precisão deve ser positiva.")
# except ValueError as ve:
#     print(f"Entrada inválida: {ve}")
#     # Reiniciar ou encerrar o programa conforme necessário
# Problemas de Formatação e Exibição dos Resultados

# Resolução: Utilize formatação adequada para exibir os resultados de maneira clara e legível. Por exemplo, limitar o número de casas decimais.


# print(f"Raiz encontrada: {raiz:.6f}")
# print(f"f({raiz:.6f}) = {f(raiz):.6f}")
# Falha ao Manter a Consistência dos Tipos de Dados

# Resolução: Assegure-se de que todas as variáveis utilizadas são do tipo correto (por exemplo, float) e que as operações entre diferentes tipos são realizadas de maneira apropriada.


# a = float(a)
# b = float(b)
# e = float(e)
# Erros de Sintaxe ou Indentação no Código 

# Resolução: Revise o código para garantir que não há erros de sintaxe ou problemas de indentação. Utilize um editor de código que destaque erros ou ferramentas de linting.


# # Utilize ferramentas como pylint ou flake8 para verificar erros
# Falta de Comentários ou Documentação Adequada Facilitando a Manutenção

# Resolução: Mantenha o código bem comentado e documentado, explicando a finalidade de funções e blocos de código. Isso facilita a compreensão e manutenção futura.


# # Exemplo de comentário detalhado
# def f(x):
#     """
#     Calcula f(x) = x * ln(x) + x^2 - x^3 * sin(x)
#     """
#     return x * math.log(x) + x**2 - x**3 * math.sin(x)
# Dependência de Bibliotecas Externas Não Importadas Corretamente

# Resolução: Verifique se todas as bibliotecas necessárias estão importadas corretamente no início do código. Instale quaisquer bibliotecas ausentes usando pip se necessário.


# import math  # Verifique se todas as bibliotecas usadas estão importadas
# Convergência para uma Raiz Não Desejada em Caso de Múltiplas Raízes

# Resolução: Ao dividir o intervalo em subintervalos menores, aplique o método em cada subintervalo individualmente para encontrar todas as raízes presentes.


# subintervalos = encontrar_subintervalos(a, b, passo=0.5)
# for (start, end) in subintervalos:
#     raiz, iteracoes = bisseccao(start, end, e)
#     print(f"Raiz encontrada no subintervalo [{start}, {end}]: {raiz}")
# Falha ao Considerar a Continuidade da Função no Intervalo

# Resolução: Assegure-se de que a função f(x) é contínua no intervalo escolhido. Funções com descontinuidades podem impedir o método de convergir corretamente.


# # Revisar a definição de f(x) para garantir a continuidade
# Problemas de Performance com Intervalos Muito Extensos ou Funções Complexas

# Resolução: Otimize o código para melhorar a performance, como limitar o número de iterações ou ajustar o passo de divisão dos subintervalos. Utilize bibliotecas como NumPy para operações matemáticas mais rápidas se necessário.


# import numpy as np  # Utilize NumPy para cálculos mais eficientes
















# # implementação dos subintervalos

# # -*- coding: utf-8 -*-
# """
# Calculadora de Raízes pelo Método da Bissecção
# =============================================

# Este programa encontra a raiz de uma função contínua utilizando o Método da Bissecção.

# Funcionalidades:
# 1. Definição interativa da função f(x).
# 2. Entrada dos limites do intervalo [a, b].
# 3. Definição da precisão desejada.
# 4. Exibição detalhada de cada iteração do método.
# 5. Retorno da raiz aproximada com a precisão especificada.

# """

# import math  # Importa a biblioteca matemática para funções como logaritmo e seno

# def f(x):
#     """
#     Define a função f(x) cuja raiz será buscada.

#     Parâmetros:
#         x (float): O valor de x onde a função será avaliada.

#     Retorna:
#         float: O valor de f(x).

#     Nota:
#         - Modifique esta função conforme necessário para buscar a raiz de diferentes funções.
#         - Exemplo de função correta:
#             f(x) = x * ln(x) + x^2 - x^3 * sin(x)
#     """
#     # Verifica se x está no domínio da função (x > 0 para log(x))
#     if x <= 0:
#         raise ValueError("x deve ser maior que 0 para calcular x * ln(x).")
#     try:
#         # Calcula e retorna o valor da função
#         return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)  # Exemplo de função. Modifique conforme necessário.
#     except OverflowError:
#         # Trata casos onde x^3 é muito grande, causando overflow
#         raise OverflowError(f"Overflow detectado em x = {x}.")
#     except Exception as ex:
#         # Trata quaisquer outros erros na avaliação da função
#         raise ValueError(f"Erro ao avaliar f(x) em x = {x}: {ex}")

# def encontrar_subintervalos(a, b, passo=1.0):
#     """
#     Encontra subintervalos dentro de [a, b] onde f(a) * f(b) < 0.

#     Parâmetros:
#         a (float): Limite inferior do intervalo principal.
#         b (float): Limite superior do intervalo principal.
#         passo (float): Tamanho do passo para dividir o intervalo.

#     Retorna:
#         list of tuples: Lista de subintervalos (a, b) onde f(a) * f(b) < 0.

#     Nota:
#         - Ajuste o valor de 'passo' conforme a complexidade da função e o tamanho do intervalo.
#     """
#     subintervalos = []  # Lista para armazenar os subintervalos válidos
#     inicio = a  # Inicia no limite inferior

#     while inicio < b:
#         fim = inicio + passo  # Define o limite superior do subintervalo
#         if fim > b:
#             fim = b  # Ajusta se ultrapassar o limite superior principal
#         try:
#             fa = f(inicio)  # Calcula f(a) no início do subintervalo
#             fb = f(fim)     # Calcula f(b) no fim do subintervalo
#             if fa * fb < 0:
#                 subintervalos.append((inicio, fim))  # Adiciona subintervalo válido
#         except ValueError:
#             # Ignora subintervalos onde a função não está definida ou ocorre erro
#             pass
#         inicio = fim  # Move para o próximo subintervalo

#     return subintervalos  # Retorna a lista de subintervalos válidos

# def bisseccao(a, b, e, max_iter=1000):
#     """
#     Método da Bissecção para encontrar a raiz de f(x) no intervalo [a, b].

#     Parâmetros:
#         a (float): Limite inferior do intervalo.
#         b (float): Limite superior do intervalo.
#         e (float): Precisão desejada para o cálculo.
#         max_iter (int): Número máximo de iterações permitidas.

#     Retorna:
#         tuple: (raiz aproximada, número de iterações)

#     Levanta:
#         ValueError: Se f(a) * f(b) >= 0, indicando que não há garantia de raiz no intervalo.
#     """

#     # Calcula f(a) e f(b) para verificar a condição inicial
#     fa = f(a)  # Valor da função no limite inferior
#     fb = f(b)  # Valor da função no limite superior

#     # Exibe os valores iniciais de f(a) e f(b)
#     print(f"Verificando o intervalo inicial:")
#     print(f"f(a) = f({a}) = {fa}")
#     print(f"f(b) = f({b}) = {fb}\n")

#     # Verifica se f(a) e f(b) têm sinais opostos
#     if fa * fb >= 0:
#         # Se não tiverem sinais opostos, o método da Bissecção não pode ser aplicado
#         raise ValueError(f"O método da Bissecção não pode ser aplicado no intervalo [{a}, {b}].\n"
#                          f"f(a) = f({a}) = {fa} e f(b) = f({b}) = {fb} não têm sinais opostos.")

#     # Inicializa o contador de iterações
#     iteracao = 1

#     # Define os limites atuais do intervalo
#     ai = a  # Limite inferior atual
#     bi = b  # Limite superior atual

#     # Exibe informações iniciais sobre o método
#     print("Iniciando o Método da Bissecção:")
#     print(f"Função definida: f(x) = x * ln(x) + x^2 - x^3 * sin(x)")
#     print(f"Intervalo inicial: [{ai}, {bi}]")
#     print(f"Precisão desejada: {e}\n")

#     # Loop principal do método da Bissecção
#     while abs(bi - ai) > e:
#         # Calcula o ponto médio do intervalo atual
#         ci = (ai + bi) / 2
#         try:
#             fci = f(ci)  # Calcula f(ci)
#         except ValueError as ve:
#             # Trata casos onde a função não está definida em ci
#             print(f"Erro ao calcular f(ci) em x = {ci}: {ve}")
#             return (None, iteracao)

#         # Exibe os detalhes da iteração atual
#         print(f"Iteração {iteracao}:")
#         print(f"  a{iteracao} = {ai}")        # Limite inferior atual
#         print(f"  b{iteracao} = {bi}")        # Limite superior atual
#         print(f"  c{iteracao} = {ci}")        # Ponto médio atual
#         print(f"  f(c{iteracao}) = {fci}")    # Valor da função no ponto médio

#         # Verifica se f(ci) é exatamente zero ou se a precisão foi alcançada
#         if fci == 0 or (bi - ai) / 2 < e:
#             # Se sim, a raiz foi encontrada dentro da precisão desejada
#             print("\nConvergência alcançada pelo Método da Bissecção.\n")
#             return (ci, iteracao)  # Retorna a raiz aproximada e o número de iterações

#         # Decide em qual subintervalo a raiz está localizada
#         if fa * fci < 0:
#             # Se f(a) e f(ci) têm sinais opostos, a raiz está no intervalo [ai, ci]
#             bi = ci          # Atualiza o limite superior para o ponto médio
#             fb = fci         # Atualiza f(bi) para o novo limite superior
#             print(f"  A raiz está no intervalo [{ai}, {ci}].\n")
#         else:
#             # Caso contrário, a raiz está no intervalo [ci, bi]
#             ai = ci          # Atualiza o limite inferior para o ponto médio
#             fa = fci         # Atualiza f(ai) para o novo limite inferior
#             print(f"  A raiz está no intervalo [{ci}, {bi}].\n")

#         # Incrementa o contador de iterações
#         iteracao += 1

#         # Verifica se o número máximo de iterações foi atingido
#         if iteracao > max_iter:
#             # Se sim, informa que o método atingiu o máximo de iterações sem convergência
#             print("Número máximo de iterações atingido sem convergência pelo Método da Bissecção.\n")
#             return (ci, iteracao - 1)  # Retorna a última aproximação e o número de iterações realizadas

#     # Calcula a raiz aproximada como o ponto médio final do intervalo
#     raiz_aproximada = (ai + bi) / 2
#     # Exibe os resultados finais após a conclusão do método
#     print(f"Raiz aproximada após {iteracao - 1} iterações: {raiz_aproximada}")
#     print(f"Intervalo final: [{ai}, {bi}]")
#     print(f"f({raiz_aproximada}) = {f(raiz_aproximada)}\n")

#     # Retorna a raiz aproximada encontrada e o número de iterações
#     return (raiz_aproximada, iteracao - 1)

# def main():
#     """
#     Função principal que controla o fluxo do programa.

#     Executa as seguintes etapas:
#     1. Exibe uma mensagem de boas-vindas.
#     2. Informa ao usuário sobre a função definida.
#     3. Solicita ao usuário os limites do intervalo [a, b].
#     4. Solicita ao usuário a precisão desejada.
#     5. Encontra subintervalos válidos.
#     6. Aplica o Método da Bissecção em cada subintervalo válido.
#     7. Exibe o resultado final.
#     8. Termina o programa.
#     """
#     # Exibe uma mensagem de boas-vindas e informações iniciais
#     print("===========================================")
#     print("   CALCULADORA DE RAÍZES - BISSECCÃO")
#     print("===========================================\n")

#     # Informa ao usuário sobre a função definida
#     print("Por favor, defina a função f(x) cuja raiz deseja encontrar.")
#     print("Atualmente, a função está definida como:")
#     print("f(x) = x * ln(x) + x^2 - x^3 * sin(x)")
#     print("Se desejar modificar a função, edite a função f(x) diretamente no código.\n")

#     # Solicita ao usuário os limites do intervalo [a, b]
#     while True:
#         try:
#             # Solicita o limite inferior do intervalo
#             a_input = input("Digite o limite inferior do intervalo (a): ")
#             a = float(a_input)  # Converte a entrada para float

#             # Solicita o limite superior do intervalo
#             b_input = input("Digite o limite superior do intervalo (b): ")
#             b = float(b_input)  # Converte a entrada para float

#             # Verifica se a <= b
#             if a >= b:
#                 # Se não, informa ao usuário e reinicia o loop para nova entrada
#                 print("O limite inferior deve ser menor que o limite superior. Tente novamente.\n")
#                 continue  # Reinicia o loop para nova entrada

#             # Calcula f(a) e f(b) para verificar a condição do método da Bissecção
#             fa = f(a)
#             fb = f(b)

#             # Verifica se f(a) e f(b) têm sinais opostos
#             if fa * fb >= 0:
#                 # Se não tiverem sinais opostos, informa ao usuário e reinicia o loop
#                 print("f(a) e f(b) devem ter sinais opostos. O método da Bissecção não pode ser aplicado neste intervalo.\n")
#                 print(f"f(a) = f({a}) = {fa}")
#                 print(f"f(b) = f({b}) = {fb}\n")
#                 continue  # Reinicia o loop para nova entrada

#             # Se tudo estiver correto, sai do loop
#             break

#         except ValueError as ve:
#             # Trata casos onde a entrada não é um número válido ou x <= 0
#             print(f"Entrada inválida: {ve}. Por favor, digite números válidos e x > 0.\n")

#     # Solicita ao usuário a precisão desejada para o cálculo
#     while True:
#         try:
#             # Solicita a precisão desejada
#             e_input = input("Digite a precisão desejada (por exemplo, 0.000001): ")
#             e = float(e_input)  # Converte a entrada para float

#             # Verifica se a precisão é um número positivo
#             if e <= 0:
#                 # Se não, informa ao usuário e reinicia o loop para nova entrada
#                 print("A precisão deve ser um número positivo. Tente novamente.\n")
#                 continue  # Reinicia o loop para nova entrada

#             # Se tudo estiver correto, sai do loop
#             break

#         except ValueError:
#             # Trata casos onde a entrada não é um número válido
#             print("Entrada inválida. Por favor, digite um número válido.\n")

#     # Define o tamanho do passo para encontrar subintervalos
#     passo = 1.0  # Você pode ajustar esse valor conforme necessário

#     # Encontra todos os subintervalos onde f(a)*f(b) < 0
#     subintervalos = encontrar_subintervalos(a, b, passo)

#     if not subintervalos:
#         # Se não houver subintervalos válidos, informa ao usuário
#         print("Nenhum subintervalo encontrado com sinais opostos. O método da Bissecção não pode ser aplicado.")
#     else:
#         # Exibe os subintervalos encontrados
#         print(f"\nSubintervalos encontrados com f(a)*f(b) < 0 dentro de [{a}, {b}]:")
#         for idx, (start, end) in enumerate(subintervalos, start=1):
#             print(f"  Subintervalo {idx}: [{start}, {end}]")

#         # Itera sobre cada subintervalo e aplica o Método da Bissecção
#         for idx, (start, end) in enumerate(subintervalos, start=1):
#             print(f"\n--- Resolvendo Subintervalo {idx}: [{start}, {end}] ---\n")

#             try:
#                 # Chama a função bisseccao com os limites do subintervalo
#                 raiz, iteracoes = bisseccao(start, end, e)
#                 # Exibe a raiz encontrada e o número de iterações
#                 print(f"Raiz encontrada no Subintervalo {idx}: {raiz}")
#                 print(f"f({raiz}) = {f(raiz)}")
#                 print(f"Número de iterações realizadas: {iteracoes}\n")
#             except ValueError as ve:
#                 # Trata erros específicos do Método da Bissecção
#                 print(f"Bissecção: {ve}")
#             except OverflowError as oe:
#                 # Trata erros de overflow
#                 print(f"Bissecção: {oe}")
#             except Exception as ex:
#                 # Trata quaisquer outros erros inesperados
#                 print(f"Bissecção: Ocorreu um erro inesperado: {ex}")

#     # Exibe uma mensagem de encerramento
#     print("===========================================")
#     print("       FIM DA CALCULADORA DE RAÍZES")
#     print("===========================================\n")

# # Verifica se o script está sendo executado diretamente
# if __name__ == "__main__":
#     main()  # Chama a função principal para iniciar o programa




# import math  # Importa a biblioteca matemática para usar logaritmo natural e seno

# def f(x):
#     """
#     Define a função f(x) = x * ln(x) + x^2 - x^3 * sin(x)
    
#     Parâmetros:
#         x (float): O valor de x onde a função será avaliada.
    
#     Retorna:
#         float: O valor de f(x).
#     """
#     if x <= 0:
#         raise ValueError("x deve ser maior que 0 para calcular o logaritmo natural.")
#     return x ** (math.log(x)) + x**(2) - x**(3) * math.sin(x)

# def bisseccao(a, b, e, max_iter=1000):
#     """
#     Método da Bissecção para encontrar raízes de f(x) no intervalo [a, b].
    
#     Parâmetros:
#         a (float): Limite inferior do intervalo.
#         b (float): Limite superior do intervalo.
#         e (float): Precisão desejada.
#         max_iter (int): Número máximo de iterações.
    
#     Retorna:
#         float: A raiz aproximada de f(x).
#     """
#     fa = f(a)
#     fb = f(b)
    
#     # Verifica se f(a) e f(b) têm sinais opostos
#     if fa * fb > 0:
#         print("f(a) e f(b) devem ter sinais opostos. O método da bissecção não pode ser aplicado neste intervalo.")
#         print(f"f(a) = f({a}) = {fa}")
#         print(f"f(b) = f({b}) = {fb}")
#         return None
    
#     print(f"Iniciando o Método da Bissecção com a={a}, b={b}, precisão={e}\n")
    
#     for i in range(1, max_iter +1):
#         c = (a + b) / 2  # Ponto médio do intervalo
#         fc = f(c)
        
#         print(f"Iteração {i}: a={a}, b={b}, c={c}, f(c)={fc}")
        
#         # Verifica se o ponto médio é a raiz ou se a precisão foi alcançada
#         if fc == 0 or (b - a)/2 < e:
#             print("Convergência alcançada.")
#             return c  # Raiz encontrada
        
#         # Decide em qual subintervalo a raiz está
#         if fa * fc < 0:
#             b = c  # A raiz está no intervalo [a,c]
#             fb = fc
#         else:
#             a = c  # A raiz está no intervalo [c,b]
#             fa = fc
    
#     print("Número máximo de iterações atingido sem convergência.")
#     return c

# def main():
#     """
#     Função principal para executar o método da Bissecção.
#     """
#     print("=== Método da Bissecção ===")
    
#     # Definir o intervalo [a,b]
#     a = 1.0
#     b = 20.0
    
#     # Definir a precisão desejada
#     e = 1e-6
    
#     # Chamar o método da Bissecção
#     raiz = bisseccao(a, b, e)
    
#     if raiz is not None:
#         print(f"\nRaiz encontrada: {raiz}")
#         print(f"f({raiz}) = {f(raiz)}")
    
#     print("\n=== FIM ===")

# if __name__ == "__main__":
#     main()



import math

def f(x):
    """
    Define a função f(x) = x^log(x) + x^2 - x^3 * sin(x)
    
    Parâmetros:
        x (float): O valor de x onde a função será avaliada.
    
    Retorna:
        float: O valor de f(x).
    """
    if x <= 0:
        raise ValueError("x deve ser maior que 0 para calcular o logaritmo natural.")
    return x ** (math.log(x)) + x**2 - x**3 * math.sin(x)

def bisseccao(a, b, e, max_iter=1000):
    """
    Método da Bissecção para encontrar raízes de f(x) no intervalo [a, b].
    
    Parâmetros:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        e (float): Precisão desejada.
        max_iter (int): Número máximo de iterações.
    
    Retorna:
        float: A raiz aproximada de f(x).
    """
    fa = f(a)
    fb = f(b)
    
    # Verifica se f(a) e f(b) têm sinais opostos
    if fa * fb > 0:
        print("f(a) e f(b) devem ter sinais opostos. O método da bissecção não pode ser aplicado neste intervalo.")
        print(f"f(a) = f({a}) = {fa}")
        print(f"f(b) = f({b}) = {fb}")
        return None
    
    print(f"Iniciando o Método da Bissecção com a={a}, b={b}, precisão={e}\n")
    
    for i in range(1, max_iter + 1):
        c = (a + b) / 2  # Ponto médio do intervalo
        fc = f(c)
        
        print(f"Iteração {i}: a={a}, b={b}, c={c}, f(c)={fc}")
        
        # Verifica se o ponto médio é a raiz ou se a precisão foi alcançada
        if fc == 0 or (b - a)/2 < e:
            print("Convergência alcançada.")
            return c  # Raiz encontrada
        
        # Decide em qual subintervalo a raiz está
        if fa * fc < 0:
            b = c  # A raiz está no intervalo [a,c]
            fb = fc
        else:
            a = c  # A raiz está no intervalo [c,b]
            fa = fc
    
    print("Número máximo de iterações atingido sem convergência.")
    return c

def main():
    """
    Função principal para executar o método da Bissecção.
    """
    print("=== Método da Bissecção ===")
    
    # Definir o intervalo [a,b]
    a = 1.0
    b = 20.0
    
    # Definir a precisão desejada
    e = 1e-6
    
    # Chamar o método da Bissecção
    raiz = bisseccao(a, b, e)
    
    if raiz is not None:
        print(f"\nRaiz encontrada: {raiz}")
        print(f"f({raiz}) = {f(raiz)}")
    
    print("\n=== FIM ===")

if __name__ == "__main__":
    main()
    
