import unittest
from src.chapter_08.sorting_in_place_in_linear_time \
    import sorting_in_place_in_linear_time


class TestSortingInPlaceInLinearTime(unittest.TestCase):
    def test_sorting_in_place_in_linear_time(self):
        numbers = []
        sorting_in_place_in_linear_time(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        sorting_in_place_in_linear_time(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [0, 1, 1, 0, 1, 0, 0, 1]
        sorting_in_place_in_linear_time(numbers)
        self.assertSequenceEqual([0, 0, 0, 0, 1, 1, 1, 1], numbers)


if __name__ == '__main__':
    unittest.main()
