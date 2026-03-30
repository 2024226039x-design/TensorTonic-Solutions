import numpy as np

def dot_product(x, y):
    x = np.array(x,dtype=float)
    y = np.array(y,dtype=float)
    result = np.dot(x,y)
    return float(result)
    