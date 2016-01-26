# Problems
## 4-1
### a
Here, we have a = 2, b = 2, and $f(n) = \Theta(n^4)$, and thus we have that $n^{\log_ba} = n^{\log_2{2}} = n$. Since $f(n) = \Omega(n^{\log_b{a} + \epsilon})$, where $\epsilon \leq 3$, case 3 applies. And for sufficiently large n, we have that $af(\frac{n}{b}) = 2f(\frac{n}{2}) = \frac{n^4}{8} = cf(n)$, for $c = \frac{1}{8}$. So, the solution to the recurrence is $T(n) = \Theta(n^4)$.

### b
Here, we have a = 1, $b = \frac{10}{7}$, and $f(n) = \Theta(n)$, and thus we have that $n^{\log_ba} = n^{\log_{\frac{10}{7}}{1}} = 1$. Since $f(n) = \Omega(n^{\log_b{a} + \epsilon})$, where $\epsilon \leq 1$, case 3 applies. And for sufficiently large n, we have that $af(\frac{n}{b}) = f(\frac{7n}{10}) = \frac{7n}{10} = cf(n)$, for $c = \frac{7}{10}$. So, the solution to the recurrence is $T(n) = \Theta(n)$.

### c
Here, we have a = 16, b = 4, and $f(n) = \Theta(n^2)$, and thus we have that $n^{\log_ba} = n^{\log_4{16}} = n^2$. So case 2 applies, so the solution to the recurrence is $T(n) = \Theta(n^2\lg{n})$.

### d
Here, we have a = 7, b = 3, and $f(n) = \Theta(n^2)$, and thus we have that $n^{\log_ba} = n^{\log_3{7}}$. Since $f(n) = \Omega(n^{\log_b{a} + \epsilon})$, where $\epsilon \leq 2 - \log_3{7}$, case 3 applies. And for sufficiently large n, we have that $af(\frac{n}{b}) = 7f(\frac{n}{3}) = \frac{7n^2}{9} = cf(n)$, for $c = \frac{7}{9}$. So, the solution to the recurrence is $T(n) = \Theta(n^2)$.

### e
Here, we have a = 7, b = 2, and $f(n) = \Theta(n^2)$, and thus we have that $n^{\log_ba} = n^{\log_2{7}} = n^{\lg{7}}$. Since $f(n) = O(n^{\log_b{a} - \epsilon})$, where $\epsilon \leq \lg{\frac{7}{4}}$, case 1 applies. So, the solution to the recurrence is $T(n) = \Theta(n^{\lg7})$.

### f
Here, we have a = 2, b = 4, and $f(n) = \Theta(\sqrt{n})$, and thus we have that $n^{\log_ba} = n^{\log_4{2}} = \sqrt{n}$, case 2 applies. So, the solution to the recurrence is $T(n) = \sqrt{n}\lg{n}$.

### g
