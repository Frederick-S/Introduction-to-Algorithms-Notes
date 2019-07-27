import unittest
from src.chapter_07.three_way_partition_quick_sort import \
    three_way_partition_quick_sort


class TestThreeWayPartitionQuickSort(unittest.TestCase):
    def test_three_way_partition_quick_sort(self):
        numbers = []
        three_way_partition_quick_sort(numbers)
        self.assertSequenceEqual([], numbers)

        numbers = [1]
        three_way_partition_quick_sort(numbers)
        self.assertSequenceEqual([1], numbers)

        numbers = [31, 41, 59, 26, 41, 58]
        three_way_partition_quick_sort(numbers)
        self.assertSequenceEqual([26, 31, 41, 41, 58, 59], numbers)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        three_way_partition_quick_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        three_way_partition_quick_sort(numbers)
        self.assertSequenceEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], numbers)

        numbers = [4, 6, 13, 8, 13, 19, 20, 21, 13]
        three_way_partition_quick_sort(numbers)
        self.assertSequenceEqual([4, 6, 8, 13, 13, 13, 19, 20, 21], numbers)


if __name__ == '__main__':
    unittest.main()
