# Função para calcular a norma (ou módulo) de um vetor v.
# A norma é dada pela raiz quadrada da soma dos quadrados dos componentes do vetor.
def norma(v):
    # A função soma o quadrado de cada elemento do vetor 'v' e retorna a raiz quadrada dessa soma.
    return sum(vi**2 for vi in v) ** 0.5  # Calcula a norma do vetor v.

# Função para resolver um sistema linear utilizando eliminação de Gauss.
# A função recebe uma matriz A e um vetor b, e resolve o sistema Ax = b.
def resolver_sistema_linear(A, b):
    n = len(A)  # 'n' é o número de equações, que é igual ao número de linhas de A.
    x = [0] * n  # Inicializa o vetor solução x com zeros. Inicialmente, x = [0, 0, ..., 0].

    # A primeira parte do algoritmo aplica a eliminação de Gauss.
    for i in range(n):
        for j in range(i + 1, n):
            # 'fator' é o valor necessário para zerar os elementos abaixo da diagonal.
            fator = A[j][i] / A[i][i]  # Calcula o fator que será usado para zerar a entrada A[j][i].
            b[j] -= fator * b[i]  # Atualiza o vetor b para refletir a eliminação.
            
            # Realiza a eliminação na matriz A.
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]  # Subtrai o múltiplo da linha i da linha j para zerar A[j][i].

    # A segunda parte do algoritmo realiza a substituição reversa para resolver o sistema triangular superior.
    for i in range(n - 1, -1, -1):
        soma_produtos = sum(A[i][j] * x[j] for j in range(i + 1, n))  # Soma os produtos A[i][j] * x[j] para j > i.
        x[i] = (b[i] - soma_produtos) / A[i][i]  # Resolve para x[i] usando a substituição reversa.

    return x  # Retorna o vetor solução x.

# Função para resolver um sistema de equações não lineares utilizando o Método de Newton Modificado.
# A função recebe a função F, a Jacobiana J, um valor inicial x0, e as tolerâncias epsilon1 e epsilon2.
def newton_modificado(F, J, x0, epsilon1, epsilon2, max_iter=100):
    x_k = x0[:]  # Faz uma cópia de x0 e armazena em x_k. Inicia a iteração com x0.
    J_k = J(x_k)  # Calcula a Jacobiana J(x_k) no ponto inicial x_k.
    
    # O loop a seguir realiza o processo iterativo de Newton modificado.
    for k in range(max_iter):  # Realiza no máximo max_iter iterações.
        F_k = F(x_k)  # Avalia a função F no ponto x_k.

        # Se a norma de F_k for menor que epsilon1, isso significa que o vetor F_k está suficientemente próximo de zero.
        if norma(F_k) < epsilon1:
            return x_k, k, True  # Retorna a solução encontrada, o número de iterações e True (sucesso).

        try:
            # Tenta resolver o sistema linear J_k * s_k = -F_k para encontrar o vetor de correção s_k.
            s_k = resolver_sistema_linear([row[:] for row in J_k], [-fi for fi in F_k])
        except ZeroDivisionError:
            # Se ocorrer uma divisão por zero (por exemplo, a Jacobiana é singular), retorna o valor de x_k, o número de iterações e False (falha).
            return x_k, k, False  
        
        # Atualiza o valor de x_k para x_{k+1} com a correção s_k.
        x_k_plus_1 = [x_k[i] + s_k[i] for i in range(len(x_k))]

        # Se a norma da diferença entre x_k_plus_1 e x_k for menor que epsilon2, significa que a solução convergiu.
        if norma([x_k_plus_1[i] - x_k[i] for i in range(len(x_k))]) < epsilon2:
            return x_k_plus_1, k + 1, True  # Retorna a solução encontrada, o número de iterações e True (sucesso).

        # Se a solução não convergiu, atualiza x_k para x_k_plus_1 e continua para a próxima iteração.
        x_k = x_k_plus_1

        # A cada 5 iterações, recalcula a Jacobiana J_k para melhorar a precisão.
        if k % 5 == 0:  
            J_k = J(x_k)  # Recalcula a Jacobiana no novo ponto x_k.

    return x_k, max_iter, False  # Se o número máximo de iterações for alcançado sem convergência, retorna x_k, o número máximo de iterações e False (falha).
