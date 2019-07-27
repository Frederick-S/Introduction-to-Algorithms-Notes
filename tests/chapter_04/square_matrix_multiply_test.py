import unittest
from src.chapter_04.square_matrix_multiply import square_matrix_multiply


class TestSquareMatrixMultiply(unittest.TestCase):
    def test_square_matrix_multiply(self):
        a = [[1]]
        b = [[1]]
        c = [[1]]
        self.assertSequenceEqual(c, square_matrix_multiply(a, b))

        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        c = [[19, 22], [43, 50]]
        self.assertSequenceEqual(c, square_matrix_multiply(a, b))

        a = [[1, 3], [7, 5]]
        b = [[6, 8], [4, 2]]
        c = [[18, 14], [62, 66]]
        self.assertSequenceEqual(c, square_matrix_multiply(a, b))


if __name__ == '__main__':
    unittest.main()
