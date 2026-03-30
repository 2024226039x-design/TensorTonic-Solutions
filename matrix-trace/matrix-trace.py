import numpy as np

def matrix_trace(A):
    A = np.array(A,dtype=float)
    n = A.shape[0]
    result = 0.0
    for i in range(n):
        result += A[i][i]

    return float(result)
        
