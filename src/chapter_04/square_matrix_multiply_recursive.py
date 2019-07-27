def square_matrix_multiply_recursive(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]

    if n == 1:
        c[0][0] = a[0][0] * b[0][0]
    else:
        half = n // 2

        a11 = [[0] * half for _ in range(half)]
        a12 = [[0] * half for _ in range(half)]
        a21 = [[0] * half for _ in range(half)]
        a22 = [[0] * half for _ in range(half)]
        b11 = [[0] * half for _ in range(half)]
        b12 = [[0] * half for _ in range(half)]
        b21 = [[0] * half for _ in range(half)]
        b22 = [[0] * half for _ in range(half)]

        for i in range(half):
            for j in range(half):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + half]
                a21[i][j] = a[i + half][j]
                a22[i][j] = a[i + half][j + half]
                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + half]
                b21[i][j] = b[i + half][j]
                b22[i][j] = b[i + half][j + half]

        c11 = add(
            square_matrix_multiply_recursive(a11, b11),
            square_matrix_multiply_recursive(a12, b21))
        c12 = add(
            square_matrix_multiply_recursive(a11, b12),
            square_matrix_multiply_recursive(a12, b22))
        c21 = add(
            square_matrix_multiply_recursive(a21, b11),
            square_matrix_multiply_recursive(a22, b21))
        c22 = add(
            square_matrix_multiply_recursive(a21, b12),
            square_matrix_multiply_recursive(a22, b22))

        for i in range(half):
            for j in range(half):
                c[i][j] = c11[i][j]
                c[i][j + half] = c12[i][j]
                c[i + half][j] = c21[i][j]
                c[i + half][j + half] = c22[i][j]

    return c


def add(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    return c
