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

## 2-3 Correctness of Horner's rule
a. In terms of $\Theta$-notation, what is the running time of this code fragment for Horner's rule?

It's $\Theta(n)$.

b. Write pseudocode to implement the naive polynomial-evaluation algorithm that computes each term of the polynomial from scratch. What is the running time of this algorithm? How does it compare to Horner's rule?

The pseudocode of the naive polynomial-evaluation algorithm:

```
POLYNOMIAL-EVALUATION(A, x)

y = 0

for i = 0 to n
    a = A[i]
    x_product = 1

    for j = 1 to i
        x_product = x_product * x

    y = y + a * x_product
```

The running time of this algorithm is $\Theta(n^2)$. It's slower than the Horner's rule.

c. Use the loop invariant to show that, at termination, $y = \sum_{k = 0}^{n} a_k{x^k}$.

**Initialization**: at the start of the iteration of the for loop, i is n, and $y = \sum_{k = 0}^{-1} a_{k + n + 1}{x^k}$, this is not a valid summation, so y is still 0. Thus the loop invariant is correct.

**Maintenance**: at the start of the ith iteration, we have:
$$y = \sum_{k = 0}^{n - (i + 1)} a_{k + i + 1}{x^k}$$

And after the ith iteration, we have:

$$
\begin{eqnarray}
y &=& a_i + xy = a_i + x\sum_{k = 0}^{n - (i + 1)} a_{k + i + 1}{x^k} \\\\\\
&=& a_i + x(a_{i + 1}x^0 + a_{i + 2}x^1 + \ldots + a_nx^{n - i - 1}) \\\\\\
&=& a_i + a_{i + 1}x^1 + a_{i + 2}x^2 + \ldots + a_nx^{n - i} \\\\\\
&=& a_ix^0 + a_{i + 1}x^1 + a_{i + 2}x^2 + \ldots + a_nx^{n - i} \\\\\\
&=& \sum_{k = 0}^{n - i} a_{k + i}{x^k} \\\\\\
&=& \sum_{k = 0}^{n - ((i - 1) + 1)} a_{k + (i - 1) + 1}{x^k}
\end{eqnarray}
$$

So the loop invariant is still true after the end of ith iteration.

**Termination**: when the for loop terminates, i is -1, and we replace i with -1 in the summation:

$$y = \sum_{k = 0}^{n - (-1 + 1)} a_{k + -1 + 1}{x^k} = \sum_{k = 0}^{n} a_{k}{x^k}$$

So the loop invariant is correct.

d. Conclude by arguing that the given code fragment correctly evaluates a polynomial characterized by the coefficients $a_0, a_1, \ldots, a_n$.

At the end of the iteration of the for loop of lines 2-3, we have $y = \sum_{k = 0}^{n} a_{k}{x^k}$, so it's correct.

## 2-4 Inversions
a. List the five inversions of the array $\langle 2, 3, 8, 6, 1\rangle$.

$\langle 0, 4\rangle, \langle 1, 4\rangle, \langle 2, 3\rangle, \langle 2, 4\rangle, \langle 6, 1\rangle$.

b. What array with elements from the set $\lbrace 1, 2, \ldots, n \rbrace$ has the most inversions? How many does it have?

The array $\lbrace n, \ldots, 2, 1\rbrace$ has the most inversions. It has:

$$(n - 1) + (n - 2) + \ldots + 1 = \frac{n(n - 1)}{2}$$

c. What is the relationship between the running time of insertion sort and the number of inversions in the input array?

Let's go back to the pseudocode of insertion sort. We know the running time of insertion sort is:

$$T(n) = c_1n + c_2(n - 1) + c_4(n - 1) + c_5\sum_{j = 2}^{n} t_j + c_6\sum_{j = 2}^{n} (t_j - 1) + c_7\sum_{j = 2}^{n} (t_j - 1) + c_8(n - 1)$$

where $t_j$ is the number of times the while loop test in line 5 is executed for the jth outer for loop.

We can see lines 6 and 7 will be executed when there is an inversion, let's denote $p_j$ the number of inversions in the subarray A[1..j]. So we have $p_j = t_j - 1$. When j is increasing, the number of inversions in the whole array A[1..n] is decreasing, but it doesn't create new inversions in eath iteration, since the relative order in subarray A[1..j] and A[j + 1..n] are not changed. So if we denote $m$ the number of inversions in the whole array A, we have $\sum_{j = 2}^{n} p_j = \sum_{j = 2}^{n} (t_j - 1) = m$. So:

$$T(n) = c_1n + c_2(n - 1) + c_4(n - 1) + c_5(m + n - 1) + c_6m + c_7m + c_8(n - 1)$$

d. Give an algorithm that determines the number of inversions in any permutation on n elements in $\Theta(n\lg{n})$ worst-case time.

```
NUMBER-OF-INVERSIONS(A)
	n = A.length
	
	return MERGE-SORT(A, 1, n)

MERGE-SORT(A, p, r)
	inversions = 0
	
	if p < r
		q = [(p + q) / 2]
		
		inversions += MERGE-SORT(A, p, q)
		inversions += MERGE-SORT(A, q + 1, r)
		inversions += MERGE(A, p, q, r)
	
	return inversions

MERGE(A, p, q, r)

n1 = q - p + 1
n2 = r - q
let L[1..n1] and R[1..n2] be new arrays
for i = 1 to n1
    L[i] = A[p + i - 1]
for j = 1 to n2
    R[j] = A[q + j]
i = 1
j = 1
inversions = 0
for k = p to r
    if i > n1:
        A[k] = R[j]
        j = j + 1
    else if j > n2:
        A[k] = L[i]
        i = i + 1
    else if L[i] <= R[j]:
        A[k] = L[i]
        i = i + 1
    else
        A[k] = R[j]
        j = j + 1
        inversions += n1 - i + 1
```