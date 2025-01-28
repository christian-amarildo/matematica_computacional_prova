# Define uma função chamada `somatorio` que calcula o somatório de um número `x` repetido `n` vezes.
def somatorio(x, n):
    # Inicializa a variável `total` como 0, que será usada para armazenar a soma acumulada.
    total = 0

    # Inicia um loop `for` que irá iterar de 1 até `n` (inclusive).
    # `range(1, n+1)` cria uma sequência de números de 1 a `n`.
    for i in range(1, n+1):
        # Adiciona o valor de `x` ao total acumulado em cada iteração do loop.
        total += x  # `total = total + x` é a forma expandida da operação.

    # Retorna o valor final de `total`, que é o somatório de `x` repetido `n` vezes.
    return total


# Imprime o resultado do somatório chamando a função `somatorio` com `x = 0.5` e `n = 30000`.
# Neste caso, o somatório será o valor de 0.5 somado 30.000 vezes.
print(somatorio(0.5, 30000))

# Imprime o resultado do somatório chamando a função `somatorio` com `x = 0.11` e `n = 30000`.
# O valor 0.11 será somado 30.000 vezes.
print(somatorio(0.11, 30000))
