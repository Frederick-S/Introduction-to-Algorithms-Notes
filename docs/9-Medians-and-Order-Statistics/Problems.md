# Problems
## 9-1
### a
Sorting requires $O(n\lg{n})$, plus $O(i)$ to list the i numbers, the total running time is $O(n\lg{n}) + O(i)$.

### b
It requires $O(n)$ to build a max-priority queue, the `EXTRACT-MAX` costs $O(\lg{n})$, thus the total running time is $O(n) + iO(\lg{n})$.

### c
First we need to find the `n - i + 1` smallest element, this requires O(n). And the array is partitioned around the `n - i + 1` smallest element. So we need to sort the `i - 1` numbers, it costs $O((i - 1)\lg{(i - 1)})$, so the total running time is $O(n) + O((i - 1)\lg{(i - 1)})$.

## 9-2
### a
The median of $x_1, x_2, \ldots, x_n$ is $x_{\lceil \frac{n}{2} \rceil}$. So $\sum_{x_i < x_k} w_i = \frac{1}{n}(\lceil \frac{n}{2} \rceil - 1) < \frac{1}{n}(\frac{n}{2} + 1 - 1) = \frac{1}{2}$. $\sum_{x_i > x_k} w_i = \frac{1}{n}(n - \lceil \frac{n}{2} \rceil) \leq \frac{1}{n}(n - \frac{n}{2}) = \frac{1}{2}$.

### b
First we sort the elements, and then iterate the sorted elements and sum the corresponding weight, if the sum of weights is bigger than 0.5, then the current element is the weighted median.

```
WEIGHTED-MEDIAN(A)

SORT(A)
weight-sum = 0
for i = 1 to n
    weight-sum += get weight of A[i]
    if weight-sum >= 0.5:
        return A[i]
```

We need $O(n\lg{n})$ to sort all elements, and need O(n) to find the weighted median, the total running time is thus $O(n\lg{n}) + O(n) = O(n\lg{n})$.

### c
First we get the median of all x, and sum the weights of elements whose value is less than median, and sum the weights of elements whose value is larger than median. If the sum of weights in left part is smaller than 0.5 and the sum of weights in right part is also not larger than 0.5, then the median is weighted median. Otherwise, we do the same procedure on the on the left part if its sum of weights is larger than 0.5, or the right part.

```
WEIGHTED-MEDIAN(A)

if n = 1
    return A[1]
if n = 2
    if A[1].weight >= A[2].weight
        return A[1]
    else
        return A[2]
else
    median = SELECT(A, MATH.CEIL(A / 2))
    left-weights = 0
    right-weights = 0
    for i = 1 to MATH.CEIL(A / 2) - 1
        left-weights = left-weights + A[i].weight
    for i = MATH.CEIL(A / 2) + 1 to n
        right-weights = right-weights + A[i].weight
    if left-weights < 0.5 and right-weights <= 0.5
        return median
    elseif left-weights >= 0.5
        median.weight = median.weight + right-weights
        A' = { x <= median }
        return WEIGHTED-MEDIAN(A')
    elseif right-weights > 0.5
        median.weight = median.weight + left-weights
        A' = { x >= median }
        return WEIGHTED-MEDIAN(A')
```

The recurrence of the algorithm is $T(n) = T(\frac{n}{2}) + \Theta(n)$. Let's solve it by the master method. Here we have a = 1, b = 2, $f(n) = \Theta(n)$. So $\log_b{a} = \log_2{1} = 0$, so $f(n) = \Omega(n^{\log_b{a} + \epsilon})$ for $\epsilon = 0.5$. And $af(\frac{n}{b}) = f(\frac{n}{2}) \leq cf(n)$ for $c = \frac{1}{2}$ and all sufficiently large n, thus $T(n) = \Theta(f(n)) = \Theta(n)$.

### d
Let p denotes the weighted median, so $f(p) = \sum_{i = 1}^n w_id(p - p_i) = \sum_{i = 1}^n w_i|p - p_i|$. Since we need to prove the weighted median is the best solution, so for any other point x other than p we should have $f(x) \geq f(p)$, or $f(x) - f(p) \geq 0$.

So $f(x) - f(p) = \sum_{i = 1}^n w_i|x - p_i| - \sum_{i = 1}^n w_i|p - p_i| = \sum_{i = 1}^n w_i(|x - p_i| - |p - p_i|)$.

First let's check the situation when x < p.

When $p_i \leq x < p$, $|x - p_i| - |p - p_i| = x - p_i - (p - p_i) = x - p$, when $x < p_i < p$, $|x - p_i| - |p - p_i| = (p_i - x) - (p - p_i) > 0 - (p - x) = x - p$. When $x < p \leq p_i$, $|x - p_i| - |p - p_i| = p_i - x - (p_i - p) = p - x$.

