# Problems
## 6-1
### a
Let `A = [1, 2, 3, 4]`, if we use `BUILD-MAX-HEAP`, we have `A = [4, 2, 3, 1]`. If we use `BUILD-MAX-HEAP'`, we have `A = [4, 3, 2, 1]`. That's a counterexample.

### b
The worst-case happens when A is in increasing order, in each iteration, `MAX-HEAP-INSERT(A, A[i])` requires $O(\lg{k})$ to heapify the heap (move `A[i]` from bottom to top), where k is the number of elements in heap. Thus the running time is $\sum_{i = 2}^{n}\lg{i} = \lg{(n!)} = \Theta(n\lg{n})$.

## 6-2
### a
For a node with index i (i = 1, 2, ..., n), its kth child index is `d(i - 1) + k + 1` in array, and its parent's index is $\lceil \frac{i - 1}{d} \rceil$.

### b
The max number of elements in d-ary heap is $d^0 + d^1 + \ldots + d^h = \sum_{i = 0}^{h}d^h = \frac{d^{h + 1} - 1}{d - 1}$, the min number of elements in d-ary heap is $d^0 + d^1 + \ldots + d^{h - 1} + 1 = \sum_{i = 0}^{h}d^{h - 1} + 1 = \frac{d^h - 1}{d - 1} + 1$. Thus, $\frac{d^h - 1}{d - 1} + 1 \leq n \leq \frac{d^{h + 1} - 1}{d - 1}$.

For a d-ary heap, we have $d \geq 2$. Let's check the left part first. $\frac{d^h - 1}{d - 1} + 1 = \frac{d^h - 1 + (d - 2)}{d - 1} \geq \frac{d^h - 1}{d - 1}$, so $h \leq \log_d{(n(d - 1) + 1)}$. And:

$$
\begin{eqnarray}
\log_d{(n(d - 1) + 1)} - (\log_d{(n(d - 1))} + 1)  &=& \log_d{(\frac{1}{d}(1 + \frac{1}{n(d - 1)}))} \\\
&\leq& \log_d{(\frac{1}{d}(1 + \frac{1}{d - 1}))} \\\
&=& \log_d{\frac{1}{d - 1}} \\\
&\leq& \log_d{\frac{1}{\frac{d}{2}}} \\\
&=& \log_d{\frac{2}{d}} \\\
&=& \log_d2 - 1 \\\
&\leq& \log_2{2} - 1 \\\
&=& 0
\end{eqnarray}
$$

So $\log_d{(n(d - 1) + 1)} \leq \log_d{(n(d - 1))} + 1$, if n = 1 and d = 2, we have $\log_d{(n(d - 1) + 1)} = \log_d{(n(d - 1))} + 1$, for a d-ary heap, n is usually not 1, so we can say $\log_d{(n(d - 1) + 1)} < \log_d{(n(d - 1))} + 1$. Thus we have $h < \log_d{(n(d - 1))} + 1$.

Then let's check the right part. $\frac{d^{h + 1} - 1}{d - 1} < \frac{d^{h + 1}}{d - 1}$, so $h > \log_d{(n(d - 1))} - 1$.

So $h = \lfloor \log_d{(n(d - 1))} \rfloor$.

### c
It's similar like `EXTRACT-MAX` 2-ary heap. The running time of `EXTRACT-MAX` for d-ary heap is mainly the running time of `MAX-HEAPIFY`. We need to change `MAX-HEAPIFY` a little bit.
```
MAX-HEAPIFY(A, i)
largest = i
for i = 1 to d
    child = CHILD(i)
    if child <= A.heap-size and A[child] > A[largest]
        largest = child
if largest != i
    exchange A[i] with A[largest]
    MAX-HEAPIFY(A, largest)
```

So the running time of `MAX-HEAPIFY` for d-ary heap is $O(dh) = O(d\log_d{(n(d - 1))})$.

### d
The `INSERT` method only compares node i with its parent, so the running time is $O(h) = O(\log_d{(n(d - 1))})$.

### e
Since the `INSERT` method calls `INCREASE-KEY` method, the running time of `INCREASE-KEY` is also $O(h) = O(\log_d{(n(d - 1))})$.

## 6-3
### a
