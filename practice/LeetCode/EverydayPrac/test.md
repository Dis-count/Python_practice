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
