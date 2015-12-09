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
In question 3.2-3, we've already proved that $\lg{(n!)} = \Theta(n\lg{n})$, notice that $\lg(n^n) = n\lg{n}$, so $\lg{(n!)} = \Theta(\lg{n^n})$. And $\lg{(n!)} = O(\lg{n^n})$, $\lg{(n!)} = \Omega(\lg{n^n})$.

### Summary

|A   |B   |O   |o   |$\Omega$   |w   |$\Theta$   |
|---|---|---|---|---|---|---|
|$\lg^k{n}$   |$n^{\epsilon}$   |yes   |yes   |no   |no   |no   |
|$n^k$   |$c^n$   |yes   |yes   |no   |no   |no   |
|$\sqrt{n}$   |$n^{\sin{n}}$   |no   |no   |no   |no   |no   |
|$2^n$   |$2^{\frac{n}{2}}$   |no   |no   |yes   |yes   |no   |
|$n^{\lg{c}}$   |$c^{\lg{n}}$   |yes   |no   |yes   |no   |yes   |
|$\lg(n!)$   |$\lg(n^n)$   |yes   |no   |yes   |no   |yes   |

## 3-3
### a
First, let's compare $2^{2^{n + 1}}$ and $2^{2^n}$, it's easy to see $2^{2^n} = O(2^{2^{n + 1}})$. But could $2^{2^n} = \Omega(2^{2^{n + 1}})$? If it's true, then there exist a positive constant c and $n_0$ such that $0 \leq c2^{2^{n + 1}} \leq 2^{2^n}$ for all $n \geq n_0$. But $\frac{2^{2^n}}{c2^{2^{n + 1}}} = \frac{1}{c2^{2^{n + 1} - 2^n}} = \frac{1}{c2^{2^n}}$. No matter how small c is, $2^{2^n}$ will be greater than $\frac{1}{c}$. So $2^{2^n} = \Omega(2^{2^{n + 1}})$ could not be true.

Then let's compare $n!$ and $e^n$. We know $n! = 2^{\lg{(n!)}}$, and $e^n = (2^{\lg{e}})^n = 2^{n\lg{e}}$. In question 3.2-3 we know $\lg{(n!)} = \Theta(n\lg{n})$, so $\lg{(n!)}$ grows faster than $n\lg{e}$. So $n!$ grows faster than $e^n$, thus $n! = \Omega(e^n)$.

And it's obvious $(n + 1)! = \Omega(n!)$. Notice that $\frac{n!}{c(n + 1)!} = \frac{1}{c(n + 1)}$, which will eventually smaller than 1. So $n!$ could not be $\Omega((n + 1)!)$.

And what about $(n + 1)!$ and $2^{2^n}$? $(n + 1)! = 2^{\lg{(n + 1)!}} = 2^{\Theta((n + 1)\lg{(n + 1)})} = 2^{O((n + 1)^2)} = 2^{O(n^2)}$. So $2^{2^{n}}$ grows faster, $2^{2^n} = \Omega((n + 1)!)$.

Since $e^n = (\frac{e}{2})^n2^n$, and $(\frac{e}{2})^n$ grows faster than $n$, so $e^n$ grows faster than $n2^n$, $e^n = \Omega(n2^n)$.

And it's easy to see that $n2^n = \Omega(2^n)$, $2^n = \Omega(\frac{3}{2})^n$.

$(\lg{n})^{\lg{n}} = (2^{\lg{\lg{n}}})^{\lg{n}} = 2^{\lg{n}\lg{\lg{n}}}$. And $n^{\lg{\lg{n}}} = (2^{\lg{n}})^{\lg{\lg{n}}} = 2^{\lg{n}\lg{\lg{n}}}$. So $(\lg{n})^{\lg{n}} = n^{\lg{\lg{n}}}$. And $(\frac{3}{2})^n = (2^{\lg{\frac{3}{2}}})^n = 2^{n\lg{\frac{3}{2}}}$. Let $\lg{n} = k$, so $\lg{n}\lg{\lg{n}} = k\lg{k}$, $n\lg{\frac{3}{2}} = 2^k\lg{\frac{3}{2}}$, so we can see $2^k\lg{\frac{3}{2}}$ grows faster. Thus $(\frac{3}{2})^n = \Omega((\lg{n})^{\lg{n}})$.

