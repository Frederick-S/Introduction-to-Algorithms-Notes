# Problems
## 5-1
### a
Let's define the indicator random variable $X_i$, for $1 \leq i \leq n$, by:

$$
\begin{eqnarray}
X_i &=& I\lbrace\text{the INCREMENT operation increases the counter}\rbrace \\\
&=& \begin{cases}
      n_{i + 1} - n_i, & \text{the INCREMENT operation increases the counter} \\\
      0, & \text{otherwise}
    \end{cases}
\end{eqnarray}
$$

We have:

$$
\begin{eqnarray}
E[X_i] &=& 0 * Pr\lbrace \text{the INCREMENT operation doesn't increase the counter} \rbrace + (n_{i + 1} - n_i) * Pr\lbrace \text{the INCREMENT operation increases the counter} \rbrace \\\
&=& 0 * (1 - \frac{1}{n_{i + 1} - n_i}) + (n_{i + 1} - n_i) * \frac{1}{n_{i + 1} - n_i} \\\
&=& 1
\end{eqnarray}
$$

Let X be the random variable as the expected value represented by the counter, we have $X = \sum_{i = 1}^{n}X_i$. So:

$$
\begin{eqnarray}
E[X] &=& E[\sum_{i = 1}^{n}X_i] \\\
&=& \sum_{i = 1}^{n}E[X_i] \\\
&=& \sum_{i = 1}^{n}1 \\\
&=& n
\end{eqnarray}
$$

### b
$Var(X_i) = E[X_i^2] - (E[X_i])^2 = 0^2 * (1 - \frac{1}{n_{i + 1} - n_i}) + (n_{i + 1} - n_i)^2 * \frac{1}{n_{i + 1} - n_i} - 1^2 = 100^2 * \frac{1}{100} - 1^2 = 99$.

Because the random variables $X_i$ are uncorrelated, so $Var(X) = Var(\sum_{i = 1}^{n}X_i) = \sum_{i = 1}^{n}Var(X_i) = \sum_{i = 1}^{n}99 = 99n$.

## 5-2
### a
```
RANDOM-SEARCH(A, x)

n = A.length
let B[1..n] be new array

while B is not full
    i = RANDOM(1, n)
    B[i] = i

    if A[i] = x
        return i

return -1
```

### b
This is similar like the question "How many balls must we toss, an the average, until a given bin contains a ball?", the answer is n.

### c
Each time when we pick an index, we have the probability $\frac{k}{n}$ such that we find x in A. So according to C.32, it takes $\frac{1}{\frac{k}{n}} = \frac{n}{k}$ trials before we find x.

### d
This is similar like the question "How many balls must we toss until every bin contains at least one ball?", the answer is $n(\ln{n} + O(1))$.

### e
The best-case running time is 1, and the worst-case running time is n, thus the average-case running time is $\frac{n + 1}{2}$.

### f
The best-case running time is 1, and the worst-case running time is n - k + 1. The average-case running time is $\frac{n + 1}{k + 1}$, here is the [discussion](https://stackoverflow.com/questions/5125525/average-case-running-time-of-linear-search-algorithm).

### g
If there are no indices i such that A[i] = x, then it always scans all elements in A, thus the average-case and worst-case running time are both n.

### h
The worst-case running time is the same as DETERMINISTIC-SEARCH, the expected-case running time is the average-case running time in DETERMINISTIC-SEARCH.

### i
The DETERMINISTIC-SEARCH. It has better average-case running time, and the SCRAMBLE-SEARCH takes additional time to permute the array.