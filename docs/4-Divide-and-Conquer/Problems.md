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
First let's create a recursion tree for the recurrence $T(n) = T(n - 2) + n^2$.

```
\documentclass{standalone} 
\usepackage{tikz}
\usetikzlibrary{positioning}

\tikzset{
    no edge from this parent/.style={
        every child/.append style={
        edge from parent/.style={draw=none}}},
    level 4/.style={level distance=6mm} 
}

\begin{document}
\begin{tikzpicture}

\node (root){$n^2$} 
    child {node {$(n - 2)^2$}
        child {node {$(n - 4)^2$}
            child {node {$\vdots$}[no edge from this parent]
                child {node {T(1)}}}}};

\node[right=1 of root] {$n^2$}[no edge from this parent]
    child {node {$(n - 2)^2$}[no edge from this parent]
        child {node {$(n - 4)^2$}[no edge from this parent]
            child {node {}[no edge from this parent]
                child {node {$\Theta(1)$}}}}};
\end{tikzpicture}
\end{document}
```

![Alt text](4.1-g.png)

The number of nodes at depth i is 1. And each node at depth i, for $i = 0, 1, 2, \ldots, \frac{n - 1}{2} - 1$, has a cost of $(n - 2i)^2$. So the total cost over all nodes at depth i, is $(n - 2i)^2$. The bottom level, at depth $\frac{n - 1}{2}$, has 1 node, which contributing cost T(1), for a total cost of T(1), which is $\Theta(1)$. So:

$$
\begin{eqnarray}
T(n) &=& \sum_{i = 0}^{\frac{n - 1}{2} - 1}(n - 2i)^2 + \Theta(1) \\\
&=& \sum_{i = 0}^{\frac{n - 1}{2} - 1}(n^2 - 2ni + 4i^2) + \Theta(1) \\\
&=& \sum_{i = 0}^{\frac{n - 1}{2} - 1}n^2 - \sum_{i = 0}^{\frac{n - 1}{2} - 1}2ni + \sum_{i = 0}^{\frac{n - 1}{2} - 1}4i^2 + \Theta(1) \\\
&=& \frac{n - 1}{2}n^2 - 2n\frac{(\frac{n - 1}{2} - 1)(1 + \frac{n - 1}{2} - 1)}{2} + 4\frac{(\frac{n - 1}{2} - 1)(\frac{n - 1}{2} - 1 + 1)(2(\frac{n - 1}{2} - 1) + 1)}{6} + \Theta(1) \\\
&=& \frac{n^2(n - 1)}{2} - \frac{n(n - 1)(n - 3)}{4} + \frac{(n - 1)(n - 2)(n - 3)}{6} + \Theta(1) \\\
&=& \frac{5n^3 - 6n^2 + 13n -12}{6} + \Theta(1) \\\
&=& \Theta(n^3)
\end{eqnarray}
$$

Thus, we have derived a guess of $T(n) = \Theta(n^3)$ for our original recurrence. Now let's use the substitution method to verify that our guess was correct. We want to show that $T(n) \geq c_1n^3$ and $T(n) \leq c_2n^3$ for some constants $c_1 > 0$ and $c_2 > 0$. So:

$$
\begin{eqnarray}
T(n) &=& T(n - 2) + n^2 \\\
&\geq& c_1(n - 2)^3 + n^2 \\\
&=& c_1n^3 + (1 - 6c_1)n^2 + 4c_1(3n - 2) \\\
&>& c_1n^3
\end{eqnarray}
$$

where the last step holds as long as $c_1 \leq \frac{1}{6}$.

So $T(n) = \Omega(n^3)$.

And:

$$
\begin{eqnarray}
T(n) &=& T(n - 2) + n^2 \\\
&\leq& c_2(n - 2)^3 + n^2 \\\
&=& c_2n^3 + n((1 - 6c_2)n + 12c_2) - 8c_2 \\\
&\leq& c_2n^3
\end{eqnarray}
$$

where the last step holds as long as $c_2 > \frac{1}{6}$ and $n \geq \frac{12c_2}{6c_2 - 1}$.

So $T(n) = O(n^3)$, thus $T(n) = \Theta(n^3)$.

## 4-2
### a
Here is the pseudocode of recursive binary search algorithm:

