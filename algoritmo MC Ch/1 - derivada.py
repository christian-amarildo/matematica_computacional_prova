"""
Código: Calculadora de Derivadas (Sem uso de SymPy)
=================================================

Este código permite calcular:
1) Derivada Simples (para polinômios em x)
2) Regra da Cadeia
3) Derivada Parcial (para funções polinomiais simples em x, y e z)

Descrição Geral:
----------------
- O programa exibe um menu principal onde o usuário pode escolher qual tipo de derivada deseja calcular.
- Cada opção solicita as informações necessárias para realizar o cálculo de forma manual, sem a utilização de bibliotecas simbólicas.
- Os resultados são exibidos na tela.

Como utilizar:
--------------
1) Ao executar o programa, será exibido um menu com 4 opções:
   [1] Derivada Simples
   [2] Regra da Cadeia
   [3] Derivada Parcial
   [0] Sair

2) Escolha a opção desejada digitando o número correspondente e pressione Enter.

3) Siga as instruções que aparecerão na tela. Para cada tipo de derivada:
   - Derivada Simples:
     * Você informará os coeficientes do polinômio em ordem decrescente do expoente.
       Exemplo: se a função é 5x^3 + 2x^2 + 4x + 1, digite "5 2 4 1".
     * A saída será uma lista com os coeficientes da derivada resultante.
       Exemplo: para 5x^3 + 2x^2 + 4x + 1, a derivada é 15x^2 + 4x + 4, então os coeficientes são [15, 4, 4].

   - Regra da Cadeia:
     * Você fornecerá os valores numéricos de g(x), de x e as derivadas f'(g(x)) e g'(x).
       Ou seja, se deseja calcular a derivada de f(g(x)) em um ponto x específico, precisará do valor de g(x) nesse ponto,
       do próprio valor de x, e dos valores de f'(g(x)) e g'(x).
     * O programa faz o produto f'(g(x)) * g'(x) e retorna o resultado.

   - Derivada Parcial:
     * O programa faz uma derivada parcial de uma expressão polinomial simples em até três variáveis: x, y e z.
     * Você deverá inserir a expressão de forma segmentada (separando os termos por espaços) e depois escolher qual variável derivar.
     * Exemplo: para x^2 + xy + y^2, insira os termos (x^2, xy, y^2) separadamente. O programa tentará parsear e derivar.
     * Esta parte ainda é simples e não cobre todos os casos possíveis de polinômios. É apenas um exemplo.

Observações:
------------
- O código é inteiramente didático e não abrange casos muito complexos.
- Caso queira extensões ou lide com funções mais complexas (ex. exponenciais, logarítmicas, senos, cossenos),
  deve-se adaptar o código ou utilizar uma biblioteca simbólica.

"""

# Função para exibir o menu principal com as opções de tipos de derivadas.
def menu_principal():
    """
    Exibe as opções principais de derivada e solicita a escolha do usuário.
    Retorna:
        int: A escolha do usuário (1, 2, 3 ou 0).
    """
    print("\n===========================================")
    print("     BEM-VINDO(A) À CALCULADORA DE DERIVADAS")
    print("===========================================\n")
    print("Escolha o tipo de derivada que deseja calcular:")
    print("[1] Derivada Simples")
    print("[2] Regra da Cadeia")
    print("[3] Derivada Parcial")
    print("[0] Sair")

    while True:
        try:
            opcao = int(input("\nDigite sua escolha: "))
            if opcao in [0, 1, 2, 3]:
                return opcao
            else:
                print("Opção inválida. Por favor, escolha 0, 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro correspondente à opção desejada.")

