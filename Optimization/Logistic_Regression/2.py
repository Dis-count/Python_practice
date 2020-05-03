def sigmod(z):
    """
    sigmod函数
    :param z: mx1矩阵
    :return: mx1矩阵
    """
    return 1.0 / (1 + np.exp(-z))


def model(theta, X):
    """
    预测函数
    :param theta:  nx1矩阵
    :param X: mxn矩阵
    :return: mx1矩阵
    """
    return sigmod(X.dot(theta))


def cosst_function(theta, X, y):
    """
    代价函数
    :param theta: nx1矩阵
    :param X: mxn矩阵
    :param y: mx1矩阵
    :return: 实数
    """
    m = y.size

    h = sigmod(X.dot(theta))
    J = -(1.0/m)*((np.log(h)).T.dot(y) + (np.log(1-h)).T.dot(1-y))

    return J[0, 0]


def derivative(theta, X, y):
    """
    对theta求偏导
    :param theta: nx1矩阵
    :param X: mxn矩阵
    :param y: mx1矩阵
    :return: nx1矩阵
    """
    m = y.size
    h = sigmod(X.dot(theta))
    grad = (1.0/m) * X.T.dot(h - y)
    return grad


def gradient(grade_theta, theta, alpha):
    """
    𝜃更新
    :param grade_theta:求导后的𝜃矩阵(nx1)
    :param theta: 更新后的𝜃矩阵(nx1)
    :param alpha: 学习率
    :return: 返回更新后的𝜃矩阵(nx1)
    """
    return theta - alpha * grade_theta

def logistic_regression(X, y):
    """
    逻辑回归算法
    :param X: mxn矩阵
    :param y: mx1矩阵
    :return: nx1矩阵
    """
    start = time.clock()
    m = X.shape[0] # 样本个数
    n = X.shape[1] # 特征个数

    y = y.reshape(m, 1)
    cost_record = []  # 记录代价函数的值
    alpha = 0.1  # 学习率
    maxiters = 1000 # 最大迭代次数

    theta = np.zeros(n).reshape(n, 1)  # 设置权重参数的初始值
    cost_val = cosst_function(theta, X, y)

    cost_record.append(cost_val)

    iters = 0
    while True:
        if iters >= maxiters:
            break
        grad = derivative(theta, X, y)

        # 权重参数更新
        new_theta = gradient(grad, theta, alpha)
        theta = new_theta
        cost_update = cosst_function(new_theta, X, y)
        cost_val = cost_update
        cost_record.append(cost_val)
        iters += 1
    end = time.clock()
    print("cost time: %f s" % (end - start))

    return cost_record, theta, iters


def predict(theta, X, threshold=0.5):
    """
    预测函数
    :param theta: 已求解的theta函数
    :param X: 输入变量
    :param threshold: 阈值
    :return: 输出变量（预测）
    """
    p = model(theta, X) >= threshold
    return p.astype('int')
