def hoare_partition_quick_sort(numbers):
    hoare_partition_quick_sort_internal(numbers, 0, len(numbers) - 1)


def hoare_partition_quick_sort_internal(numbers, p, r):
    if p < r:
        q = hoare_partition(numbers, p, r)

        hoare_partition_quick_sort_internal(numbers, p, q)
        hoare_partition_quick_sort_internal(numbers, q + 1, r)


def hoare_partition(numbers, p, r):
    x = numbers[p]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1

            if numbers[j] <= x:
                break

        while True:
            i += 1

            if numbers[i] >= x:
                break

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            return j
