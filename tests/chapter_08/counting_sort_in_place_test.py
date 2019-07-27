import unittest
from src.chapter_08.counting_sort_in_place import counting_sort_in_place


class TestCountingSortInPlace(unittest.TestCase):
    def test_counting_sort_in_place(self):
        numbers = []
        counting_sort_in_place(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        counting_sort_in_place(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [2, 5, 3, 0, 2, 3, 0, 3]
        counting_sort_in_place(numbers)
        self.assertSequenceEqual([0, 0, 2, 2, 3, 3, 3, 5], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        counting_sort_in_place(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counting_sort_in_place(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        counting_sort_in_place(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)


if __name__ == '__main__':
    unittest.main()
