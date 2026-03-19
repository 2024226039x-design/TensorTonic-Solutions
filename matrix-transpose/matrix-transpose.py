import numpy as np

def matrix_transpose(A):
    A =np.array(A)
    rows, cols = A.shape
    result = np.zeros((cols,rows))
    for i in range(rows):
        for j in range(cols):
            result[j][i]=A[i][j]
    return result