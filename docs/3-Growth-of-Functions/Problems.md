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
have $f'(x) >= 0 \text{ when } x \geq \frac{k}{\epsilon}$. So f(x) is a monotonically increasing function when $x \geq \frac{k}{\epsilon}$.

In order to solve $\epsilon{x} - k\lg{x} > 0$, we only have to solve $\frac{x}{\lg{x}} > \frac{k}{\epsilon}$, since $\lim_{x \to +\infty} \frac{x}{\lg{x}} = +\infty$, so there exists a constant $x_0$ such that $\frac{x_0}{\lg{x_0}} > \frac{k}{\epsilon}$, so $f(x_0) > 0$.

So we can find a constant $x_0$ such that $f(x) \geq 0 \text{ for all } x \geq x_0$. Thus $\epsilon\lg{n} \geq k\lg{\lg{n}} \text{ for all } n \geq 2^{x_0}$. Therefore we proved there exist positive constants c = 1 and $n_0 = 2^{x_0}$
such that $0 \leq \lg^k{n} \leq n^{\epsilon} \text{ for all } n \geq n_0$. So $\lg^k{n} = O(n^{\epsilon})$.

Now let's compare $\lg^k{n}$ and $cn^{\epsilon}$. Similarly, $cn^{\epsilon} = 2^{\lg{c}}(2^{\lg{n}})^{\epsilon} = 2^{\lg{c} + \epsilon\lg{n}}$. So let $\lg{n} = x$, so $\lg{c} + \epsilon\lg{n} - k\lg{\lg{n}} = \lg{c} + \epsilon{x} - k\lg{x}$.
Let $g(x) = \epsilon{x} - k\lg{x} + \lg{c}$. And $g'(x) = \epsilon - \frac{k}{x}$, $g'(x) >= 0 \text{ when } x \geq \frac{k}{\epsilon}$. So g(x) is a monotonically increasing function when $x \geq \frac{k}{\epsilon}$.

In order to solve $g(x) > 0$, we need to solve $\epsilon{x} - k\lg{x} > -\lg{c}$. Namely, for any given positive constant c, we need to find a $x_0$ such that $g(x_0)$ is greater than $-\lg{c}$.
Notice that $\epsilon{x} - k\lg{x} = f(x)$ and f(x) is a a monotonically increasing function. For a given constant, we can find a $x_0$ such that $f(x_0)$ is greater than that constant.

So, for any given constant c, we can find a $x_0$ such that $g(x_0) > 0$. Thus, for any positive constant c, there exists positive constant $n_0 = 2^{x_0}$ such that $0 \leq \lg^k{n} < cn^{\epsilon} \text{ for all } n \geq n_0$. So $\lg^k{n} = o(n^{\epsilon})$.

Since $\lg^k{n} = o(n^{\epsilon})$, then $\lg^k{n}$ could not be $\Omega(n^{\epsilon})$, $w(n^{\epsilon})$, $\Theta(n^{\epsilon})$.

### b
$n^k = (2^{\lg{n}})^k = 2^{k\lg{n}}$, $c^n = (2^{\lg{c}})^n = 2^{n\lg{c}}$. So it's also obvious that $n\lg{c}$ grows faster than $k\lg{n}$. Let $f(n) = n\lg{c} - k\lg{n}$. Because $c > 1$, so $\lg{c} > 0$. Thus we
have the same function $f(x)$ defined in question a. So similarly, we know $n^k = O(c^n)$.

Now let's compare $n^k$ and $bc^n$. $bc^n = 2^{\lg{b}}(2^{\lg{c}})^n = 2^{\lg{b} + n\lg{c}}$. Let $g(n) = \lg{b} + n\lg{c} - k\lg{n}$, and again we have the same function g(x) defined in question a.
So $n^k = o(c^n)$.

### c
Let's compare $\sqrt{n}$ and $cn^{\sin{n}}$. $\sqrt{n} = (2^{\lg{n}})^{\frac{1}{2}} = 2^{\frac{1}{2}\lg{n}}$, $cn^{\sin{n}} = 2^{\lg{c}}(2^{\lg{n}})^{\sin{n}} = 2^{\sin{n}\lg{n} + \lg{c}}$. Let $f(n) = \sin{n}\lg{n} + \lg{c} - \frac{1}{2}\lg{n} = (\sin{n} - \frac{1}{2})\lg{n} + \lg{c}$. So the question is: does there exist a positive constant c (or for any positive constant c), there exists a positive constant $n_0$, such that f(n) > 0 (or f(n) < 0) for all $n \geq n_0$?

