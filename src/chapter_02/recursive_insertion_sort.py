def recursive_insertion_sort(numbers):
    recursive_insertion_sort_internal(numbers, len(numbers) - 1)


def recursive_insertion_sort_internal(numbers, end):
    if end > 0:
        recursive_insertion_sort_internal(numbers, end - 1)
        insert(numbers, end)


def insert(numbers, end):
    key = numbers[end]
    i = end - 1

    while i >= 0 and numbers[i] > key:
        numbers[i + 1] = numbers[i]
        i -= 1

    numbers[i + 1] = key