```
RECURSIVE-BINARY-SEARCH(A, v, low, high)

if low <= high
    middle = (low + high) / 2

    if A[middle] < v
        return RECURSIVE-BINARY-SEARCH(A, v, middle + 1, high)
    else if A[middle] > v
        return RECURSIVE-BINARY-SEARCH(A, v, low, middle - 1)
    else
        return middle

return NIL
```

#### An array is passed by pointer
Before it halves the problem size, it needs to do some operations like comparing `low` and `high`, calculating `middle`. But they are constant operations, we can let it be $\Theta(1)$.

So $T(n) = T(\frac{n}{2}) + \Theta(1)$. Here, we have a = 1, b = 2, and $f(n) = \Theta(1)$, and thus we have that $n^{\log_ba} = n^{\log_2{1}} = 1$. So case 2 applies, thus $T(n) = \Theta(n^{\log_ba}\lg{n}) = \Theta(\lg{n}) = \Theta(\lg{N})$.

#### An array is passed by copying
Each time it halves the problem size, it needs additional $\Theta(N)$ operation to copy the array. So $T(n) = T(\frac{n}{2}) + \Theta(N) + \Theta(1) = T(\frac{n}{2}) + \Theta(N) = T(\frac{n}{4}) + \Theta(N) + \Theta(N) = \ldots = T(1) + \lg{n}\Theta(N) = \Theta(N\lg{N})$.

#### An array is passed by range
Each time it halves the problem size, it needs additional $\Theta(n)$ operation to copy the array. So $T(n) = T(\frac{n}{2}) + \Theta(n) + \Theta(1) = T(\frac{n}{2}) + \Theta(n)$.

Here, we have a = 1, b = 2, and $f(n) = \Theta(n)$, and thus we have that $n^{\log_ba} = n^{\log_2{1}} = 1$. Since $f(n) = \Omega(n^{\log_b{a} + \epsilon})$, where $\epsilon \leq 1$, case 3 applies. And for sufficiently large n, we have that $af(\frac{n}{b}) = f(\frac{n}{2}) = \Theta(\frac{n}{2}) = c\Theta(n)$, for $c = \frac{1}{2}$. So, the solution to the recurrence is $T(n) = \Theta(n) = \Theta(N)$.

### b
Here is the pseudocode of merge sor algorithm:

```
MERGE-SORT(A, p, r)

if p < r
    q = (p + r) / 2
    MERGE-SORT(A, p ,q)
    MERGE-SORT(A, q + 1, r)
    MERGE(A, p, q, r)
```

#### An array is passed by pointer
We already know the solution that $T(n) = \Theta(n\lg{n}) = \Theta(N\lg{N})$.

#### An array is passed by copying
From the pseudocode we know it needs to pass the array 3 times to subroutine. So we have $T(n) = 2T(\frac{n}{2}) + \Theta(n) + 3\Theta(N) = 2T(\frac{n}{2}) + \Theta(n) + \Theta(N)$. Let's use the iterative method to solve it:

$$
\begin{eqnarray}
T(n) &=& 2T(\frac{n}{2}) + \Theta(n) + \Theta(N) \\\
&=& 2(2T(\frac{n}{4}) + \Theta(\frac{n}{2}) + \Theta(N)) + \Theta(n) + \Theta(N) \\\
&=& 4T(\frac{n}{4}) + 2\Theta(\frac{n}{2}) + 2\Theta(N) + \Theta(n) + \Theta(N) \\\
&=& 4T(\frac{n}{4}) + 2\Theta(n) + 3\Theta(N) \\\
&=& \ldots \\\
&=& 2^iT(\frac{n}{2^i}) + i\Theta(n) + (1 + 2 + \ldots + 2^{i - 1})\Theta(N) \text{ for } i = 1, 2, \ldots, \lg{n} \\\
&=& 2^{\lg{n}}T(1) + \lg{n}\Theta(n) + \Theta(N)\frac{1 - 2^{\lg{n}}}{1 - 2} \\\
&=& nT(1) + \Theta(n\lg{n}) + \Theta(Nn) \\\
&=& \Theta(N^2)
\end{eqnarray}
$$

#### An array is passed by range
It needs additional $3\Theta(n)$ to copy the array. So $T(n) = 2T(\frac{n}{2}) + \Theta(n) + 3\Theta(n) = 2T(\frac{n}{2}) + \Theta(n) = \Theta(n\lg{n}) = \Theta(N\lg{N})$.

## 4-3
