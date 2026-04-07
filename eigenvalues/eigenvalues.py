import numpy as np

def calculate_eigenvalues(matrix):
    # 尝试转成 numpy 数组，非法输入返回 None
    try:
        matrix = np.array(matrix, dtype=float)
    except Exception:
        return None

    # 检查是否为方阵（行数=列数，且是二维）
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    eigenvalues = np.linalg.eigvals(matrix)

    eigenvalues = sorted(eigenvalues, key=lambda x: (-x.real, -x.imag))

    return np.array(eigenvalues, dtype=complex)