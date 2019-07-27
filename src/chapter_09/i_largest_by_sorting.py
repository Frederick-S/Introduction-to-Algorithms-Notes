from ..chapter_02.merge_sort import merge_sort


def i_largest_by_sorting(numbers, i):
    merge_sort(numbers)

    return numbers[len(numbers) - i:]
