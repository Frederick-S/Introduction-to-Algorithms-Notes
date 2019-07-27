def square_matrix_multiply(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            value = 0

            for k in range(n):
                value += a[i][k] * b[k][j]

            c[i][j] = value

    return c
