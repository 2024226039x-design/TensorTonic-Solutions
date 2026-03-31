import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    # 类型转换，防止传入字符串
    seq_len = int(seq_len)
    d_model = int(d_model)
    base = float(base)

    # 1.创建空矩阵，seq_len 行 × d_model 列
    PE = np.zeros((seq_len, d_model))

    # 2.位置向量，竖起来方便广播
    pos = np.arange(seq_len).reshape(-1,1)

    # 3.频率除数
    i = np.arange(0,d_model,2)
    div = base ** (i / d_model)

    # 4.算角度
    angle = pos / div

    # 5.偶数列填sin，奇数列填cos
    PE[:,0::2] = np.sin(angle)
    PE[:,1::2] = np.cos(angle[:,:d_model // 2])

    return PE