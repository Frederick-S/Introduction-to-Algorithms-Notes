def merge_sort_with_insertion_sort(numbers):
    cutoff = 3
    auxiliary = numbers[:]
    merge_sort(numbers, auxiliary, 0, len(numbers) - 1, cutoff)


def merge_sort(numbers, auxiliary, low, high, cutoff):
    if low < high:
        if low + cutoff >= high:
            insertion_sort(numbers, low, high)

            return

        middle = (low + high) // 2

        merge_sort(numbers, auxiliary, low, middle, cutoff)
        merge_sort(numbers, auxiliary, middle + 1, high, cutoff)
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


def insertion_sort(numbers, low, high):
    for i in range(low, high + 1):
        j = i - 1
        key = numbers[i]

        while j >= low and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key
