def fatorial(n) -> float:
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

n = int(input("Número de termos: "))
x = int(input("Expoente: "))

resultado = 0
for k in range(0, n+1):
    resultado += (x ** k)/ fatorial(k)

print(f"e^{x} calculado pela Série de Taylor com {n} termos é: {resultado}")