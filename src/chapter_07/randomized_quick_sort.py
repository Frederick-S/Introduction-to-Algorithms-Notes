from random import randint
from .quick_sort import partition


def randomized_quick_sort(numbers):
    randomized_quick_sort_internal(numbers, 0, len(numbers) - 1)


def randomized_quick_sort_internal(numbers, p, r):
    if p < r:
        q = randomized_partition(numbers, p, r)

        randomized_quick_sort_internal(numbers, p, q - 1)
        randomized_quick_sort_internal(numbers, q + 1, r)


def randomized_partition(numbers, p, r):
    i = randint(p, r)
    numbers[i], numbers[r] = numbers[r], numbers[i]

    return partition(numbers, p, r)
