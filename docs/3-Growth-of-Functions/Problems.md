# Problems
## 3-1
Let $a_{max} = max(a_0, a_1, \ldots, a_d)$. Because $a_d > 0$, so $a_{max} > 0$. Now let's prove there exists a constant $n_1$ such that $p(n) \geq 0 \text{ for all } n \geq n_1$.

Let $a_{absmax} = max(abs(a_0), abs(a_1), \ldots, abs(a_{d - 1}))$. So $p(n) \geq a_dn^d + \sum_{i = 0}^{d - 1} (-a_{absmax}n^{d - 1}) = a_dn^d -da_{absmax}n^{d - 1} = n^{d - 1}(a_dn - da_{absmax})$. So $p(n) \geq 0$ when $n \geq \lceil\frac{da_{absmax}}{a_d}\rceil$, $n_1 = \lceil\frac{da_{absmax}}{a_d}\rceil$.

### a
If $k \geq d$, then $p(n) \leq \sum_{i = 0}^d a_{max}n^d = (d + 1)a_{max}n^d \leq (d + 1)a_{max}n^k$.

So there exist positive constants $c = (d + 1)a_{max}$ and $n_0 = max(1, n_1)$ such that $0 \leq p(n) \leq cn^k \text{ for all } n \geq n_0$. Thus $p(n) = O(n^k)$.
