import unittest
from src.chapter_09.randomized_select import randomized_select


class TestRandomizedSelect(unittest.TestCase):
    def test_randomized_select(self):
        numbers = [1]
        self.assertEqual(1, randomized_select(numbers, 1))

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(5, randomized_select(numbers, 5))

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(5, randomized_select(numbers, 5))


if __name__ == '__main__':
    unittest.main()
