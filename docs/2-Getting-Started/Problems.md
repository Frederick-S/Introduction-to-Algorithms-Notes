# Problems
## 2-1 Insertion sort on small arrays in merge sort
a. Show that insertion sort can sort the $n / k$ sublists, each of length k, in $\Theta(nk)$ worst-case time.

We know that the worst-case running time of sorting $n$ elements with insertion sort is $\Theta(n^2)$. So the running time of sorting $k$ elements is $\Theta(k^2)$. And there are $\frac{n}{k}$ sublists of length $k$, so the whole running time is $\frac{n}{k} * \Theta(k^2) = \Theta(nk)$.

b. Show how to merge the sublists in $\Theta(n\lg{n / k})$ worst-case time.

We can go back to look at figure 2.5 in the book. In original merge sort, there are $n$ elements at the bottom in recursion tree. In each step, current array will be divided into two subarrays, until the array only contains one element. But in the modified algorithm, this operation stops when current array contains less than $k$ elements. Thus, it stops after $\lg{\frac{n}{k}}$ recursions. So the height of recursion tree is $\lg{\frac{n}{k}} + 1$. Because each level contributes a cost of $\Theta(n)$ merge operation, the total merge running time is $\Theta(n)(\lg{\frac{n}{k}} + 1) = \Theta(n\lg{\frac{n}{k}})$.

c. What is the largest value of $k$ as a function of $n$ for which the modified algorithm has the same running time as standard merge sort, in terms of $\Theta$-notation?

Given the modified algorithm runs in $\Theta(nk + n\lg{\frac{n}{k}})$ worst-case time, we know $n\lg{\frac{n}{k}} \leq n\lg{n}$, so this part will not influence the upper bound running time. Thus $nk$ is responsible for the worst-case running time of the modified algorithm. And we can see if $k$ is larger than $\lg{n}$, the modified algorithm will not have the same running time as the standard merge sort algorithm. So the largest value of $k$ is $\lg{n}$.

d. How should we choose $k$ in practice?

The optimum value of $k$ is system dependent. The optimum value on one machine may not be optimum on another machine.
