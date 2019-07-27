def leftmost_min_element_in_each_row_of_monge_array(matrix):
    # Column index of leftmost min element in each row
    leftmost_min_element_in_each_row = [0] * len(matrix)

    leftmost_min_element_divide_and_conquer(
        matrix, leftmost_min_element_in_each_row, 0, len(matrix) - 1, 1)

    return leftmost_min_element_in_each_row


def leftmost_min_element_divide_and_conquer(
        matrix, leftmost_min_element_in_each_row, row_start, row_end, step):
    if row_start == row_end:
        leftmost_min_element_in_each_row[row_start] = \
            find_leftmost_min_element_in_row(
                matrix, row_start, 0, len(matrix[row_start]) - 1)
    else:
        # Construct a submatrix consisting of the even-numbered rows
        sub_matrix_row_start = row_start + step
        sub_matrix_row_end = 0

        if row_end % 2 == 0 or ((row_end - row_start) // step) % 2 == 0:
            sub_matrix_row_end = row_end - step
        elif ((row_end - row_start) // step) % 2 == 1:
            sub_matrix_row_end = row_end

        leftmost_min_element_divide_and_conquer(
            matrix, leftmost_min_element_in_each_row,
            sub_matrix_row_start, sub_matrix_row_end, step * 2)

        leftmost_min_element_in_odd_numbered_rows(
            matrix, leftmost_min_element_in_each_row, row_start, row_end, step)


def find_leftmost_min_element_in_row(matrix, row, column_start, column_end):
    min_column_index = 0

    for column in range(column_start, column_end + 1):
        if matrix[row][column] < matrix[row][min_column_index]:
            min_column_index = column

    return min_column_index


def leftmost_min_element_in_odd_numbered_rows(
        matrix, leftmost_min_element_in_each_row, row_start, row_end, step):
    for odd_numbered_row in range(row_start, row_end + 1, step * 2):
        prev_even_numbered_row = odd_numbered_row - step
        next_even_numbered_row = odd_numbered_row + step
        column_start = -1
        column_end = -1

        if prev_even_numbered_row >= row_start and \
                next_even_numbered_row <= row_end:
            column_start = \
                leftmost_min_element_in_each_row[prev_even_numbered_row]
            column_end = \
                leftmost_min_element_in_each_row[next_even_numbered_row]
        elif prev_even_numbered_row >= row_start:
            column_start = \
                leftmost_min_element_in_each_row[prev_even_numbered_row]
            column_end = len(matrix[0]) - 1
        elif next_even_numbered_row <= row_end:
            column_start = 0
            column_end = \
                leftmost_min_element_in_each_row[next_even_numbered_row]

        leftmost_min_element_in_each_row[odd_numbered_row] = \
            find_leftmost_min_element_in_row(
                matrix, odd_numbered_row, column_start, column_end)
