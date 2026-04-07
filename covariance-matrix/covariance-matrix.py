import numpy as np

def covariance_matrix(X):
    X = np.array(X,dtype=float)
    if X.ndim != 2:
        return None
    n = X.shape[0]
    if n < 2:
        return None
    mean = np.mean(X,axis=0)
    X_contered = X - mean
    cov = X_contered.T @ X_contered / (n-1)
    return cov