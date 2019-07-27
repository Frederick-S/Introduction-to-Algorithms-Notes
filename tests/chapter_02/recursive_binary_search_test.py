import unittest
from src.chapter_02.recursive_binary_search import recursive_binary_search


class TestRecursiveBinarySearch(unittest.TestCase):
    def test_recursive_binary_search(self):
        numbers = []
        self.assertEqual(False, recursive_binary_search(numbers, 1))

        numbers = [2]
        self.assertEqual(False, recursive_binary_search(numbers, 1))

        numbers = [1, 2, 3, 4]
        self.assertEqual(True, recursive_binary_search(numbers, 1))
        self.assertEqual(True, recursive_binary_search(numbers, 4))
        self.assertEqual(False, recursive_binary_search(numbers, 5))


if __name__ == '__main__':
    unittest.main()
