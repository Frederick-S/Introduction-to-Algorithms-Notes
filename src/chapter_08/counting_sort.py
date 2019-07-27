def counting_sort(numbers):
    length = len(numbers)

    if length == 0:
        return numbers

    k = max(numbers)
    c = [0] * (k + 1)
    b = [0] * length

    for i in range(length):
        c[numbers[i]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    for i in range(length - 1, -1, -1):
        b[c[numbers[i]] - 1] = numbers[i]
        c[numbers[i]] -= 1

    return b
