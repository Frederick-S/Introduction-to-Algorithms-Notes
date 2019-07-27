import unittest
from src.chapter_04.find_maximum_subarray_divide_and_conquer \
    import find_maximum_subarray_divide_and_conquer


class TestMaximumSubarrayDivideAndConquer(unittest.TestCase):
    def test_maximum_subarray_divide_and_conquer(self):
        numbers = []
        self.assertSequenceEqual(
            (-1, -1, -float('inf')),
            find_maximum_subarray_divide_and_conquer(
                numbers, 0, len(numbers) - 1))

        numbers = [1, 2, 3, 4, 5]
        self.assertSequenceEqual(
            (0, 4, 15),
            find_maximum_subarray_divide_and_conquer(
                numbers, 0, len(numbers) - 1))

        numbers = [-1, -2, -3, -4, -5]
        self.assertSequenceEqual(
            (0, 0, -1),
            find_maximum_subarray_divide_and_conquer(
                numbers, 0, len(numbers) - 1))

        numbers = [-5, -4, -3, -2, -1]
        self.assertSequenceEqual(
            (4, 4, -1),
            find_maximum_subarray_divide_and_conquer(
                numbers, 0, len(numbers) - 1))

        numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertSequenceEqual(
            (3, 6, 6),
            find_maximum_subarray_divide_and_conquer(
                numbers, 0, len(numbers) - 1))


if __name__ == '__main__':
    unittest.main()
