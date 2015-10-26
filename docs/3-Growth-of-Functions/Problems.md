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
From question b we know $p(n) \geq n^{d - 1}(a_dn - da_{absmax})$, let $f(n) = n^{d - 1}(a_dn - da_{absmax}) - cn^k = n^k(n^{d - k}(a_d - \frac{da_{absmax}}{n}) - c)$, because k < d, so it's obvious that f(n) is a  monotonically increasing function. First let $a_d - \frac{da_{absmax}}{n} > \frac{a_d}{2}$ and we get $n > \frac{2da_{absmax}}{a_d}$. So $f(n) > n^k(n^{d - k}\frac{a_d}{2} - c) \text{ for all } n >= \lceil \frac{2da_{absmax}}{a_d} \rceil + 1$. Then let $n^{d - k}\frac{a_d}{2} - c > 0$ and we have $n > (\frac{2c}{a_d})^{\frac{1}{d - k}}$. So for any given positive constant c we can find a positive constant $n_0 = max(\lceil \frac{2da_{absmax}}{a_d} \rceil + 1, \lceil (\frac{2c}{a_d})^{\frac{1}{d - k}} \rceil + 1)$ such that $0 \leq cn^k < p(n) \text{ for all } n \geq n_0$. So $p(n) = w(n^k)$.

## 3.2
### a
Note that $n = 2^{\lg{n}}$. So $\lg^k{n} = (2^{\lg{\lg{n}}})^k = 2^{k\lg{\lg{n}}}$, $n^\epsilon = (2^{\lg{n}})^{\epsilon} = 2^{\epsilon\lg{n}}$. It's obvious that $\epsilon\lg{n}$ grows faster than 
$k\lg{\lg{n}}$. Let $\lg{n} = x, x > 0$, so $k\lg{\lg{n}} = k\lg{x}$, $\epsilon\lg{n} = \epsilon{x}$. Let $f(x) = \epsilon{x} - k\lg{x}$, so $f'(x) = \epsilon - \frac{k}{x}$. Because $\epsilon > 0$ and $k \geq 1$, we 
have $f'(x) >= 0 \text{ when } x \geq \frac{k}{\epsilon}$. So f(x) is a monotonically increasing function when $x \geq \frac{k}{\epsilon}$. So $f(x) \geq f(\frac{k}{\epsilon}) = k(1 - \lg{\frac{k}{\epsilon}})$.
 
If $k \leq 2\epsilon$, then $k(1 - \lg{\frac{k}{\epsilon}}) \geq 0$, so $f(x) \geq 0 \text{ for all } x \geq \frac{k}{\epsilon}$.
 
If $k > 2\epsilon$, then $k(1 - \lg{\frac{k}{\epsilon}}) < 0$. In order to solve $\epsilon{x} - k\lg{x} > 0$, we only have to solve $\frac{x}{\lg{x}} > \frac{k}{\epsilon}$, since $\lim_{x \to +\infty} \frac{x}{\lg{x}} = +\infty$, so there exists a constant $x_0$ such that $\frac{x_0}{\lg{x_0}} > \frac{k}{\epsilon}$, so $f(x_0) > 0$.
 
So either way we can find a constant $x_0$ such that $f(x) \geq 0$. Thus $\epsilon\lg{n} \geq k\lg{\lg{n}} \text{ for all } n \geq 2^{x_0}$. Therefore we proved there exist positive constants c = 1 and $n_0 = 2^{x_0}$ 
such that $0 \leq \lg^k{n} \leq n^{\epsilon} \text{ for all } n \geq n_0$. So $\lg^k{n} = O(n^{\epsilon})$.
 
### Summay
 
|A   |B   |O   |o   |$\Omega$   |w   |$\Theta$   |
|---|---|---|---|---|---|---|
|$\lg^k{n}$   |$n^{\epsilon}$   |yes   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |

