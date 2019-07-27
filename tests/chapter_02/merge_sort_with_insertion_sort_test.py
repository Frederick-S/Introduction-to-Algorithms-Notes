import unittest
from src.chapter_02.merge_sort_with_insertion_sort import (
    merge_sort_with_insertion_sort
)


class TestMergeSortWithInsertionSort(unittest.TestCase):
    def test_merge_sort_with_insertion_sort(self):
        numbers = []
        merge_sort_with_insertion_sort(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        merge_sort_with_insertion_sort(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        merge_sort_with_insertion_sort(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        merge_sort_with_insertion_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        merge_sort_with_insertion_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)


if __name__ == '__main__':
    unittest.main()
