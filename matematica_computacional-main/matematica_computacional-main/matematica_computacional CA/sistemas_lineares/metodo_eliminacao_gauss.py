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


def metodo_eliminacao_gauss(A, b):
    # Pegar quantidade de linhas e colunas (L = C)
    n, _ = np.shape(A)
    # Fazer a matriz aumentada de A e b
    A_aumentada = np.concatenate((A, b), 1)
    print(f"Matriz aumentada: \n{A_aumentada}\n")

    # Iteração vai até n-1
    for c in range(n-1):
        # Candidato a pivô é o elemento da coluna c que está na diagonal principal
        pivo = A_aumentada[c, c]
        for l in range(c+1, n):
            # Operações para zerar as linhas abaixo do pivô
            fator = A_aumentada[l, c] / pivo
            A_aumentada[l, 0:] -= fator * A_aumentada[c, 0:]
            print(f"Escalonando coluna {c}: \n{A_aumentada}\n")

    print(f"Matriz triangular superior: \n{A_aumentada}\n")
    
    # Separar a matriz triangular superior e o vetor b
    A_triangular = A_aumentada[:, :-1]
    b = A_aumentada[:, -1]

    # Vetor solução X
    x = sistemaTriangularSuperior(A_triangular, b)
    
    print(f"Vetor solução: \n{x}\n")
    return x


def metodo_eliminacao_gauss_pivoteamento_parcial(A, b):
    # Pegar quantidade de linhas e colunas (L = C)
    n, _ = np.shape(A)
    # Fazer a matriz aumentada de A e b
    A_aumentada = np.concatenate((A, b), 1)
    print(f"Matriz aumentada inicial: \n{A_aumentada}\n")

    # Etapas de escalonamento
    for c in range(n-1):
        # Pivoteamento parcial: encontrar o índice do maior elemento em módulo na coluna c
        max_index = np.argmax(np.abs(A_aumentada[c:, c])) + c
        if max_index != c:
            # Trocar as linhas c e max_index
            A_aumentada[[c, max_index]] = A_aumentada[[max_index, c]]
            print(f"Troca de linhas {c} e {max_index} para pivoteamento:\n{A_aumentada}\n")

        # Candidato a pivô é o elemento da diagonal principal
        pivo = A_aumentada[c, c]
        if np.abs(pivo) < 1e-12:
            raise ValueError("Sistema singular ou quase singular, pivô muito pequeno!")

        for l in range(c+1, n):
            # Operações para zerar as linhas abaixo do pivô
            fator = A_aumentada[l, c] / pivo
            A_aumentada[l, c:] -= fator * A_aumentada[c, c:]
            print(f"Escalonando coluna {c}: \n{A_aumentada}\n")

    print(f"Matriz triangular superior: \n{A_aumentada}\n")

     # Separar a matriz triangular superior e o vetor b
    A_triangular = A_aumentada[:, :-1]
    b = A_aumentada[:, -1]

    # Vetor solução X
    x = sistemaTriangularSuperior(A_triangular, b)

    print(f"Vetor solução: \n{x}\n")
    return x



A = np.array([
    [3, -4, -6],
    [18, -21, -33],
    [12, -10, -22]
], dtype=float)

b = np.array([
    [25],
    [141],
    [66]
], dtype=float)

# metodo_eliminacao_gauss(A, b)

metodo_eliminacao_gauss_pivoteamento_parcial(A, b)
