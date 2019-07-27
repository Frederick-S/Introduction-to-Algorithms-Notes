import unittest
from src.chapter_08.k_sorted_array import k_sorted_array


class TestKSortedArray(unittest.TestCase):
    def test_k_sorted_array(self):
        numbers = []
        k_sorted_array(numbers, 2)
        self.assertSequenceEqual([], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k_sorted_array(numbers, 3)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        k_sorted_array(numbers, 3)
        self.assertSequenceEqual([3, 2, 1, 6, 5, 4, 9, 8, 7], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        k_sorted_array(numbers, 2)
        self.assertSequenceEqual([31, 26, 41, 41, 59, 58], numbers)


if __name__ == '__main__':
    unittest.main()
