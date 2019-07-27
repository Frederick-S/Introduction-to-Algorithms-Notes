def quick_sort(numbers):
    quick_sort_internal(numbers, 0, len(numbers) - 1)


def quick_sort_internal(numbers, p, r):
    if p < r:
        q = partition(numbers, p, r)

        quick_sort_internal(numbers, p, q - 1)
        quick_sort_internal(numbers, q + 1, r)


def partition(numbers, p, r):
    x = numbers[r]
    i = p - 1

    for j in range(p, r):
        if numbers[j] <= x:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + 1], numbers[r] = numbers[r], numbers[i + 1]

    return i + 1
