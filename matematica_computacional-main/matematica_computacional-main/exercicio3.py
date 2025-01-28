def exponencial(valor, expoente):
    return valor ** expoente  # Utiliza a operação de potência de forma simples

def somatorio(n):
    soma = 0
    for x in range(1, n + 1):
        soma += x
    return soma

def fatorial(x):
    fat = 1
    for i in range(1, x + 1):  # Simplesmente usa o intervalo de 1 a x
        fat *= i
    return fat

def euler(n, x):
    e = 1  # Inicializa com o primeiro termo da série (1)
    for i in range(1, n + 1):  # Somando até o n-ésimo termo
        e += (x ** i) / fatorial(i)  # Adiciona cada termo da série
    return e

def inverte_e(e):
    return 1 / e  # Inverte o valor de e

# Entradas do usuário
n = int(input("Insira o valor de n: "))
x = int(input("Insira o valor de x: "))

# Cálculo e exibição do resultado
resultado = euler(n, x)
print("Resultado de Euler:", resultado)
print("Inverso de e:", inverte_e(resultado))
