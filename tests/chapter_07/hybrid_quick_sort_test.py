import unittest
from random import randint
from src.chapter_07.hybrid_quick_sort import hybrid_quick_sort


class TestHybridQuickSort(unittest.TestCase):
    def test_hybrid_quick_sort(self):
        numbers = [randint(1, 1000) for i in range(1000)]
        numbers_sorted = numbers[:]
        numbers_sorted.sort()

        hybrid_quick_sort(numbers, 50)
        self.assertSequenceEqual(numbers_sorted, numbers)


if __name__ == '__main__':
    unittest.main()