First let's check $f(n) > 0$, nomatter how big c is, we can find a $n_1$ such that $\lg{n_1} > \lg{c}$, since $-\frac{3}{2} \leq \sin{n} - \frac{1}{2} \leq \frac{1}{2}$. So there exists a $n_2 \geq n_1$ such that $\sin{n_2} - \frac{1}{2} = -1$, so $f(n_2) < 0$. So for any given constant c, there doesn't exist a constant $n_0$ such that f(n) > 0 for all $n \geq n_0$.

Similarly, for $f(n) < 0$, no matter how small c is, we can find a $n_1$ such that $\lg{n_1} > 2abs(\lg{c})$, and there exists a $n_2 \geq n_1$ such that $\sin{n_2} - \frac{1}{2} = \frac{1}{2}$, so $f(n_2) > 0$. So for any given constant c, there doesn't exist a constant $n_0$ such that f(n) < 0 for all $n \geq n_0$.

Thus, we cannot compare which grows faster.

### d
It's obvious that there exist a positive constant c = 1 and $n_0 = 1$ such that $0 \leq c2^{\frac{n}{2}} \leq 2^n \text{ for all } n \geq n_0$. So $2^n = \Omega(2^{\frac{n}{2}})$.

Now let's compare $2^n$ and $c2^{\frac{n}{2}}$. $c2^{\frac{n}{2}} = 2^{\lg{c}}2^{\frac{n}{2}} = 2^{\frac{n}{2} + \lg{c}}$. Let $f(n) = n - (\frac{n}{2} + \lg{c}) = \frac{n}{2} - \lg{c}$. Let $f(n) > 0$, we have $n > 2\lg{c}$. So for any constant c, there exists a positive constant $n_0 = 2\lg{c} + 1$ such that $2^n > c2^{\frac{n}{2}} \text{ for all } n >= n_0$. So $2^n = w(2^{\frac{n}{2}})$.

### e
$n^{\lg{c}} = (2^{\lg{n}})^{\lg{c}} = 2^{\lg{c}\lg{n}}$, $c^{\lg{n}} = (2^{\lg{c}})^{\lg{n}} = 2^{\lg{c}\lg{n}}$, so $n^{\lg{c}} = c^{\lg{n}}$, thus there exist positive constants $b_1 = 1$ and $n_1 = 1$ such that $0 \leq n^{\lg{c}} \leq b_1c^{\lg{n}} \text{ for all } n \geq n_1$, and there exist positive constants $b_2 = 1$ and $n_2 = 1$ such that $0 \leq b_2c^{\lg{n}} \leq n^{\lg{c}} \text{ for all } n \geq n_2$, and there exist positive constants $b_3 = 1$, $b_4 = 1$ and $n_3 = 1$ such that $0 \leq b_3c^{\lg{n}} \leq n^{\lg{c}} \leq b_4c^{\lg{n}} \text{ for all } n \geq n_3$. So $n^{\lg{c}} = O(c^{\lg{n}})$, $n^{\lg{c}} = \Omega(c^{\lg{n}})$, $n^{\lg{c}} = \Theta(c^{\lg{n}})$.

Since $n^{\lg{c}}$ and $c^{\lg{n}}$ are the same functions, so for any positive constant b, we cannot find a positive constant $n_0$ such that $n^{\lg{c}} < bc^{\lg{n}}$ or $n^{\lg{c}} > bc^{\lg{n}}$ for all $n \geq n_0$.

### f
Since $n! \leq n^n \text{ for all } n \geq 1$, so we can find a positive constant c = 1 and $n_0 = 1$ such that $0 \leq \lg(n!) \leq c\lg({n^n}) \text{ for all } n \geq n_0$, so $\lg(n!) = O(\lg({n^n}))$.
### Summay

|A   |B   |O   |o   |$\Omega$   |w   |$\Theta$   |
|---|---|---|---|---|---|---|
|$\lg^k{n}$   |$n^{\epsilon}$   |yes   |yes   |no   |no   |no   |
|$n^k$   |$c^n$   |yes   |yes   |no   |no   |no   |
|$\sqrt{n}$   |$n^{\sin{n}}$   |no   |no   |no   |no   |no   |
|$2^n$   |$2^{\frac{n}{2}}$   |no   |no   |yes   |yes   |no   |
|$n^{\lg{c}}$   |$c^{\lg{n}}$   |yes   |no   |yes   |no   |yes   |
|   |   |   |   |   |   |   |

