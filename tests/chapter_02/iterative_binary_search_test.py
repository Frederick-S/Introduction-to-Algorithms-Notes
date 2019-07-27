import unittest
from src.chapter_02.iterative_binary_search import iterative_binary_search


class TestIterativeBinarySearch(unittest.TestCase):
    def test_iterative_binary_search(self):
        numbers = []
        self.assertEqual(False, iterative_binary_search(numbers, 1))

        numbers = [2]
        self.assertEqual(False, iterative_binary_search(numbers, 1))

        numbers = [1, 2, 3, 4]
        self.assertEqual(True, iterative_binary_search(numbers, 1))
        self.assertEqual(True, iterative_binary_search(numbers, 4))
        self.assertEqual(False, iterative_binary_search(numbers, 5))


if __name__ == '__main__':
    unittest.main()