According to [Stirling's approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation), we know $n! = \Theta(n^{n + \frac{1}{2}}e^{-n})$. So $(\lg{n})! = \Theta((\lg{n})^{\lg{n} + \frac{1}{2}}e^{-\lg{n}}) = \Theta((\lg{n})^{\lg{n}}\frac{\sqrt{\lg{n}}}{e^{\lg{n}}}) = O((\lg{n})^{\lg{n}})$, since $e^x$ grows much faster than $\sqrt{x}$. So $(\lg{n})^{\lg{n}} = \Omega((\lg{n})!)$.

Let $\lg{n} = x$, so $n = 2^x$, $n^3 = 2^{3x}$. $(\lg{n})! = \Theta((\lg{n})^{\lg{n}}\frac{\sqrt{\lg{n}}}{e^{\lg{n}}}) = \Theta(x^{x + \frac{1}{2}}e^{-x}) = \Theta(e^{x(\ln{x} - 1) + \frac{1}{2}\ln{x}})$. And $2^{3x} = e^{(3\ln{2})x}$. So $(\lg{n})!$ grows faster than $n^3$.

$4^{\lg{n}} = (2^2)^{\lg{n}} = (2^{\lg{n}})^2 = n^2$, so $n^2 = 4^{\lg{n}}$. And it's obvious $n^3 = \Omega(n^2)$, $n^2 = \Omega(n\lg{n})$. And in question 3.2-3 we already proved $\lg({n!}) = \Theta(n\lg{n})$.

And it's easy to know $n\lg{n} = \Omega(n)$, $n = 2^{\lg{n}}$.

Similarly, $(\sqrt{2})^{\lg{n}} = (2^{\lg{n}})^{\frac{1}{2}} = \sqrt{n}$, so $n = \Omega({(\sqrt{2})^{\lg{n}}})$.

$\sqrt{n} = n^{\frac{1}{2}} = (2^{\lg{n}})^{\frac{1}{2}} = 2^{\frac{1}{2}\lg{n}}$, it grows faster than $2^{\sqrt{2\lg{n}}}$, so $(\sqrt{2})^{\lg{n}} = \Omega(2^{\sqrt{2\lg{n}}})$.

$\lg^2{n} = (2^{\lg{\lg{n}}})^2 = 2^{2\lg{\lg{n}}}$, in question 3-2 we know $\lg^k{n} = o(n^{\epsilon})$ for $k \geq 1$ and $\epsilon > 0$, so here we have $k = 1$, $\epsilon = \frac{1}{2}$, so $\sqrt{2\lg{n}}$ grows faster than $2\lg{\lg{n}}$, so $2^{\sqrt{2\lg{n}}} = \Omega(\lg^2{n})$.

And $\lg^2{n} = \Omega(\ln{n})$, $\ln{n} = \Omega(\sqrt{\lg{n}})$.

Then let's compare $\sqrt{\lg{n}}$ and $\ln{\ln{n}}$. $\sqrt{\lg{n}} = \sqrt{\frac{\ln{n}}{\ln{2}}}$, from previous proof, we know $\sqrt{\frac{\ln{n}}{\ln{2}}}$ grows faster than $\ln{\ln{n}}$. So $\sqrt{\lg{n}} = \Omega(\ln{\ln{n}})$.

$\ln{\ln{n}} = 2^{\lg{\ln{\ln{n}}}}$, and according to the definition of [Iterated logarithm](https://en.wikipedia.org/wiki/Iterated_logarithm), we can see $\lg{\ln{\ln{n}}}$ grows faster than $\lg^\*{n}$. So $\ln{\ln{n}} = \Omega(2^{\lg^\*{n}})$. And $2^{\lg^\*{n}} = \Omega(\lg^\*{n})$.

Since $\lg^\*{n} = 1 + \lg^\*{\lg{n}}$, so $\lg^\*{\lg{n}} = \Theta(\lg^\*{n})$.

In question 3.2-5 we proved that $\lg^\*{(\lg{n})}$ is asymptotically larger than $\lg{(\lg^\*{n})}$. So $\lg^\*{(\lg{n})} = \Omega(\lg{(\lg^\*{n})})$.

$n^{\frac{1}{\lg{n}}} = (2^{\lg{n}})^{\frac{1}{\lg{n}}} = 2$, so $n^{\frac{1}{\lg{n}}} = \Theta(1)$.

#### Summary
* $g_1 = 2^{2^{n + 1}}$
* $g_2 = 2^{2^n}$
* $g_3 = (n + 1)!$
* $g_4 = n!$
* $g_5 = e^n$
* $g_6 = n2^n$
* $g_7 = 2^n$
* $g_8 = (\frac{3}{2})^n$
* $g_9 = (\lg{n})^{\lg{n}}$
* $g_{10} = n^{\lg{\lg{n}}}, g_9 = \Theta(g_{10})$
* $g_{11} = (\lg{n})!$
* $g_{12} = n^3$
* $g_{13} = n^2$
* $g_{14} = 4^{\lg{n}}, g_{13} = \Theta(g_{14})$
* $g_{15} = n\lg{n}$
* $g_{16} = \lg({n!}), g_{15} = \Theta(g_{16})$
* $g_{17} = n$
* $g_{18} = 2^{\lg{n}}, g_{17} = \Theta(g_{18})$
* $g_{19} = (\sqrt{2})^{\lg{n}}$
* $g_{20} = 2^{\sqrt{2\lg{n}}}$
* $g_{21} = \lg^2{n}$
* $g_{22} = \ln{n}$
* $g_{23} = \sqrt{\lg{n}}$
* $g_{24} = \ln{\ln{n}}$
* $g_{25} = 2^{\lg^\*{n}}$
* $g_{26} = \lg^\*{n}$
* $g_{27} = \lg^\*{\lg{n}}, g_{26} = \Theta(g_{27})$
* $g_{28} = \lg{(\lg^\*{n})}$
* $g_{29} = n^{\frac{1}{\lg{n}}}$
* $g_{30} = 1, g_{29} = \Theta(g_{30})$

### b
How do we find a function like this? In question 3-2, we know that $n^{\sin{n}}$ is neither $o(\sqrt{n})$ nor $w(\sqrt{n})$. We can use the feature of $\sin{n}$. So we can build a function that can be quite big and quite small. And it has to be not smaller than the largest function in $g_i(n)$ sometimes, so we can simply have a function like $n2^{2^{n + 1}}$, which is $\Omega(g_i(n))$. Then we multiply $|\sin{n}|$, so the function is $|\sin{n}|n2^{2^{n + 1}}$, which is neither $O(g_i(n))$ nor $\Omega(g_i(n))$.

## 3-4
### a
This is not true. If $g(n) = O(f(n))$, then there exist positive constants $c_1$ and $n_1$ such that $0 \leq g(n) \leq c_1f(n) \text{ for all } n \geq n_1$, since $f(n) = O(g(n))$, so there also exist positive constants $c_2$ and $n_2$ such that $0 \leq f(n) \leq c_2g(n) \text{ for all } n \geq n_2$, so we have $0 \leq \frac{1}{c_1}g(n) \leq f(n) \leq c_2g(n) \text{ for all } n \geq max(n_1, n_2)$, which means $f(n) = \Theta(g(n))$. This is not 100% true.

### b
This is not true. Let $f(n) = n$ and $g(n) = \lg{n}$, it's easy to see $f(n) + g(n) = \Theta(n) \neq \Theta(min(f(n), g(n)))$.

### c
This is true. Because $f(n) = O(g(n))$, so there exist positive constants c and $n_0$ such that $0 \leq f(n) \leq cg(n) \text{ for all } n \geq n_0$. So $0\leq \lg{(f(n))} \leq \lg{(cg(n))} = \lg{c} + \lg{(g(n))} = \lg{c} * 1 + \lg{(g(n))} \leq \lg{c} * \lg{(g(n))} + \lg{(g(n))} = (\lg{c} + 1)\lg{(g(n))}$. So we find a positive constant $c_1 = \lg{c} + 1$ such that $0 \leq \lg{(f(n))} \leq c_1\lg{(g(n))} \text{ for all } n \geq n_0$, so $\lg{(f(n))} = O(\lg{(g(n))}$.

### d
This is not true. If $g(n) = O(f(n))$, then there exist positive constants $c_1$ and $n_1$ such that $0 \leq g(n) \leq c_1f(n) \text{ for all } n \geq n_1$. Suppose $2^{f(n)} = O(2^{g(n)})$, then there exist positive constants $c_2$ and $n_2$ such that $0 \leq 2^{f(n)} \leq {c_2}2^{g(n)} \text{ for all } n \geq n_2$. And ${c_2}2^{g(n)} = 2^{\lg{c_2} + g(n)}$. So we have $f(n) \leq \lg{c_2} + g(n)$. But this is not always true, let $f(n) = n + \lg{n}$ and $g(n) = n$, so $f(n) \leq 2g(n) \text{ for all } n \geq 1$. But for any given positive constant $c_2$, we can always find a positive constant $n_3$ such that $n + \lg{n} > \lg{c_2} + n \text{ for all } n \geq n_3$. So $2^{f(n)} \neq O(2^{g(n)})$ in this situation.

### e
This is not true. Let $f(n) = \frac{1}{n}$, if $f(n) = O((f(n))^2)$, then there exist positive constants c and $n_0$ such that $0 \leq \frac{1}{n} \leq \frac{c}{n^2} \text{ for all } n \geq n_0$. But $\frac{c}{n^2} - \frac{1}{n} = \frac{c - n}{n^2} \leq 0 \text{ for all } n \geq c$. So we cannot find such $n_0$ for any positive constant $c$.

### f
This is true. If $f(n) = O(g(n))$, then there exist positive constants c and $n_0$ such that $0 \leq f(n) \leq cg(n) \text{ for all } n \geq n_0$, so we have $0 \leq \frac{1}{c}f(n) \leq g(n) \text{ for all } n \geq n_0$, which is the definition of $g(n) = \Omega(f(n))$.

### g
This is not true. Let $f(n) = 2^{2n}$, so $f(\frac{n}{2}) = 2^n$. So it's obvious $f(n) \neq \Theta(f(\frac{n}{2}))$.

### h
This is true. Suppose $f(n) + o(f(n)) = \Theta(f(n))$, then we need to prove that there exist positive constatns $c_1$, $c_2$ and $n_0$ such that $0 \leq c_1f(n) \leq f(n) + o(f(n)) \leq c_2f(n)$. It's easy to find $c_1 = 1$ since $o(f(n)) \geq 0$. And according to the definition of $o(f(n))$, we know for any positive constant c there exists positive constant $n_1$ such that $0 \leq o(f(n)) < cf(n) \text{ for all } n \geq n_1$. so we can choose $c = 1$, so $f(n) + o(f(n)) \leq f(n) + f(n) = 2f(n)$, so we have $c_2 = 2$ and $n_0 = n_1$. So $f(n) + o(f(n)) = \Theta(f(n))$.

## 3-5
### a
Suppose both $f(n) = O(g(n))$ and $f(n) = \mathop{\Omega}^{\infty}(g(n))$ are not true. If $f(n) = O(g(n))$ is not true, then there are two cases, first, we can not find any positive constant c such that $0 \leq f(n) \leq cg(n)$ for any integer n. It means for any positive constant c we have $f(n) > cg(n)$. So it satisfies $f(n) \geq cg(n) \geq 0$ for infinitely many integers n. So it shows $f(n) = \mathop{\Omega}^{\infty}(g(n))$ is true, thus, the hypothesis is wrong. Second, we can find a constant c such that $0 \leq f(n) \leq cg(n)$ for some integers n. If the set of integers n is finite, then there is an infinite set such that $f(n) \geq cg(n) \geq 0$, so $f(n) = \mathop{\Omega}^{\infty}(g(n))$. If the set is infinite but we cannot find a positive constant $n_0$ that satisfies $f(n) = O(g(n))$, there is also a infinite set such that $f(n) > cg(n) \geq 0$, so the hypothesis is wrong. So we proved either $f(n) = O(g(n))$ or $f(n) = \mathop{\Omega}^{\infty}(g(n))$ or both.

In problem 3-2 we proved both $\sqrt{n} = O(n^{\sin{n}})$ and $\sqrt{n} = \Omega(n^{\sin{n}})$ are wrong. So it's not true if we use $\Omega$ in place of $\mathop{\Omega}^{\infty}$.

### b
The advantage is that we can describe the relationship of two functions when we cannot use $\Omega$ notation. The disadvantage is that sometimes we cannot clearly know the running time of a function.

### c
If $f(n) = \Theta(g(n))$, then we have $f(n) = O'(g(n))$ and $f(n) = \Omega(g(n))$. If we have $f(n) = O'(g(n))$ and $f(n) = \Omega(g(n))$, $f(n) = \Theta(g(n))$ is also true. Since $f(n) = \Omega(g(n))$ guarantees $f(n) \geq 0$.

### d
$\tilde{\Omega}(g(n)) = \lbrace f(n): \text{ there exist positive constants } c, \text{ } k, \text{ and } n_0 \text{ such that } 0 \leq cg(n)\lg^k{n} \leq f(n) \text{ for all } n \geq n_0 \rbrace$.

$\tilde{\Theta}(g(n)) = \lbrace f(n): \text{ there exist positive constants } c_1, \text{ } c_2, \text{ } k_1, \text{ } k_2 \text{ and } n_0 \text{ such that } 0 \leq c_1g(n)\lg^{k_1}{n} \leq f(n) \leq c_2g(n)\lg^{k_2}{n} \text{ for all } n \geq n_0 \rbrace$.

Prove Theorem 3.1:

If $f(n) = \tilde{\Theta}(g(n))$, then there exist positive constants $c_1$, $c_2$, $k_1$, $k_2$, $n_0$ such that $0 \leq c_1g(n)\lg^{k_1}{(n)} \leq f(n) \leq c_2g(n)\lg^{k_2}{(n)} \text{ for all } n \geq n_0$.

It means: $0 \leq c_1g(n)\lg^{k_1}{(n)} \leq f(n) \text{ for all } n \geq n_0$ and $0 \leq f(n) \leq c_2g(n)\lg^{k_2}{(n)} \text{ for all } n \geq n_0$. They are the definition of $f(n) = \tilde{O}(g(n))$ and $f(n) = \tilde{\Omega}(g(n))$.

If $f(n) = \tilde{O}(g(n))$ and $f(n) = \tilde{\Omega}(g(n))$. Then there exist positive constants $c_1$, $c_2$, $k_1$, $k_2$, $n_1$, $n_2$ such that $0 \leq c_1g(n)\lg^{k_1}{(n)} \leq f(n) \text{ for all } n \geq n_1$ and $0 \leq f(n) \leq c_2g(n)\lg^{k_2}{(n)} \text{ for all } n \geq n_2$. Then we combine them together: $0 \leq c_1g(n)\lg^{k_1}{(n)} \leq f(n) \leq c_2g(n)\lg^{k_2}{(n)} \text{ for all } n \geq max(n_1, n_2)$. So $f(n) = \tilde{\Theta}(g(n))$.

## 3-6
