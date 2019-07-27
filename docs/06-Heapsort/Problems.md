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
$$
\begin{matrix}
2 & 3 & 4 & 5 \\\
8 & 9 & 12 & 14 \\\
16 & \infty & \infty & \infty \\\
\infty & \infty & \infty & \infty
\end{matrix}
$$

### b
If $Y[1, 1] = \infty$, then no cell can has a value greater than `Y[1, 1]`, other cells are all $\infty$, so Y is empty.

`Y[m, n]` is the largest in Y, if it's not $\infty$, then others are also not $\infty$, so Y is full.

### c
`Y[1, 1]` is the smallest, after we extract it, we need to make Y to a Young tableau again.

First we start at `Y[1, 1]`, then we compare its right element and below element, if right element is smaller than below element, we put right element to `Y[1, 1]`, which makes `Y[1, 1]` to `Y[1, m]` sorted, but `Y[1, 2]` to `Y[m, n]` might be not a Young tableau.

if right element is greater than below element, we put below element to `Y[1, 1]`, which makes `Y[1, 1]` to `Y[1, n]` sorted, but `Y[2, 1]` to `Y[m, n]` might be not a Young tableau.

```
EXTRACT-MIN(Y)
smallest = Y[1, 1]
Y[1, 1] = ∞
YOUNGIFY(Y, 1, 1)
return smallest

YOUNGIFY(Y, row, column)
smallest_row = row
smallest_column = column
if row + 1 <= m and Y[row + 1, column] < Y[row, column]
    smallest_row = row + 1
if column + 1 <= n and Y[row, column + 1] < Y[smallest_row, smallest_column]
    smallest_row = row
    smallest_column = column + 1
if smallest_row != row or smallest_column != column
    exchange Y[row, column] with Y[smallest_row, smallest_column]
    YOUNGIFY(Y, smallest_row, smallest_column)
```

After each recursive procedure, the `YOUNGIFY` method cuts a row or a column, which reduces the problem size to (m - 1) x n or m x (n - 1). Notice that both (m - 1) + n = m + n - 1 and m + (n - 1) = m + n - 1, so m + n is decreased by 1 in each recursive procedure. so T(p) = T(p - 1) + O(1), it's obvious to know that T(p) = O(p) = O(m + n).

### d
Similar like `EXTRACT-MIN`, we first put the new element to `Y[m, n]`, then youngify the tableau from `Y[m, n]`. The running time is O(m + n).

```
INSERT(Y, key)
Y[m][n] = key
YOUNGIFY-INSERT(Y, m, n)

YOUNGIFY-INSERT(Y, row, column)
largest_row = row
largest_column = column
if row - 1 >= 1 and Y[row - 1][column] > Y[row][column]
    largest_row = row - 1
if column - 1 >= 1 and Y[row][column - 1] > Y[largest_row][largest_column]
    largest_row = row
    largest_column = column - 1
if largest_row != row or largest_column != column
    exchange Y[row, column] with Y[largest_row, largest_column]
    YOUNGIFY-INSERT(Y, largest_row, largest_column)
```

### e
The `INSERT` operation takes O(n + n) = O(n) time, and there are $n^2$ elements, so we can insert each element into the n x n Young tableau, thus the running time is $n^2O(n) = O(n^3)$.

### f
We start from `Y[m, 1]`, and compare `Y[m, 1]` with target value, if `Y[m, 1]` is greater than target value, we move to `Y[m - 1, 1]`, if it's smaller than target value, we move to `Y[m, 2]`, otherwise, we find the target value.

```
FIND(Y, key)
row = m
column = 1
while row >= 1 and column <= n
    if Y[row][column] == key
        return True
    else if Y[row][column] < key
        column += 1
    else if Y[row][column] > key
        row -= 1
return False
```

Similar like `YOUNGIFY`, it reduces the problem size to (m - 1) * n or m * (n - 1), so the running time is O(m + n).