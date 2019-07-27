import unittest
from src.chapter_09.minimum_and_maximum import minimum_and_maximum


class TestMinimumAndMaximum(unittest.TestCase):
    def test_minimum_and_maximum(self):
        numbers = []
        self.assertSequenceEqual([], minimum_and_maximum(numbers))

        numbers = [1]
        self.assertSequenceEqual([1, 1], minimum_and_maximum(numbers))

        numbers = [3, 2]
        self.assertSequenceEqual([2, 3], minimum_and_maximum(numbers))

        numbers = [2, 5, 3, 0, 2, 3, 0, 3]
        self.assertSequenceEqual([0, 5], minimum_and_maximum(numbers))

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertSequenceEqual([1, 9], minimum_and_maximum(numbers))


if __name__ == '__main__':
    unittest.main()
