def number_of_inversions(numbers):
    auxiliary = numbers[:]
    inversions = merge_sort(numbers, auxiliary, 0, len(numbers) - 1)

    return inversions


def merge_sort(numbers, auxiliary, low, high):
    inversions = 0

    if low < high:
        middle = (low + high) // 2

        inversions += merge_sort(numbers, auxiliary, low, middle)
        inversions += merge_sort(numbers, auxiliary, middle + 1, high)
        inversions += merge(numbers, auxiliary, low, middle, high)

    return inversions


def merge(numbers, auxiliary, low, middle, high):
    for k in range(low, high + 1):
        auxiliary[k] = numbers[k]

    i = low
    j = middle + 1
    inversions = 0

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
            inversions += middle + 1 - i

    return inversions
