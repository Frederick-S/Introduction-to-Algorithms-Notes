import unittest
from src.chapter_07.randomized_quick_sort import randomized_quick_sort


class TestRandomizedQuickSort(unittest.TestCase):
    def test_randomized_quick_sort(self):
        numbers = []
        randomized_quick_sort(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        randomized_quick_sort(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        randomized_quick_sort(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        randomized_quick_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        randomized_quick_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)


if __name__ == '__main__':
    unittest.main()
