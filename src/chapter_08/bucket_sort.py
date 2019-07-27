import math
from ..chapter_02.insertion_sort import insertion_sort


def bucket_sort(numbers):
    length = len(numbers)
    result = []
    b = [[] for _ in range(length)]

    for i in range(length):
        j = math.floor(length * numbers[i])
        b[j].append(numbers[i])

    for i in range(length):
        insertion_sort(b[i])

    for i in range(length):
        result += b[i]

    return result
