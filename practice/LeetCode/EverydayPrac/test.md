$a^{(p-1)} \equiv 1\pmod{p}$

Consider a stochastic linear program in inequality form
minimize $c^{T} x$
subject to:
$$\mathbb{P}\left(a_{i}^{T} x \leq b_{i}\right) \geq p, \quad i=1, \ldots, m$$

where the parameters $a_i$ are independent Gaussian random vectors with mean $\bar{a}_i$ and covariance $\sum_i$  and $p \geq 0.5$. This problem can be expressed as the SOCP
minimize $c^{T} x$
subject to:
$$\bar{a}_{i}^{T} x+\Phi^{-1}(p)\left\|\Sigma_{i}^{1 / 2} x\right\|_{2} \leq b_{i}, \quad i=1, \ldots, m$$
, where $\Phi^{−1}(⋅)$ is the inverse normal cumulative distribution function.

A polyhedron is a set described by a finite number of affine inequalities and equalities:
$$\mathcal{P}=\{x: A x \leq b, \quad C x=d\}$$
where $A$, $C$ are matrices, $b$, $d$ are vectors, and inequalities are understood componentwise. Sometimes bounded polyhedra are referred to as polytopes.


机会约束规划-- 确定等价类

设随机变量 $\xi(w)$ 的概率分布函数为 $\Phi(\dot)$
对给定的置信水平 $\alpha$, 必存在一个数 $K_{\alpha}$ 使得

$P\left\{\xi(w) \geq K_{\alpha}\right\}=\alpha$

$P\{\xi(w) \geq h(x)\} \geq \alpha \Leftrightarrow h(x) \leq K_{\alpha}$
其中，
$\Phi\left(K_{\alpha}\right)=1-\alpha, K_{\alpha}=\Phi^{-1}(1-\alpha)$

https://wenku.baidu.com/view/80eea79ba200a6c30c22590102020740bf1ecd5f.html
