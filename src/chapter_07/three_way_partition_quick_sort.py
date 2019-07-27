def three_way_partition_quick_sort(numbers):
    three_way_partition_quick_sort_internal(numbers, 0, len(numbers) - 1)


def three_way_partition_quick_sort_internal(numbers, p, r):
    if p < r:
        q, t = three_way_partition(numbers, p, r)

        three_way_partition_quick_sort_internal(numbers, p, q - 1)
        three_way_partition_quick_sort_internal(numbers, t + 1, r)


def three_way_partition(numbers, p, r):
    x = numbers[r]
    i = p - 1
    t = p - 1

    for j in range(p, r):
        if numbers[j] < x:
            t += 1
            i += 1
            numbers[t], numbers[i] = numbers[i], numbers[t]

            if t != j:
                numbers[j], numbers[i] = numbers[i], numbers[j]
        elif numbers[j] == x:
            t += 1
            numbers[t], numbers[j] = numbers[j], numbers[t]

    numbers[t + 1], numbers[r] = numbers[r], numbers[t + 1]

    return i + 1, t + 1
