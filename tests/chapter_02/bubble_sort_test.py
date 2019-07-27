import unittest
from src.chapter_02.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        numbers = []
        bubble_sort(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        bubble_sort(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        bubble_sort(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bubble_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)


if __name__ == '__main__':
    unittest.main()