Thus:

$$
\begin{eqnarray}
\sum_{i = 1}^n w_i(|x - p_i| - |p - p_i|) &>& (x - p)\sum_{p_i < p}w_i + (p - x)\sum_{p_i \geq p}w_i \\\
&=& (p - x)(\sum_{p_i \geq p}w_i - \sum_{p_i < p}w_i)
\end{eqnarray}
$$

Because p is weighted median, so $\sum_{p_i \geq p}w_i > \frac{1}{2}$, $\sum_{p_i < p}w_i < \frac{1}{2}$, so $(p - x)(\sum_{p_i \geq p}w_i - \sum_{p_i < p}w_i) > 0$.

Now let's check the situation when x > p.

When $p_i \leq p < x$, $|x - p_i| - |p - p_i| = x - p_i - (p - p_i) = x - p$, when $p < p_i < x$, $|x - p_i| - |p - p_i| = x - p_i - (p_i - p) > 0 - (x - p) = p - x$, when $p < x \leq p_i$, $|x - p_i| - |p - p_i| = p_i - x - (p_i - p) = p - x$.

Thus:

$$
\begin{eqnarray}
\sum_{i = 1}^n w_i(|x - p_i| - |p - p_i|) &>& (p - x)\sum_{p_i > p}w_i + (x - p)\sum_{p_i \leq p}w_i \\\
&=& (x - p)(\sum_{p_i \leq p}w_i - \sum_{p_i > p}w_i)
\end{eqnarray}
$$

Because $\sum_{p_i \leq p}w_i > \frac{1}{2}$ and $\sum_{p_i > p}w_i < \frac{1}{2}$, so $(x - p)(\sum_{p_i \leq p}w_i - \sum_{p_i > p}w_i) > 0$.

So for any point x other than p we have $f(x) > f(p)$, so the weighted median is the best solution.

### e
We need to find a point p(x, y) such that $\sum_{i = 1}^n w_i(|x - x_i| + |y - y_i|)$ is minimum. Because $\sum_{i = 1}^n w_i(|x - x_i| + |y - y_i|) = \sum_{i = 1}^n w_i|x - x_i| + \sum_{i = 1}^n w_i|y - y_i|$, the problem is actually 2 1-dimensional problems. Thus let x be the weighted median of all x coordinate values, and let y be the weighted median of all y coordinate values, so p(x, y) is the best solution.

## 9-3
### a
If $i \geq \frac{n}{2}$, then we use the `SELECT` algorithm, otherwise we group every two elements into pairs $(a_j, b_j)$ and make sure $a_j \leq b_j$, if n is odd, we also let the last element be a pair, this step needs $\lfloor \frac{n}{2} \rfloor$. So now we have $\lceil \frac{n}{2} \rceil$ pairs. Then we recursively call the algorithm on $a_j$, so we can get the ith smallest element of all $a_j$, this step requires $U_i(\lceil \frac{n}{2} \rceil)$. Notice that the partition method partition all $a_j$ into two parts, so the ith smallest element of all elements could only be among $a_1\ldots{a_i}$ and $b_1\ldots{b_i}$. Then we run the `SELECT` algorithm on the 2i elements to find the ith smallest element.

```
SMALL-ORDER-STATISTICS(A, i)
if i >= n / 2
    return SELECT(A, i)
let pairs be a new array
for i = 1 to n with step = 2
    if i + 1 <= n
        if A[i] <= A[i + 1]
            insert [A[i], A[i + 1]] into pairs
        else
            insert [A[i + 1], A[i]] into pairs
    else
        insert [A[i]] into pairs
SMALL-ORDER-STATISTICS(pairs, i) // Run algorithm on all aj
return SELECT(pairs, i) // Run algorithm on a1 to ai plus b1 to bi
```

### b
Let's solve by the substitution method. We start by assuming that $U_i(n) = n + O(T(2i)\lg(\frac{n}{i}))$ holds for all positive m < n, in particular for $m = \lceil \frac{n}{2} \rceil$, yielding $U_i(\lceil \frac{n}{2} \rceil) = \lceil \frac{n}{2} \rceil + O(T(2i)\lg(\frac{\lceil \frac{n}{2} \rceil}{i}))$. Substituting into the recurrence yields:

$$
\begin{eqnarray}
U_i(n) &=& \lfloor \frac{n}{2} \rfloor + \lceil \frac{n}{2} \rceil + O(T(2i)\lg(\frac{\lceil \frac{n}{2} \rceil}{i})) + T(2i) \\\
&=& n + O(T(2i)\lg(\frac{\lceil \frac{n}{2} \rceil}{i})) + O(T(2i)) \\\
&=& n + O(T(2i)(\lg(\frac{\lceil \frac{n}{2} \rceil}{i}) + 1)) \\\
&=& n + O(T(2i)(\lg(\frac{\lceil \frac{n}{2} \rceil}{i}) + \lg2)) \\\
&=& n + O(T(2i)\lg(\frac{n}{i}))
\end{eqnarray}
$$

