def merge_sort(numbers):
    auxiliary = numbers[:]
    merge_sort_internal(numbers, auxiliary, 0, len(numbers) - 1)


def merge_sort_internal(numbers, auxiliary, low, high):
    if low < high:
        middle = (low + high) // 2

        merge_sort_internal(numbers, auxiliary, low, middle)
        merge_sort_internal(numbers, auxiliary, middle + 1, high)
        merge(numbers, auxiliary, low, middle, high)


def merge(numbers, auxiliary, low, middle, high):
    for k in range(low, high + 1):
        auxiliary[k] = numbers[k]

    i = low
    j = middle + 1

    for k in range(low, high + 1):
        if i > middle:
            numbers[k] = auxiliary[j]
            j += 1
        elif j > high:
            numbers[k] = auxiliary[i]
            i += 1
        elif auxiliary[i] <= auxiliary[j]:
            numbers[k] = auxiliary[i]
            i += 1
        else:
            numbers[k] = auxiliary[j]
            j += 1
