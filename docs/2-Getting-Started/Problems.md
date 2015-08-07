# Problems
## 2-1 Insertion sort on small arrays in merge sort
a. Show that insertion sort can sort the $n / k$ sublists, each of length k, in $\Theta(nk)$ worst-case time.

We know that the worst-case running time of sorting $n$ elements with insertion sort is $\Theta(n^2)$. So the running time of sorting $k$ elements is $\Theta(k^2)$. And there are $\frac{n}{k}$ sublists of length $k$, so the whole running time is $\frac{n}{k} * \Theta(k^2) = \Theta(nk)$.

b. Show how to merge the sublists in $\Theta(n\lg{n / k})$ worst-case time.

We can go back to look at figure 2.5 in the book. In original merge sort, there are $n$ elements at the bottom in recursion tree. In each step, current array will be divided into two subarrays, until the array only contains one element. But in the modified algorithm, this operation stops when current array contains less than $k$ elements. Thus, it stops after $\lg{\frac{n}{k}}$ recursions. So the height of recursion tree is $\lg{\frac{n}{k}} + 1$. Because each level contributes a cost of $\Theta(n)$ merge operation, the total merge running time is $\Theta(n)(\lg{\frac{n}{k}} + 1) = \Theta(n\lg{\frac{n}{k}})$.

c. What is the largest value of $k$ as a function of $n$ for which the modified algorithm has the same running time as standard merge sort, in terms of $\Theta$-notation?

Given the modified algorithm runs in $\Theta(nk + n\lg{\frac{n}{k}})$ worst-case time, we know $n\lg{\frac{n}{k}} \leq n\lg{n}$, so this part will not influence the upper bound running time. Thus $nk$ is responsible for the worst-case running time of the modified algorithm. And we can see if $k$ is larger than $\lg{n}$, the modified algorithm will not have the same running time as the standard merge sort algorithm. So the largest value of $k$ is $\lg{n}$.

d. How should we choose $k$ in practice?

The optimum value of $k$ is system dependent. A optimum value on one machine may not be optimum on another machine.

## 2-2 Correctness of bubblesort
a. In order to show that BUBBLESORT actually sorts, what else do we need to prove?

We need to prove the array A' consists of the elements originally in A.

b. State precisely a loop invariant for the for loop in lines 2-4, and prove that this loop invariant holds.

Loop invariant:

**At the start of each iteration of the for loop of lines 2-4, A[j] is the smallest in the subarray A[j..n]**.

**Initialization**: at the start of the iteration, j is n, and the subarray A[j..n] only contains one element, which is of course the smallest.

**Maintenance**: if it is true before an iteration of the loop, we have A[j] is the smallest one in the subarray A[j..n]. Then we compare A[j - 1] and A[j], if A[j - 1] is smaller, we exchange A[j] with A[j - 1], thus A[j - 1] is the smallest one in the subarray A[j - 1..n]. So it remains true before the next iteration.

**Termination**: it terminates when j equals to i. And when it terminates, we know A[i] is the smallest element in the subarray A[i..n]. So the loop invariant is correct.

c. Using the termination condition of the loop invariant proved in part (b), state a loop invariant for the for loop in lines 1-4 that will allow you to prove inequality (2.3).

Loop invariant:

**At the start of each iteration of the for loop of lines 1-4, the subarray A[1..i - 1] is in sorted order, and any element in the subarray A[1..i - 1] is not larger than any element in the subarray A[i..n]**.

**Initialization**: at the start of the iteration, i is 1, the subarray A[1..i - 1] is empty, the loop invariant is true.

**Maintenance**: if it is true before an iteration of the loop, we have the subarray A[1..i - 1] is in sorted order. After the for loop in lines 2-4, A[i] is the smallest in the subarray A[i..n]. Because the elements in the subarray A[1..i - 1] is not larget than the elements in the subarray A[i..n], we know the subarray A[1..i] is still sorted. It remains true before the next iteration.

**Termination**: it terminates when i is n. Substituting n for i in the wording of loop invariant, we have that the subarray A[1..n - 1] is in sorted order, and the elements in the subarray A[1..n - 1] is not larger than the elements in the subarray A[n..n], so the subarray A[1..n] is in sorted order. And the subarray A[1..n] is the entire array, we conclude that the entire array is sorted. Hence, the algorithm is correct.

d. What is the worst-case running time of bubblesort? How does it compare to the running time of insertion sort?

The worst-case running time of bubblesort is approximately $n + (n - 1) + \ldots + 3 = \Theta(n^2)$.

The worst-case running time of insertion sort is also $\Theta(n^2)$, but the best-case running time of insertion sort is $\Theta(n)$. For bubblesort, the best-case running time is still $\Theta(n^2)$, because a best-case input could not reduce the cost of the for loop of lines 2-4.
