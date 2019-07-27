def square_matrix_multiply_strassen_algorithm(a, b):
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

        s1 = subtract(b12, b22)
        s2 = add(a11, a12)
        s3 = add(a21, a22)
        s4 = subtract(b21, b11)
        s5 = add(a11, a22)
        s6 = add(b11, b22)
        s7 = subtract(a12, a22)
        s8 = add(b21, b22)
        s9 = subtract(a11, a21)
        s10 = add(b11, b12)

        p1 = square_matrix_multiply_strassen_algorithm(a11, s1)
        p2 = square_matrix_multiply_strassen_algorithm(s2, b22)
        p3 = square_matrix_multiply_strassen_algorithm(s3, b11)
        p4 = square_matrix_multiply_strassen_algorithm(a22, s4)
        p5 = square_matrix_multiply_strassen_algorithm(s5, s6)
        p6 = square_matrix_multiply_strassen_algorithm(s7, s8)
        p7 = square_matrix_multiply_strassen_algorithm(s9, s10)

        c11 = add(subtract(add(p5, p4), p2), p6)
        c12 = add(p1, p2)
        c21 = add(p3, p4)
        c22 = subtract(subtract(add(p5, p1), p3), p7)

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


def subtract(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]

    return c