# =============================
# 1) DERIVADA SIMPLES
# =============================
def derivada_simples():
    """
    Solicita ao usuário os coeficientes de um polinômio (em x) em ordem decrescente de expoentes
    e retorna a lista de coeficientes correspondentes à derivada do polinômio.

    Exemplo:
    Se o polinômio é 5x^3 + 2x^2 + 4x + 1, então:
    - coeficientes: [5, 2, 4, 1]
    - derivada: 15x^2 + 4x + 4 (coeficientes [15, 4, 4])
    """
    print("\n[Derivada Simples]")
    print("Você está calculando a derivada de um polinômio na variável x.")
    print("Exemplo de entrada: para 5x^3 + 2x^2 + 4x + 1, digite: 5 2 4 1")

    while True:
        try:
            entrada = input("Digite os coeficientes do polinômio (ordem decrescente de expoentes): ")
            coeficientes = list(map(float, entrada.split()))
            break  # Saímos do loop se deu tudo certo
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números separados por espaço.")

    # Lista que irá armazenar os coeficientes da derivada
    derivada = []
    # O maior expoente é (len(coeficientes) - 1)
    n = len(coeficientes) - 1

    # Iteramos sobre cada coeficiente.
    # i é o índice; coef é o coeficiente.
    for i, coef in enumerate(coeficientes):
        # Exemplo: se o polinômio é a0*x^n + a1*x^(n-1) + ... + an*x^0,
        # aqui i = 0 -> expoente n,
        #     i = 1 -> expoente n-1, etc.
        expoente = n - i
        if expoente >= 1:  # Somente derivamos termos de expoente >= 1
            derivada.append(coef * expoente)
    # Exemplo: se coeficientes = [5, 2, 4, 1], n=3,
    # i=0: expoente=3 -> derivadaTermo = 5*3=15
    # i=1: expoente=2 -> derivadaTermo = 2*2=4
    # i=2: expoente=1 -> derivadaTermo = 4*1=4
    # i=3: expoente=0 -> ignoramos.

    print("\nDerivada do polinômio (lista de coeficientes em ordem decrescente):")
    print(derivada)
    print("\nInterpretando a saída:")
    print("Se você obteve [15, 4, 4], isso significa 15x^2 + 4x + 4.")

# =============================
# 2) REGRA DA CADEIA
# =============================
def regra_da_cadeia():
    """
    Aplica a regra da cadeia: (f(g(x)))' = f'(g(x)) * g'(x)

    Solicitamos ao usuário:
    - O valor de g(x)
    - O valor de x
    - O valor numérico de f'(g(x))
    - O valor numérico de g'(x)

    E então retornamos o produto f'(g(x)) * g'(x).
    """
    print("\n[Regra da Cadeia]")
    print("Você está calculando a derivada de f(g(x)) em um ponto específico.")
    print("Precisaremos do valor de g(x) nesse ponto, do valor de x, e também de f'(g(x)) e g'(x).")

    while True:
        try:
            gx = float(input("Digite o valor de g(x): "))
            x_valor = float(input("Digite o valor de x: "))
            # Solicitar valor de f'(g(x))
            f_linha = float(input("Digite o valor de f'(g(x)): "))
            # Solicitar valor de g'(x)
            g_linha = float(input("Digite o valor de g'(x): "))
            resultado = f_linha * g_linha
            print(f"\nResultado da regra da cadeia (f'(g(x)) * g'(x)) = {resultado}")
            break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar valores numéricos (ex: 2.5, -3, etc.). Tente novamente.")

