import unittest
from src.chapter_04.square_matrix_multiply_strassen_algorithm \
    import square_matrix_multiply_strassen_algorithm


class TestSquareMatrixMultiplyStrassenAlgorithm(unittest.TestCase):
    def test_square_matrix_multiply_strassen_algorithm(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        c = [[19, 22], [43, 50]]
        self.assertSequenceEqual(
            c, square_matrix_multiply_strassen_algorithm(a, b))

        a = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        b = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        c = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.assertSequenceEqual(
            c, square_matrix_multiply_strassen_algorithm(a, b))


if __name__ == '__main__':
    unittest.main()
