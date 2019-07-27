import unittest
from src.chapter_08.bucket_sort import bucket_sort


class TestBucketSort(unittest.TestCase):
    def test_bucket_sort(self):
        numbers = []
        self.assertSequenceEqual([], bucket_sort(numbers))

        numbers = [0.1]
        self.assertSequenceEqual([0.1], bucket_sort(numbers))

        numbers = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
        self.assertSequenceEqual(
            [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94],
            bucket_sort(numbers))

        numbers = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71]
        self.assertSequenceEqual(
            [0.13, 0.16, 0.20, 0.39, 0.53, 0.64, 0.71, 0.79, 0.89],
            bucket_sort(numbers))


if __name__ == '__main__':
    unittest.main()
