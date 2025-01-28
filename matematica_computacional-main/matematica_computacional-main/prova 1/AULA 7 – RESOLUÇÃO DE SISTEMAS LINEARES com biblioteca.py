import numpy as np

def gaussian_elimination(A, b):
    """
    Perform Gaussian elimination with partial pivoting to solve Ax = b.
    
    Parameters:
        A (numpy.ndarray): Coefficient matrix of size n x n.
        b (numpy.ndarray): Right-hand side vector of size n.

    Returns:
        numpy.ndarray: Solution vector x of size n.
    """
    n = len(b)
    A = A.astype(float)  # Ensure matrix is in float for division
    b = b.astype(float)

    for k in range(n):
        # Partial pivoting
        max_row = np.argmax(np.abs(A[k:, k])) + k
        if A[max_row, k] == 0:
            raise ValueError("Matrix is singular and cannot be solved.")
        
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        # Elimination
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

# Example usage
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

x = gaussian_elimination(A, b)
print("Solution:", x)
