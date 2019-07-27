import math


def weighted_median_linear_time(elements):
    length = len(elements)

    if length == 1:
        return elements[0]
    elif length == 2:
        if elements[0].get('weight') >= elements[1].get('weight'):
            return elements[0]
        else:
            return elements[1]
    else:
        median = select(elements, math.ceil(length / 2))

        left_weights = 0
        right_weights = 0

        for i in range(math.ceil(length / 2) - 1):
            left_weights += elements[i].get('weight')

        for i in range(math.ceil(length / 2), length):
            right_weights += elements[i].get('weight')

        if left_weights < 0.5 and right_weights <= 0.5:
            return median
        elif left_weights >= 0.5:
            median['weight'] += right_weights

            return weighted_median_linear_time(
                elements[:math.ceil(length / 2)])
        elif right_weights > 0.5:
            median['weight'] += left_weights

            return weighted_median_linear_time(
                elements[math.ceil(length / 2) - 1:])


k = 5


def select(elements, i):
    assert i <= len(elements)

    _, value = select_internal(elements, 0, len(elements) - 1, i)

    return value


def select_internal(elements, p, r, i):
    if p == r:
        return p, elements[p]

    median = find_median_recursively(elements, p, r)
    q = partition(elements, p, r, median)
    k = q - p + 1

    if i == k:
        return q, elements[q]
    elif i < k:
        return select_internal(elements, p, q - 1, i)
    else:
        return select_internal(elements, q + 1, r, i - k)


def partition(elements, p, r, pivot):
    i = p
    t = p
    j = r

    while i < j:
        while elements[i].get('value') < pivot.get('value'):
            i += 1
            t += 1

        while t <= r and elements[t].get('value') == pivot.get('value'):
            t += 1

        while elements[j].get('value') > pivot.get('value'):
            j -= 1

        if t > r:
            break

        if i < j:
            elements[i], elements[t] = elements[t], elements[i]

            if t != j:
                elements[i], elements[j] = elements[j], elements[i]

    return i


def find_median_recursively(elements, p, r):
    medians = []

    for i in range(p, r + 1, k):
        if i + k - 1 <= r:
            insertion_sort(elements, i, i + k - 1)

            medians.append(elements[i + get_median_index(k)])
        else:
            insertion_sort(elements, i, r)

            medians.append(elements[i + get_median_index(r - i + 1)])

    if len(medians) == 1:
        return medians[0]
    else:
        return find_median_recursively(medians, 0, len(medians) - 1)


def get_median_index(length):
    if length % 2 == 1:
        return length // 2
    else:
        return length // 2 - 1


def insertion_sort(elements, start, end):
    for i in range(start + 1, end + 1):
        j = i - 1
        key = elements[i]

        while j >= 0 and elements[j].get('value') > key.get('value'):
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = key
