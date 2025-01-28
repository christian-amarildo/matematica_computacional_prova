# def somatorio(k,n,x):
#     for i in range(n-k):
#         x += x
#         i += i
#     return x
# k1= int(input("escolha o valor de k"))
# n1= int(input("escolha o valor de n"))
# x1= float(input("escolha o valor de x"))

# funcA= somatorio(k1,n1,x1)
# print(funcA)

def somatorio(n,x):
    soma = 0
    for x in range(1, n + 1):
        soma += x
    return soma

somatorioA = somatorio(1000000,0.1)
funcaoA= 10000 - somatorioA

print(funcaoA)
