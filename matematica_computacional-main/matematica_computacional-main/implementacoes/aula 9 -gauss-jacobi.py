def gauss_jacobi(A, b, x_init=None, tol=1e-6, max_iter=50000):
    n = len(A)
    
    if x_init is None:
        x = [0] * n
    else:
        x = x_init  
    
    x_new = [0] * n 
    
    for k in range(max_iter):
        for i in range(n):
            soma = b[i]
            for j in range(n):
                if i != j:
                    soma -= A[i][j] * x[j] 
            x_new[i] = soma / A[i][i] 
        
        erro = sum(abs(x_new[i] - x[i]) for i in range(n))  
        if erro < tol:  
            return x_new, k + 1
        
        x = x_new[:]  
    
    return x_new, max_iter  

A = [
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
]

b = [7, -8, 6]

x_init = [0, 0, 0]

solucao, iteracoes = gauss_jacobi(A, b, x_init)
print("Solução encontrada:", solucao)
print("Número de iterações:", iteracoes)
