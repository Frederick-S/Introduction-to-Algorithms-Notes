# Problems
## 9-1
### a
Sorting requires $O(n\lg{n})$, plus $O(i)$ to list the i numbers, the total running time is $O(n\lg{n}) + O(i)$.

### b
It requires $O(n)$ to build a max-priority queue, the `EXTRACT-MAX` costs $O(\lg{n})$, thus the total running time is $O(n) + iO(\lg{n})$.

### c
First we need to find the `n - i + 1` smallest element, this requires O(n). And the array is partitioned around the `n - i + 1` smallest element. So we need to sort the `i - 1` numbers, it costs $O((i - 1)\lg{(i - 1)})$, so the total running time is $O(n) + O((i - 1)\lg{(i - 1)})$.

## 9-2
