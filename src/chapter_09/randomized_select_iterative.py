from ..chapter_07.randomized_quick_sort import randomized_partition


def randomized_select_iterative(numbers, i):
    assert i <= len(numbers)

    return randomized_select_iterative_internal(
        numbers, 0, len(numbers) - 1, i)


def randomized_select_iterative_internal(numbers, p, r, i):
    while p <= r:
        if p == r:
            return numbers[p]

        q = randomized_partition(numbers, p, r)
        k = q - p + 1

        if i == k:
            return numbers[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i -= k
