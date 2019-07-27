import unittest
from src.chapter_04.leftmost_min_element_in_each_row_of_monge_array \
    import leftmost_min_element_in_each_row_of_monge_array


class TestLeftmostMinElementInEachRowOfMongeArray(unittest.TestCase):
    def test_leftmost_min_element_in_each_row_of_monge_array(self):
        matrix = [[1, 1], [1, 1]]
        self.assertSequenceEqual(
            [0, 0], leftmost_min_element_in_each_row_of_monge_array(matrix))

        matrix = [
            [27, 23, 22, 32], [21, 6, 5, 10],
            [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]
        self.assertSequenceEqual(
            [2, 2, 2, 3, 3],
            leftmost_min_element_in_each_row_of_monge_array(matrix))

        matrix = [
            [10, 17, 13, 28, 23], [17, 22, 16, 29, 23],
            [24, 28, 22, 34, 24], [11, 13, 6, 17, 7],
            [45, 44, 32, 37, 23], [36, 33, 19, 21, 6], [75, 66, 51, 53, 34]]
        self.assertSequenceEqual(
            [0, 2, 2, 2, 4, 4, 4],
            leftmost_min_element_in_each_row_of_monge_array(matrix))


if __name__ == '__main__':
    unittest.main()
