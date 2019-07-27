import unittest
from src.chapter_07.stack_optimized_tail_recursive_quick_sort import \
    stack_optimized_tail_recursive_quick_sort


class TestStackOptimizedTailRecursiveQuickSort(unittest.TestCase):
    def test_stack_optimized_tail_recursive_quick_sort(self):
        numbers = []
        stack_optimized_tail_recursive_quick_sort(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        stack_optimized_tail_recursive_quick_sort(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        stack_optimized_tail_recursive_quick_sort(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        stack_optimized_tail_recursive_quick_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        stack_optimized_tail_recursive_quick_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)


if __name__ == '__main__':
    unittest.main()
