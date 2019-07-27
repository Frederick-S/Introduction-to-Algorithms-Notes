def find_maximum_subarray_linear_time(numbers, low, high):
    if len(numbers) == 0:
        return -1, -1, -float('inf')

    start = -1
    max_sum_start = -1
    max_sum_end = -1
    max_sum_so_far = -float('inf')
    max_sum_ending_here = -float('inf')

    for i in range(low, high + 1):
        if numbers[i] > max_sum_ending_here + numbers[i]:
            max_sum_ending_here = numbers[i]
            start = i
        else:
            max_sum_ending_here += numbers[i]

        if max_sum_ending_here > max_sum_so_far:
            max_sum_so_far = max_sum_ending_here
            max_sum_start = start
            max_sum_end = i

    return max_sum_start, max_sum_end, max_sum_so_far
