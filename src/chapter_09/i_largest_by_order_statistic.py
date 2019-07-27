from .select import select
from ..chapter_02.merge_sort import merge_sort_internal


def i_largest_by_order_statistic(numbers, i):
    result = []
    length = len(numbers)

    result.append(select(numbers, length - i + 1))

    merge_sort_internal(numbers, numbers[:], length - i + 1, length - 1)

    for j in range(length - i + 1, length):
        result.append(numbers[j])

    return result
