def k_sorted_array(numbers, k):
    length = len(numbers)

    if k >= length:
        return

    for i in range(k):
        p = i
        r = i + k * ((length - 1 - i) // k)

        quick_sort(numbers, p, r, k)


def quick_sort(numbers, p, r, step):
    if p < r:
        q = partition(numbers, p, r, step)

        quick_sort(numbers, p, q - step, step)
        quick_sort(numbers, q + step, r, step)


def partition(numbers, p, r, step):
    x = numbers[r]
    i = p - step

    for j in range(p, r, step):
        if numbers[j] <= x:
            i += step
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[i + step], numbers[r] = numbers[r], numbers[i + step]

    return i + step
