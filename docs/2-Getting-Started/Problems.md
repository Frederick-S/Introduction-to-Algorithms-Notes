# Problems
## 2-1
### a
We know that the worst-case running time of sorting $n$ elements with insertion sort is $\Theta(n^2)$. So the running time of sorting $k$ elements is $\Theta(k^2)$. And there are $\frac{n}{k}$ sublists of length $k$, so the whole running time is $\frac{n}{k} * \Theta(k^2) = \Theta(nk)$.
