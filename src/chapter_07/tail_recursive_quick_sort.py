from .quick_sort import partition


def tail_recursive_quick_sort(numbers):
    tail_recursive_quick_sort_internal(numbers, 0, len(numbers) - 1)


def tail_recursive_quick_sort_internal(numbers, p, r):
    while p < r:
        q = partition(numbers, p, r)

        tail_recursive_quick_sort_internal(numbers, p, q - 1)

        p = q + 1
