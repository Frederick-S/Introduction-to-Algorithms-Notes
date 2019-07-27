from .radix_sort import get_number_length
from . radix_sort import radix_sort


def sorting_variable_length_integers(numbers):
    length = len(numbers)

    if length == 0:
        return numbers

    max_digit = get_number_length(max(numbers))
    numbers_by_digits = [[] for i in range(max_digit)]

    for i in range(length):
        digit = get_number_length(numbers[i])
        numbers_by_digits[digit - 1].append(numbers[i])

    for i in range(max_digit):
        radix_sort(numbers_by_digits[i])

    result = []

    for i in range(max_digit):
        result += numbers_by_digits[i]

    return result
