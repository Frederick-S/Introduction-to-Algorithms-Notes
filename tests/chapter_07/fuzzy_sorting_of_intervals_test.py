import unittest
from src.chapter_07.fuzzy_sorting_of_intervals \
    import fuzzy_sorting_of_intervals


class TestFuzzySortingOfIntervals(unittest.TestCase):
    def test_fuzzy_sorting_of_intervals(self):
        intervals = []
        fuzzy_sorting_of_intervals(intervals)
        self.assertSequenceEqual([], intervals)

        intervals = [[1, 2]]
        fuzzy_sorting_of_intervals(intervals)
        self.assertSequenceEqual([[1, 2]], intervals)

        intervals = [[7, 8], [3, 6], [2, 5], [1, 4]]
        fuzzy_sorting_of_intervals(intervals)
        self.assertSequenceEqual([7, 8], intervals[3])

        intervals = [
            [13, 14], [4, 8], [7, 12], [20, 21], [12, 15], [3, 5],
            [0, 1], [10, 17], [9, 20], [30, 31]]
        fuzzy_sorting_of_intervals(intervals)
        self.assertSequenceEqual([0, 1], intervals[0])
        self.assertSequenceEqual([30, 31], intervals[9])


if __name__ == '__main__':
    unittest.main()
