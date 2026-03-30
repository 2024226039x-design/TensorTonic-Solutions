import numpy as np

def make_diagonal(v):
    v = np.array(v,dtype=float)

    n = len(v)

    result = np.zeros((n,n))
    for i in range(n):
        result[i][i] = v[i]
    return result
