# Problems
## 3-1
Let $a_{max} = max(a_0, a_1, \ldots, a_d)$. Because $a_d > 0$, so $a_{max} > 0$. Now let's prove there exists a constant $n_1$ such that $p(n) \geq 0 \text{ for all } n \geq n_1$.

Let $a_{absmax} = max(abs(a_0), abs(a_1), \ldots, abs(a_{d - 1}))$. So $p(n) \geq a_dn^d + \sum_{i = 0}^{d - 1} (-a_{absmax}n^{d - 1}) = a_dn^d -da_{absmax}n^{d - 1} = n^{d - 1}(a_dn - da_{absmax})$. So $p(n) \geq 0$ when $n \geq \lceil\frac{da_{absmax}}{a_d}\rceil$, $n_1 = \lceil\frac{da_{absmax}}{a_d}\rceil$.

### a
If $k \geq d$, then $p(n) \leq \sum_{i = 0}^d a_{max}n^d = (d + 1)a_{max}n^d \leq (d + 1)a_{max}n^k$.

So there exist positive constants $c = (d + 1)a_{max}$ and $n_0 = max(1, n_1)$ such that $0 \leq p(n) \leq cn^k \text{ for all } n \geq n_0$. Thus $p(n) = O(n^k)$.

### b
We know $p(n) \geq n^{d - 1}(a_dn - da_{absmax})$. So $n^{d - 1}(a_dn - da_{absmax}) \geq n^d$ when $n \geq \frac{da_{absmax}}{a_d - 1}$. Thus $p(n) \geq n^d \geq n^k$ when $n \geq max(1, \lceil \frac{da_{absmax}}{a_d - 1} \rceil)$.

Let $n_2 = max(1, \lceil \frac{da_{absmax}}{a_d - 1} \rceil)$, so there exist positive constants c = 1 and $n_0 = max(n_1, n_2)$ such that $0 \leq cn^k \leq p(n) \text{ for all } n \geq n_0$. So $p(n) = \Omega(n^k)$.

### c
Let $n_3 = (n_0 \text{ in question a})$ and $n_4 = (n_0 \text{ in question b})$. From the questions a and b we know there exist positive constants $c_1 = 1$, $c_2 = (d + 1)a_{max}$ and $n_0 = max(n_3, n_4)$ such that $0 \leq c_1n^d \leq p(n) \leq c_2n^d \text{ for all } n \geq n_0$. Because k = d, so this also holds true for k, so $p(n) = \Theta(n^k)$.

### d
From question a we know $p(n) \leq (d + 1)a_{max}n^d$, because k > d, let $(d + 1)a_{max}n^d < cn^k$, then we have $n > (\frac{(d + 1)a_{max}}{c})^{\frac{1}{k - d}}$. So for any positive constant c, we can find a positive constant $n_0 = \lceil (\frac{(d + 1)a_{max}}{c})^{\frac{1}{k - d}} \rceil + 1$ such that $0 \leq p(n) < cn^k \text{ for all } n \geq n_0$. So $p(n) = o(n^k)$.

### e
