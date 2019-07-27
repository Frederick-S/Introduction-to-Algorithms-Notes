import unittest
import random
from src.chapter_09.i_largest_by_order_statistic \
    import i_largest_by_order_statistic


class TestILargestByOrderStatistic(unittest.TestCase):
    def test_i_largest_by_order_statistic(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertSequenceEqual(
            [7, 8, 9], i_largest_by_order_statistic(numbers, 3))

        numbers = [i for i in range(1, 1001)]
        self.assertSequenceEqual(
            [i for i in range(971, 1001)],
            i_largest_by_order_statistic(numbers, 30))

        numbers = [random.randint(1, 1000) for _ in range(1000)]
        self.assertSequenceEqual(
            sorted(numbers)[889:], i_largest_by_order_statistic(numbers, 111))


if __name__ == '__main__':
    unittest.main()
