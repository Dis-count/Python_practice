def model(theta, X):
    """
    预测函数
    :param theta: 参数矩阵(nx1)
    :param X:输入变量(矩阵mxn)
    :return: 输出变量, mx1
    """
    return X.dot(theta)

def cost(m, theta, X, y):
    """
    代价函数
    :param m: 训练集个数
    :param theta: 参数矩阵(mx1)
    :param X: 输入变量矩阵(mx1)
    :param y: 输出变量矩阵(mx1)
    :return:
    """
    ele = model(theta, X) - y
    item = ele ** 2
    item_sum = np.sum(item)
    return item_sum / (2 * m)

def derivative(m, theta, X, y, n):
    """
    对各个theta参数求导
    :param m: 训练集个数
    :param theta: 参数矩阵(nx1)
    :param X: 输入变量矩阵(mxn)
    :param y: 输出变量矩阵(mx1)
    :param n: 𝜃变量个数𝜃0, 𝜃1, 𝜃2, ..., 𝜃n-1
    :return: nx1 矩阵
    """
    grad_theta = []
    for j in range(n):
        # 对所有𝜃j变量求导
        grad = (model(theta, X) - y).T.dot(X[:, j])
        grad_sum = np.sum(grad)
        grad_theta.append(grad_sum / m)
    return np.array(grad_theta).reshape(n, 1)

def gradient(grade_theta, theta, alpha):
    """
    𝜃更新
    :param grade_theta:求导后的𝜃矩阵(nx1)
    :param theta: 更新后的𝜃矩阵(nx1)
    :param alpha: 学习率
    :return: 返回更新后的𝜃矩阵(nx1)
    """
    return theta - alpha * grade_theta

def stop_strage(cost, cost_update, threshold):
    """
    停止迭代条件
    :param cost:
    :param cost_update:
    :param threshold:
    :return:
    """
    return (cost >= cost_update) and (cost - cost_update < threshold)

def linear_regression(X, y):
    """
    线性回归模型
    :param X: 输入变量矩阵(mxn)
    :param y: 输出变量矩阵(mx1)
    :param threshold:
    :return:
    """
    start = time.clock()
    m = X.shape[0] # 样本个数
    n = X.shape[1]
    theta = np.zeros(n).reshape(n, 1) # 设置权重参数的初始值
    y = y.reshape(m, 1)
    print "theta:", theta.shape, ", X: ", X.shape, "y:", y.shape

    cost_record = [] # 记录代价函数的值
    alpha = 0.0001 # 学习率
    threshold = 0.01
    cost_val = cost(m, theta, X, y)

    cost_record.append(cost_val)

    iters = 0
    while True:
        grad = derivative(m, theta, X, y, n)
        # 权重参数更新
        theta = gradient(grad, theta, alpha)
        cost_update = cost(m, theta, X, y)
        if stop_strage(cost_val, cost_update, threshold):
            break
        cost_val = cost_update
        cost_record.append(cost_val)
        iters += 1
    end = time.clock()
    print("cost time: %f s" % (end - start))

    return cost_record, theta, iters

# 使用训练线性回归模型预测房价
df = pd.read_csv('house_price.csv')

print df['rooms'].unique()
print df['halls'].unique()

# 去除脏数据
keep_index = (df['rooms'] != '多') & (df['halls'] != '多')
df = df[keep_index]

# 转换数据类型
df['rooms'] = df['rooms'].astype('int')
df['halls'] = df['halls'].astype('int')

# 截取rooms、halls、size和price
X = df[['rooms', 'halls', 'size']]
y = df['price']

cost_record, theta, iters = linear_regression(X.values, y.values)
print iters
print theta
print cost_record

# 预测数据
# rooms,halls,size,price
# 1,1,49,326
# 2,1,56.45,315
# 2,1,58.3,466
# 3,1,92.33,1061
# 2,1,76.88,408

print model(theta, np.array([1, 1, 49]))
print model(theta, np.array([2, 1, 56.45]))
print model(theta, np.array([2, 1, 58.3]))
print model(theta, np.array([3, 1, 92.33]))
print model(theta, np.array([2, 1, 76.88]))
