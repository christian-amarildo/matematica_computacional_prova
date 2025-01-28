import numpy as np

def sistemaTriangularSuperior(A, b):
    # Pegar o tamanho da matriz
    n , _ = np.shape(A)
    # Iniciar o vetor solução com 0
    x = np.zeros(n)

    # Resolver de trás pra frente o sistema
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i, j] * x[j]
        x[i] = (b[i] - soma) / A[i, i]

    return x

def sistemaTriangularInferior(A, b):
    # Pegar o tamanho da matriz
    n , _ = np.shape(A)
    # Iniciar o vetor solução com 0
    x = np.zeros(n)

    # Resolver de frente pra trás o sistema
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += A[i, j] * x[j]
        x[i] = (b[i] - soma) / A[i, i]

    return x

def metodo_lu(A, b):
    # Pegar quantidade de linhas e colunas (L = C)
    n, _ = np.shape(A)
    # Criar uma matriz identidade (só diagonal principal com 1) de tamanho n
    L = np.eye(n)
    # Criar a matriz U sendo cópia de A
    U = A.copy()

    print(f"Matriz A: \n{A}\n")

    # Iteração vai até a coluna n-1
    for c in range(n):
        # Candidato a pivô é o elemento da coluna c que está na diagonal principal
        pivo = U[c, c]
        for l in range(c+1, n):
            # Operações para zerar as linhas abaixo do pivô
            fator = U[l, c] / pivo
            # Preencher a matriz identidade com os fatores
            L[l, c] = fator
            U[l, 0:] -= fator * U[c, 0:]
            print(f"Escalonando coluna {c}: \n{U}\n")

    # Matriz U vai ser a A após o escalonamento
    # Matriz L vai ser a identidade com os fatores usados no escalonamento
    print(f"Matriz L: \n{L}\n")
    print(f"Matriz U: \n{U}\n")

    # Ax = b -> LUx = b -> Ux = y -> Ly = b
    y = sistemaTriangularInferior(L, b)
    print(f"Vetor solução Y: \n{y}\n")

    # Ux = y
    x = sistemaTriangularSuperior(U, y)

    print(f"Vetor solução X: \n{x}\n")
    return x

def metodo_lu_pivoteamento(A, b):
    # Pegar quantidade de linhas e colunas (L = C)
    n, _ = np.shape(A)
    # Criar uma matriz identidade (só diagonal principal com 1) de tamanho n
    L = np.eye(n)
    #Criar uma matriz identidade (só diagonal principal com 1) de tamanho n para armazenar as trocas 
    P = np.eye(n)
    # Criar a matriz U sendo cópia de A
    U = A.copy()

    print(f"Matriz A: \n{A}\n")

    for c in range(n):
        # Pivoteamento parcial: troca de linhas
        max_row = np.argmax(abs(U[c:, c])) + c
        if c != max_row:
            U[[c, max_row]] = U[[max_row, c]]
            P[[c, max_row]] = P[[max_row, c]]
            L[[c, max_row], :c] = L[[max_row, c], :c]
            print(f"Trocando linha {c} com {max_row}: \n{U}\n")

        # Eliminação gaussiana
        for l in range(c + 1, n):
            factor = U[l, c] / U[c, c]
            L[l, c] = factor
            U[l, :] -= factor * U[c, :]
            print(f"Escalonando coluna {c}: \n{U}\n")

    # Matriz U vai ser a A após o escalonamento
    # Matriz L vai ser a identidade com os fatores usados no escalonamento
    print(f"Matriz L: \n{L}\n")
    print(f"Matriz U: \n{U}\n")

    Pb = np.dot(P, b)

    # PAx = b -> LUx = Pb -> Ux = y -> Ly = Pb
    y = sistemaTriangularInferior(L, Pb)
    print(f"Vetor solução Y: \n{y}\n")

    # Ux = y
    x = sistemaTriangularSuperior(U, y)

    print(f"Vetor solução X: \n{x}\n")
    return x


A = np.array([
    [3, -4, -6],
    [18, -21, -33],
    [12, -10, -22]
], dtype=float)

b = np.array([25, 141, 66], dtype=float)

metodo_lu(A, b)

metodo_lu_pivoteamento(A, b)
