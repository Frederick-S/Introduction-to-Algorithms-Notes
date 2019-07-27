import unittest
from src.chapter_08.sorting_variable_length_integers \
    import sorting_variable_length_integers


class TestSortingVariableLengthIntegers(unittest.TestCase):
    def test_sorting_variable_length_integers(self):
        numbers = []
        self.assertSequenceEqual([], sorting_variable_length_integers(numbers))

        numbers = [1]
        self.assertSequenceEqual(
            [1], sorting_variable_length_integers(numbers))

        numbers = [1, 10, 20, 30, 40, 50, 60, 70]
        self.assertSequenceEqual(
            [1, 10, 20, 30, 40, 50, 60, 70],
            sorting_variable_length_integers(numbers))

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorting_variable_length_integers(numbers))

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorting_variable_length_integers(numbers))

        numbers = [365, 781, 992, 12, 120, 2, 12345]
        self.assertSequenceEqual(
            [2, 12, 120, 365, 781, 992, 12345],
            sorting_variable_length_integers(numbers))


if __name__ == '__main__':
    unittest.main()
