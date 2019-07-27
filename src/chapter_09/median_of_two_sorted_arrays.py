def median_of_two_sorted_arrays(x, y):
    return median_of_two_sorted_arrays_internal(
        x, 0, len(x) - 1, y, 0, len(y) - 1)


def median_of_two_sorted_arrays_internal(x, px, rx, y, py, ry):
    if rx - px == 1:
        if x[px] <= y[py]:
            return min(x[rx], y[py])
        else:
            return min(x[px], y[ry])

    median_index_of_x = (px + rx) // 2
    median_index_of_y = (py + ry) // 2

    if x[median_index_of_x] < y[median_index_of_y]:
        return median_of_two_sorted_arrays_internal(
            x, median_index_of_x, rx, y, py, median_index_of_y)
    elif x[median_index_of_x] > y[median_index_of_y]:
        return median_of_two_sorted_arrays_internal(
            x, px, median_index_of_x, y, median_index_of_y, ry)
    else:
        return x[median_index_of_x]
