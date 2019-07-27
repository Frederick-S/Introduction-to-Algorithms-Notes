import unittest
from src.chapter_06.merge_sorted_lists import merge_sorted_lists


class TestMergeSortedLists(unittest.TestCase):
    def test_merge_sorted_lists(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], merge_sorted_lists(lists))

        lists = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        self.assertSequenceEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], merge_sorted_lists(lists))


if __name__ == '__main__':
    unittest.main()
