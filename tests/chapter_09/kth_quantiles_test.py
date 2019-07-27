import unittest
import random
from src.chapter_09.kth_quantiles import kth_quantiles


class TestKthQuantiles(unittest.TestCase):
    def test_kth_quantiles(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        quantiles = kth_quantiles(numbers, 3)
        quantiles.sort()
        self.assertSequenceEqual([3, 6], quantiles)

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        quantiles = kth_quantiles(numbers, 3)
        quantiles.sort()
        self.assertSequenceEqual([3, 6], quantiles)

        numbers = [i for i in range(1, 21)]
        quantiles = kth_quantiles(numbers, 4)
        quantiles.sort()
        self.assertSequenceEqual([5, 10, 15], quantiles)

        numbers = [i for i in range(1, 31)]
        quantiles = kth_quantiles(numbers, 8)
        quantiles.sort()
        self.assertSequenceEqual([i for i in range(4, 30, 4)], quantiles)

        numbers = [i for i in range(1, 101)]
        random.shuffle(numbers)
        quantiles = kth_quantiles(numbers, 13)
        quantiles.sort()
        self.assertSequenceEqual([i for i in range(8, 100, 8)], quantiles)

        numbers = [i for i in range(1, 1000)]
        random.shuffle(numbers)
        quantiles = kth_quantiles(numbers, 19)
        quantiles.sort()
        self.assertSequenceEqual([i for i in range(53, 1000, 53)], quantiles)


if __name__ == '__main__':
    unittest.main()
