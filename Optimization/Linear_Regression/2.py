def derivative(m, theta, X, y, n):
    """
    对各个theta参数求导（向量形式）
    :param m: 训练集个数
    :param theta: 参数矩阵(nx1)
    :param X: 输入变量矩阵(mxn)
    :param y: 输出变量矩阵(mx1)
    :param n: 𝜃变量个数𝜃0, 𝜃1, 𝜃2, ..., 𝜃n-1
    :return: nx1 矩阵
    """
    grad_sum = X.T.dot(model(theta, X) - y)
    return grad_sum / m
