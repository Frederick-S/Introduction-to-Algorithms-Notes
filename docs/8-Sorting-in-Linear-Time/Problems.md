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
We can build a deterministic decision tree A from the randomized decision tree B. We go through all nodes in B, for each node, we pick the child that has the minimum cost, and delete other children. Thus we build a deterministic tree, which is a permutation of B. And we already know the running time of deterministic decision tree is $\Omega(n\lg{n})$. So we can find a deterministic comparsion sort A whose expected number of comparisions is no more thant those made by B.

## 8-2
