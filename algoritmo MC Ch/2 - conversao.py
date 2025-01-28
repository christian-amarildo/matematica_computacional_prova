def binario_para_decimal(binario):
    """
    Converte um número binário (string) para decimal (inteiro).
    :param binario: Número binário representado como string.
    :return: O número decimal equivalente (inteiro) ou uma mensagem de erro se a entrada for inválida.
    """
    try:
        # Tenta converter a string binária para um número decimal usando a função `int` com base 2.
        decimal = int(binario, 2)
        return decimal  # Retorna o valor decimal convertido.
    except ValueError:
        # Captura um erro de conversão (caso a string contenha caracteres diferentes de '0' e '1').
        return "Entrada inválida. Certifique-se de que o número binário contém apenas 0s e 1s."


def decimal_para_binario(decimal):
    """
    Converte um número decimal (inteiro) para binário (string).
    :param decimal: Número decimal representado como inteiro.
    :return: O número binário equivalente (string) ou uma mensagem de erro se a entrada for inválida.
    """
    try:
        # Tenta converter a entrada para inteiro (caso seja passada como string).
        decimal = int(decimal)
        # Converte o número decimal para binário usando a função `bin` e remove o prefixo '0b'.
        binario = bin(decimal)[2:]
        return binario  # Retorna o valor binário convertido.
    except ValueError:
        # Captura um erro de conversão (caso a entrada não seja um número inteiro).
        return "Entrada inválida. Certifique-se de que o número decimal seja um inteiro."


# Verifica se o script está sendo executado diretamente (e não importado como módulo).
if __name__ == "__main__":
    # Exibe o título do programa.
    print("Conversor Binário <-> Decimal")
    # Exibe as opções disponíveis para o usuário.
    print("1. Binário para Decimal")
    print("2. Decimal para Binário")
    # Solicita ao usuário que escolha uma das opções do menu.
    escolha = input("Escolha uma opção (1 ou 2): ")

    # Verifica se o usuário escolheu a opção de converter binário para decimal.
    if escolha == "1":
        # Solicita ao usuário que insira um número binário.
        binario = input("Digite um número binário: ")
        # Exibe o resultado da conversão chamando a função `binario_para_decimal`.
        print(f"O número binário {binario} em decimal é: {binario_para_decimal(binario)}")

    # Verifica se o usuário escolheu a opção de converter decimal para binário.
    elif escolha == "2":
        # Solicita ao usuário que insira um número decimal.
        decimal = input("Digite um número decimal: ")
        # Exibe o resultado da conversão chamando a função `decimal_para_binario`.
        print(f"O número decimal {decimal} em binário é: {decimal_para_binario(decimal)}")

    # Verifica se o usuário inseriu uma opção inválida.
    else:
        # Exibe uma mensagem de erro caso a escolha seja diferente de '1' ou '2'.
        print("Opção inválida. Escolha 1 ou 2.")
