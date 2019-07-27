from ..chapter_02.insertion_sort import insertion_sort
from .quick_sort import partition


def hybrid_quick_sort(numbers, k):
    quick_sort_internal(numbers, 0, len(numbers) - 1, k)
    insertion_sort(numbers)


def quick_sort_internal(numbers, p, r, k):
    if p < r and r - p + 1 > k:
        q = partition(numbers, p, r)

        quick_sort_internal(numbers, p, q - 1, k)
        quick_sort_internal(numbers, q + 1, r, k)
