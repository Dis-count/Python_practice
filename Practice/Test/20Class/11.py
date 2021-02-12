import numpy as np
import matplotlib.pyplot as plt
%%matplotlib inline
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import scale, StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

X, y = make_moons(n_samples = 100, noise = 0.25, random_state = 2)
X_train, X_test, y_train, y_test = train_test_split(X,y,stratify = y, random_state =42)

X.shape

plt.scatter(X_train[:,0], X_train[:,1], c= y_train)

mlp = MLPClassifier(solver = 'lbfgs', random_state = 0, max_iter = 1000).fit(X_train, y_train)
mlp.score(X_train, y_train)

mlp.score(X_test, y_test)

xlim = plt.xlim()
ylim = plt.ylim()
xs = np.linspace(xlim[0], xlim[1], 1000)
ys = np.linspace(ylim[0], ylim[1], 1000)
xx, yy = np.meshgrid(xs, ys)
X_grid = np.c_[xx.ravel(), yy.ravel()]
plt.contour(xx, yy , mlp.predict_proba(X_grid)[:, 1].reshape(xx.shape), levels = [.5])
plt.scatter(X_train[:,0], X_train[:, 1], c= y_train)

plt.xlim(xlim)
plt.ylim(ylim)

fig, axes = plt.subplots(3,3, figsize = (8,5))
for ax, i in zip(axes.ravel(), range(10)):
    mlp = MLPClassifier(solver = 'lbfgs', random_state = i, max_iter =1000).fit(X_train, y_train)
    print(mlp.score(X_train, y_train))
    print(mlp.score(X_test, y_test))

    ax.contour(xx, yy , mlp.predict_proba(X_grid)[:, 1].reshape(xx.shape), levels = [.5])
    ax.scatter(X_train[:,0], X_train[:, 1], c= y_train)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xticks(())
    ax.set_yticks(())

# default layer:100 // Change it to 5
mlp = MLPClassifier(solver = 'lbfgs',hidden_layer_sizes=(5),random_state = 0, max_iter =1000).fit(X_train, y_train)
print(mlp.score(X_train, y_train))
print(mlp.score(X_test, y_test))

plt.contour(xx, yy, mlp.predict_proba(X_grid)[:, 1].reshape(xx.shape), levels = [.5])
plt.scatter(X_train[:,0], X_train[:, 1], c= y_train)

plt.xlim(xlim)
plt.ylim(ylim)

# three layers
mlp = MLPClassifier(solver = 'lbfgs',hidden_layer_sizes=(10,10,10),random_state = 0, max_iter =1000).fit(X_train, y_train)
print(mlp.score(X_train, y_train))
print(mlp.score(X_test, y_test))

# activation = tanh
mlp = MLPClassifier(solver = 'lbfgs',hidden_layer_sizes=(10,10,10), activation = 'tanh',random_state = 0, max_iter =1000).fit(X_train, y_train)
print(mlp.score(X_train, y_train))
print(mlp.score(X_test, y_test))


rng = np.random.RandomState(0)
x = np.sort(rng.uniform(size = 100))
y = np.sin(10*x) + 5*x + np.random.normal(0, .3 , size =100)
plt.plot(x, y, 'o')

# ---------------------------
line = np.linspace(0,1,100)
X = x.reshape(-1,1)

from sklearn.neural_network import MLPRegressor
mlp_relu = MLPRegressor(solver = 'lbfgs', max_iter = 5000).fit(X, y)
mlp_tanh = MLPRegressor(solver = 'lbfgs', max_iter = 5000, activation = 'tanh').fit(X, y)
plt.plot(x,y,'o')
plt.plot(line, mlp_relu.predict(line.reshape(-1,1)), label = 'relu')
plt.plot(line, mlp_tanh.predict(line.reshape(-1,1)), label = 'tanh')

# digit dataset
from sklearn.datasets import load_digits
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data /16., digits.target, stratify = digits.target, random_state = 0)

mlp = MLPClassifier(random_state = 0, max_iter = 1000).fit(X_train, y_train)
print(mlp.score(X_train, y_train))
print(mlp.score(X_test, y_test))

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(data.data /16., data.target, stratify = data.target, random_state = 0)

scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp = MLPClassifier(random_state = 0, max_iter = 1000).fit(X_train_scaled, y_train)
print(mlp.score(X_train_scaled, y_train))
print(mlp.score(X_test_scaled, y_test))

from sklearn.model_selection import GridSearchCV
pipe = make_pipeline(StandardScaler(), MLPClassifier(solver = 'lbfgs', max_iter = 5000, random_state = 1))
param_grid = {'mlpclassifier__alpha': np.logspace(-3,3,7)}
grid = GridSearchCV(pipe, param_grid, return_train_score = True)

grid.fit(X_train, y_train)

results = pd.DataFrame(grid.cv_results_)
results

res = results.pivot_table(index = 'param_mlpclassifier__alpha', values = ['mean_test_score', 'mean_train_score'])
res

res.plot()
plt.xscale('log')
plt.ylim(0.95,1.01)


res = results.pivot_table(index = 'param_mlpclassifier__alpha', values = ['mean_test_score', 'mean_train_score', 'std_test_score', 'std_train_score'])

res.mean_test_score.plot(yerr = res.std_test_score)
res.mean_train_score.plot(yerr = res.std_train_score)
plt.xscale('log')
plt.ylim(0.95,1.01)
plt.legend()

from sklearn.model_selection import GridSearchCV
pipe = make_pipeline(StandardScaler(), MLPClassifier(solver = 'lbfgs', max_iter = 5000, random_state =1))
param_grid = {'mlpclassifier__hidden_layer_sizes': [(10,),(50,),(100,),(500,),(10,10),(50,50),(100,100),(500,500)]}
grid = GridSearchCV(pipe, param_grid, return_train_score =True)

grid.fit(X_train, y_train)

results = pd.DataFrame(grid.cv_results_)
res = results.pivot_table(index = 'param_mlpclassifier__hidden_layer_sizes', values = ['mean_test_score', 'mean_train_score', 'std_test_score', 'std_train_score'])
res

res.mean_test_score.plot(yerr = res.std_test_score)
res.mean_train_score.plot(yerr = res.std_train_score)
plt.ylim(0.95,1.01)
plt.legend()

X_train.shape

mlp = MLPClassifier(solver = 'lbfgs', random_state = 0, hidden_layer_sizes = (2, ), max_iter = 1000).fit(X_train_scaled, y_train)
print(mlp.score(X_train_scaled, y_train))
print(mlp.score(X_test_scaled, y_test))

mlp.coefs_[0].shape

hidden = np.dot(X_test_scaled, mlp.coefs_[0]) + mlp.intercepts_[0]
hidden

plt.scatter(hidden[:,0], hidden[:,1], c= y_test)
