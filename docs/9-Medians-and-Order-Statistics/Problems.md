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
