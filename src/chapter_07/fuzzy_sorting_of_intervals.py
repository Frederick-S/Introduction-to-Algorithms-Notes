from random import randint


def fuzzy_sorting_of_intervals(intervals):
    fuzzy_sorting_of_intervals_internal(intervals, 0, len(intervals) - 1)


def fuzzy_sorting_of_intervals_internal(intervals, p, r):
    if p < r:
        q, t = randomized_partition(intervals, p, r)

        fuzzy_sorting_of_intervals_internal(intervals, p, q - 1)
        fuzzy_sorting_of_intervals_internal(intervals, t + 1, r)


def randomized_partition(intervals, p, r):
    i = randint(p, r)
    intervals[i], intervals[r] = intervals[r], intervals[i]

    return partition(intervals, p, r)


def partition(intervals, p, r):
    x = intervals[r]
    i = p - 1
    t = p - 1

    for j in range(p, r):
        if before(intervals[j], x):
            t += 1
            i += 1
            intervals[t], intervals[i] = intervals[i], intervals[t]

            if t != j:
                intervals[j], intervals[i] = intervals[i], intervals[j]
        elif overlap(intervals[j], x):
            t += 1
            intervals[t], intervals[j] = intervals[j], intervals[t]

    intervals[t + 1], intervals[r] = intervals[r], intervals[t + 1]

    return i + 1, t + 1


def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


def before(a, b):
    return a[1] < b[0]