### c
If i is a constant, and because $T(n) = O(n)$, so T(2i) = O(2i), so T(2i) is also a constant, and $O(\lg{\frac{n}{i}}) = O(\lg{n})$. Thus $U_i(n) = n + O(T(2i)\lg(\frac{n}{i})) = n + O(\lg{n})$.

### d
It's so obvious, we just replace i with $\frac{n}{k}$ and yields $U_i(n) = n + O(T(2i)\lg(\frac{n}{i})) = n + O(T(2\frac{n}{k})\lg(\frac{n}{\frac{n}{k}})) = n + O(T(\frac{2n}{k})\lg{k})$.

## 9-4
### a
$z_i$ and $z_j$ are compared if and only if the first element to be chosen as a pivot from $Z_{ijk}$ is either $z_i$ or $z_j$. And the range of $Z_{ijk}$ depends on k. So:

$$
\begin{eqnarray}
E[X_{ijk}] &=&
    \begin{cases}
      \frac{2}{j - k + 1} & \text{if } k \leq i < j \\\
      \frac{2}{j - i + 1} & \text{if } i < k \leq j \\\
      \frac{2}{k - i + 1} & \text{if } i < j < k
    \end{cases}
\end{eqnarray}
$$

### b
$$
\begin{eqnarray}
E[X_k] &=& \sum_{i = 1}^{n - 1}\sum_{j = i + 1}^n E[X_{ijk}] \\\
&=& \sum_{i = k}^{n - 1}\sum_{j = i + 1}^{n} E[X_{ijk}] + \sum_{i = 1}^{k - 1}\sum_{j = k}^{n} E[X_{ijk}] + \sum_{i = 1}^{k - 2}\sum_{j = i + 1}^{k - 1} E[X_{ijk}] \\\
&=& \sum_{i = k}^{n - 1}\sum_{j = i + 1}^{n} \frac{2}{j - k + 1} + \sum_{i = 1}^{k - 1}\sum_{j = k}^{n} \frac{2}{j - i + 1} + \sum_{i = 1}^{k - 2}\sum_{j = i + 1}^{k - 1} \frac{2}{k - i + 1} \\\
&=& 2(\sum_{i = k}^{n - 1}\sum_{j = i + 1}^{n} \frac{1}{j - k + 1} + \sum_{i = 1}^{k - 1}\sum_{j = k}^{n} \frac{1}{j - i + 1} + \sum_{i = 1}^{k - 2}\sum_{j = i + 1}^{k - 1} \frac{1}{k - i + 1}) \\\
&=& 2(\sum_{i = k}^{n - 1}\sum_{j = i + 1}^{n} \frac{1}{j - k + 1} + \sum_{i = 1}^{k - 1}\sum_{j = k}^{n} \frac{1}{j - i + 1} + \sum_{i = 1}^{k - 2} \frac{k - i - 1}{k - i + 1}) \\\
&=& 2(\sum_{i = k}^{n - 1}\sum_{j = i + 1}^{n} \frac{1}{j - k + 1} + \sum_{i = 1}^{k}\sum_{j = k}^{n} \frac{1}{j - i + 1} - \sum_{j = k}^n \frac{1}{j - k + 1} + \sum_{i = 1}^{k - 2} \frac{k - i - 1}{k - i + 1}) \\\
&=& 2(\sum_{i = 1}^{k}\sum_{j = k}^{n} \frac{1}{j - i + 1} + \sum_{i = k}^{n - 1}\sum_{j = i + 1}^{n} \frac{1}{j - k + 1} - \sum_{j = k}^n \frac{1}{j - k + 1} + \sum_{i = 1}^{k - 2} \frac{k - i - 1}{k - i + 1})
\end{eqnarray}
$$

### c
We have $\sum_{i = 1}^{k}\sum_{j = k}^{n} \frac{1}{j - i + 1} \leq n$ ([source](https://math.stackexchange.com/questions/529208/inequality-sumk-i-1-sumn-j-k1-overj-i-1-le-n)), and $\sum_{k + 1}^n \frac{j - k - 1}{j - k + 1} + \sum_{i = 1}^{k - 2} \frac{k - i - 1}{k - i + 1} < \sum_{k + 1}^n 1 + \sum_{i = 1}^{k - 2} 1 = n - k + k - 2 = n - 2 < n$, so $E[X_k] \leq 2(n + n) = 4n$.

### d
Since $E[X_k] \leq 4n$, thus $T(n) = O(n)$.