# =============================
# 3) DERIVADA PARCIAL
# =============================
def derivada_parcial():
    """
    Calcula a derivada parcial de uma função polinomial simples em até três variáveis: x, y e z.

    A ideia é bastante simplificada:
    - O usuário informa quantos termos deseja inserir.
    - Para cada termo, é solicitado o coeficiente e o expoente das variáveis x, y, z.
    - Em seguida, o usuário escolhe em relação a qual variável derivar.

    Exemplo:
    Função: f(x,y,z) = 5x^2y^1z^0 + 2x^1y^0z^2  (que seria 5x^2y + 2x z^2)

    * Número de termos = 2
    * 1º termo: coef=5, exp_x=2, exp_y=1, exp_z=0
    * 2º termo: coef=2, exp_x=1, exp_y=0, exp_z=2

    Se escolher derivar em relação a x:
    derivada = 5 * 2 x^(2-1) y^1 z^0 + 2 * 1 x^(1-1) y^0 z^2 = 10x^1y + 2z^2

    Observação:
    - Este método não faz parsing de strings e não se aplica a funções mais complicadas.
    """
    print("\n[Derivada Parcial]")
    print("Você está calculando a derivada parcial de uma função polinomial em x, y e z.")
    print("Será solicitado o número de termos e, para cada termo, os dados: coeficiente e expoentes de x, y, z.")

    while True:
        try:
            n_termos = int(input("Digite o número de termos da função: "))
            if n_termos <= 0:
                print("O número de termos deve ser um inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

    # Lista para armazenar cada termo na forma de dicionário
    # Exemplo: {"coef": 5, "x": 2, "y": 1, "z": 0}
    termos = []

    for i in range(n_termos):
        print(f"\nTermo {i+1}:")
        while True:
            try:
                coef = float(input("  Coeficiente: "))
                exp_x = int(input("  Expoente de x: "))
                exp_y = int(input("  Expoente de y: "))
                exp_z = int(input("  Expoente de z: "))
                if exp_x < 0 or exp_y < 0 or exp_z < 0:
                    print("  Os expoentes devem ser inteiros não negativos. Tente novamente.")
                    continue
                termos.append({"coef": coef, "x": exp_x, "y": exp_y, "z": exp_z})
                break
            except ValueError:
                print("  Entrada inválida. Coeficiente deve ser float e expoentes devem ser inteiros. Tente novamente.")

    # Escolha da variável
    print("\nEscolha a variável para derivar:")
    print("[1] x")
    print("[2] y")
    print("[3] z")

    while True:
        try:
            escolha_var = int(input("Digite 1, 2 ou 3: "))
            if escolha_var in [1, 2, 3]:
                break
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro (1, 2 ou 3).")

    # Mapeamos a escolha para a variável correspondente.
    if escolha_var == 1:
        var = "x"
    elif escolha_var == 2:
        var = "y"
    else:
        var = "z"

    # Agora calculamos a derivada parcial em relação a var.
    # Nova lista de termos para a derivada parcial
    derivada = []

    for termo in termos:
        coef = termo["coef"]
        exp_x = termo["x"]
        exp_y = termo["y"]
        exp_z = termo["z"]

        if var == "x":
            # Derivada parcial em relação a x
            if exp_x == 0:
                # A derivada do termo em que x tem expoente 0 é 0
                continue
            else:
                # Novo coeficiente = coef * exp_x
                novo_coef = coef * exp_x
                # Novo expoente de x = exp_x - 1
                novo_exp_x = exp_x - 1
                derivada.append({"coef": novo_coef, "x": novo_exp_x, "y": exp_y, "z": exp_z})

        elif var == "y":
            # Derivada parcial em relação a y
            if exp_y == 0:
                continue
            else:
                novo_coef = coef * exp_y
                novo_exp_y = exp_y - 1
                derivada.append({"coef": novo_coef, "x": exp_x, "y": novo_exp_y, "z": exp_z})

        else:  # var == "z"
            if exp_z == 0:
                continue
            else:
                novo_coef = coef * exp_z
                novo_exp_z = exp_z - 1
                derivada.append({"coef": novo_coef, "x": exp_x, "y": exp_y, "z": novo_exp_z})

    # Exibindo o resultado de forma legível
    print(f"\nDerivada parcial em relação a {var}:")

    if len(derivada) == 0:
        print("0")
    else:
        # Construímos a string da expressão resultante
        partes = []
        for d in derivada:
            c = d["coef"]
            e_x = d["x"]
            e_y = d["y"]
            e_z = d["z"]

            # Monta o termo no formato coef * x^ex * y^ey * z^ez
            # Ocultamos a variável se o expoente for 0, e não exibimos ^1.
            termo_str = f"{c}"  # coef sempre exibe
            if e_x > 0:
                if e_x == 1:
                    termo_str += "x"
                else:
                    termo_str += f"x^{e_x}"
            if e_y > 0:
                if e_y == 1:
                    termo_str += "y"
                else:
                    termo_str += f"y^{e_y}"
            if e_z > 0:
                if e_z == 1:
                    termo_str += "z"
                else:
                    termo_str += f"z^{e_z}"

            partes.append(termo_str)
        # Unir com +
        resultado_str = " + ".join(partes)
        print(resultado_str)

# =============================
# FUNÇÃO PRINCIPAL (MAIN)
# =============================
def main():
    """
    Função principal que controla o fluxo do programa.
    Exibe o menu, chama as funções de cada tipo de derivada e só termina quando o usuário escolhe sair.
    """
    while True:
        opcao = menu_principal()

        if opcao == 0:
            print("\nSaindo do programa...")
            break
        elif opcao == 1:
            derivada_simples()
        elif opcao == 2:
            regra_da_cadeia()
        elif opcao == 3:
            derivada_parcial()

        # Após a execução de cada opção, retornamos ao menu.
        input("\nPressione Enter para voltar ao menu...")

# Início da execução do programa
if __name__ == "__main__":
    main()
