import unittest
from src.chapter_08.counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test_counting_sort(self):
        numbers = []
        self.assertSequenceEqual([], counting_sort(numbers))

        numbers = [1]
        self.assertSequenceEqual([1], counting_sort(numbers))

        numbers = [2, 5, 3, 0, 2, 3, 0, 3]
        self.assertSequenceEqual(
            [0, 0, 2, 2, 3, 3, 3, 5], counting_sort(numbers))

        numbers = [31, 41, 59, 26, 41, 58]
        self.assertSequenceEqual(
            [26, 31, 41, 41, 58, 59], counting_sort(numbers))

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], counting_sort(numbers))

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], counting_sort(numbers))


if __name__ == '__main__':
    unittest.main()
