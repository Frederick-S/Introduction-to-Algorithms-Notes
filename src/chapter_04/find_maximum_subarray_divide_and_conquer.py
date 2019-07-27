def find_maximum_subarray_divide_and_conquer(numbers, low, high):
    if len(numbers) == 0:
        return -1, -1, -float('inf')
    elif low == high:
        return low, high, numbers[low]
    else:
        middle = (low + high) // 2

        left_maximum_subarray = find_maximum_subarray_divide_and_conquer(
            numbers, low, middle)
        right_maximum_subarray = find_maximum_subarray_divide_and_conquer(
            numbers, middle + 1, high)
        cross_maximum_subarray = find_max_crossing_subarray(
            numbers, low, middle, high)

        if (left_maximum_subarray[2] >= right_maximum_subarray[2] and
                left_maximum_subarray[2] >= cross_maximum_subarray[2]):
            return left_maximum_subarray
        elif (right_maximum_subarray[2] >= left_maximum_subarray[2] and
                right_maximum_subarray[2] >= cross_maximum_subarray[2]):
            return right_maximum_subarray
        else:
            return cross_maximum_subarray


def find_max_crossing_subarray(numbers, low, middle, high):
    start = middle
    end = middle
    current_sum = 0
    left_sum = -float('inf')
    right_sum = -float('inf')

    for i in range(middle, low - 1, -1):
        current_sum += numbers[i]

        if current_sum > left_sum:
            left_sum = current_sum
            start = i

    current_sum = 0

    for i in range(middle + 1, high + 1):
        current_sum += numbers[i]

        if current_sum > right_sum:
            right_sum = current_sum
            end = i

    return start, end, left_sum + right_sum
