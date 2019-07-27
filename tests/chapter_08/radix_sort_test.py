import unittest
from src.chapter_08.radix_sort import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        numbers = []
        radix_sort(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        radix_sort(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [31, 41, 59, 26, 41, 58, 100]
        radix_sort(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59, 100], numbers)

        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        radix_sort(numbers)
        self.assertSequenceEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        radix_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)


if __name__ == '__main__':
    unittest.main()
