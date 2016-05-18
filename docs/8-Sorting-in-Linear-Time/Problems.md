# 8-1
### a
There are n! permutations of n inputs, and each permutation is equally likely, thus the probability of each permutation is $\frac{1}{n}$. So there are n! leaves are labeled $\frac{1}{n}$, if there are more than n! leaves, the rest are labeled 0.

### b
The external path length of a tree is the total length of all paths, from the root to the leaves. We have D(T) - D(LT) = leaves of LT, and D(T) - D(RT) = leaves of RT. So D(T) = D(LT) + D(RT) + leaves of LT + leaves of RT = D(LT) + D(RT) + k.

### c
From the previous question, we have D(T) = D(LT) + D(RT) + k, and there are k - 1 permutations of LT and RT, so $d(k) = \min_{1 \leq i \leq k - 1}\lbrace d(i) + d(k - i) + k \rbrace$.

### d
We have:

$$
\begin{eqnarray}
f'(i) &=& (i\lg{i} + (k - i)\lg{(k - i)})' \\\
&=& \lg{i} + i\frac{1}{i\ln2} + (-1)\lg{(k - i)} + (k - i)\frac{1}{(k - i)\ln2}(-1) \\\
&=& \lg{i} + \frac{1}{\ln2} - \lg{(k - i)} - \frac{1}{\ln2} \\\
&=& \lg{\frac{i}{k - i}}
\end{eqnarray}
$$

Let $\lg{\frac{i}{k - i}} \geq 0$, we get $i \geq \frac{k}{2}$, let $\lg{\frac{i}{k - i}} < 0$, we have $i < \frac{k}{2}$, so f(i) is monotonically decreasing at $[1, \frac{k}{2})$ and monotonically increasing at $(\frac{k}{2}, k - 1]$, and $f'(\frac{k}{2}) = 0$, so f(i) is minimized at $i = \frac{k}{2}$.

So $f(\frac{k}{2}) = k(\lg{k} - 1)$.

We assume that $d(k) = \Omega(k\lg{k})$, substituting it to $\min_{1 \leq i \leq k - 1}\lbrace d(i) + d(k - i) + k \rbrace$ yielding:

$$
\begin{eqnarray}
\min_{1 \leq i \leq k - 1}\lbrace d(i) + d(k - i) + k \rbrace &\geq& \min_{1 \leq i \leq k - 1}\lbrace ci\lg{i} + c(k - i)\lg{(k - i)} + k \rbrace \\\
&=& \min_{1 \leq i \leq k - 1}\lbrace c(i\lg{i} + (k - i)\lg{(k - i)}) + k \rbrace \\\
&\geq& c(\frac{k}{2}\lg{\frac{k}{2}} + \frac{k}{2}\lg{\frac{k}{2}}) + k \\\
&=& ck\lg{k} + (1 - c)k \\\
&\geq& ck\lg{k} \\\
&=& \Omega(k\lg{k})
\end{eqnarray}
$$

where the last step holds as long as $c \leq 1$.

So $d(k) = \Omega(k\lg{k})$

### e
We know that $T_A$ has n! leaves, so k = n!, thus, $D(T_A) = d(n!) = \Omega(n!\lg{(n!)})$.

Since each permutation has probability $\frac{1}{n!}$, the average-case time to sort n elements is $\frac{D(T_A)}{n!} = \frac{\Omega(n!\lg{(n!)})}{n!} = \Omega(\lg{(n!)}) = \Omega(n\lg{n})$.

### f
Suppose the randomized decision tree B has k permutations, so there exists a tree in the k permutations that has minimum comparisions, we can pick that tree as the deterministic decision tree A.

## 8-2
### a
Counting sort.

### b
```
SORT-IN-PLACE(A)

i = 1
j = A.length

while i < j
    while A[i] == 0
        i = i + 1

    while A[j] == 1
        j = j - 1

    if i < j
        exchange A[i] with A[j]
```

### c
Insertion sort.

### d
The first algorithm satisfies, and that's the algorithm used in the book.

The second algorithm is not stable, and the third algorithm doesn't run in O(n) time.

### e
```
COUNTING-SORT-IN-PLACE(A, k)

let C[0..k] be a new array
for i = 0 to k
    C[i] = 0
for j = 1 to A.length
    C[A[j]] = C[A[j]] + 1
for i = 1 to k
    C[i] = C[i] + C[i - 1]
i = 1
while i <= A.length
    element = A[i]
    position = C[element]
    if i >= position
        i = i + 1
    else if element != A[position]
        exchange A[i] with A[position]
        C[element] = C[element] - 1
    else
        C[element] = C[element] - 1
```

It's not stable.

## 8-3
### a
```
SORTING-VARIABLE-LENGTH-ITEMS(A)

n = A.length
let B[1..n] be a new array
for i = 1 to n
    let B[i] be a new array
for i = 1 to n
    insert A[i] to B[j], where j is the length of A[i]
for i = 1 to n:
    sort B[i] by RADIX-SORT
concatenate the lists B[1], B[2], ..., B[n] together in order
```

Let $a_i$ be the number of integers which have i digits, so $\sum_{i = 1}^n{a_ii} = n$. The running time of `RADIX-SORT` is $O(dn)$, here we have $d = i, n = a_i$ so the total running time to sort all `B[i]` is $\sum_{i = 1}^nO(ia_i) = O(n)$.

The other for loops also takes O(n), so the running time of the algorithm is still O(n).

### b

