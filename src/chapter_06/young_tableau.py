import sys


def young_tableau_extract_min(matrix):
    smallest = matrix[0][0]
    matrix[0][0] = sys.maxsize

    youngify(matrix, 0, 0)

    return smallest


def youngify(matrix, row, column):
    smallest_row = row
    smallest_column = column
    max_row = len(matrix)
    max_column = len(matrix[0])

    if row + 1 < max_row and matrix[row + 1][column] < matrix[row][column]:
        smallest_row = row + 1

    if (column + 1 < max_column and
            matrix[row][column + 1] < matrix[smallest_row][smallest_column]):
        smallest_row = row
        smallest_column = column + 1

    if smallest_row != row or smallest_column != column:
        matrix[row][column], matrix[smallest_row][smallest_column] = \
            matrix[smallest_row][smallest_column], matrix[row][column]

        youngify(matrix, smallest_row, smallest_column)


def young_tableau_insert(matrix, value):
    max_row = len(matrix)
    max_column = len(matrix[0])
    matrix[max_row - 1][max_column - 1] = value

    def youngify_insert(matrix, row, column):
        largest_row = row
        largest_column = column

        if row - 1 >= 0 and matrix[row - 1][column] > matrix[row][column]:
            largest_row = row - 1

        if (column - 1 >= 0 and
                matrix[row][column - 1] > matrix[largest_row][largest_column]):
            largest_row = row
            largest_column = column - 1

        if largest_row != row or largest_column != column:
            matrix[row][column], matrix[largest_row][largest_column] = \
                matrix[largest_row][largest_column], matrix[row][column]

            youngify_insert(matrix, largest_row, largest_column)

    youngify_insert(matrix, max_row - 1, max_row - 1)


def young_tableau_find(matrix, value):
    max_row = len(matrix)
    max_column = len(matrix[0])
    row = max_row - 1
    column = 0

    while row >= 0 and column <= max_column - 1:
        current = matrix[row][column]

        if current == value:
            return True
        elif current > value:
            row -= 1
        elif current < value:
            column += 1

    return False
