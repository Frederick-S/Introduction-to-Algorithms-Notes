from .quick_sort import partition


def stack_optimized_tail_recursive_quick_sort(numbers):
    stack_optimized_tail_recursive_quick_sort_internal(
        numbers, 0, len(numbers) - 1)


def stack_optimized_tail_recursive_quick_sort_internal(numbers, p, r):
    while p < r:
        q = partition(numbers, p, r)

        if q - p > r - q:
            stack_optimized_tail_recursive_quick_sort_internal(
                numbers, q + 1, r)

            r = q - 1
        else:
            stack_optimized_tail_recursive_quick_sort_internal(
                numbers, p, q - 1)

            p = q + 1
