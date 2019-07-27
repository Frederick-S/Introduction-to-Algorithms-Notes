import unittest
import random
from src.chapter_09.select import select


class TestSelect(unittest.TestCase):
    def test_select(self):
        numbers = [1, 1, 0, 0, 0]
        self.assertEqual(0, select(numbers, 3))

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(5, select(numbers, 5))

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(8, select(numbers, 8))

        numbers = [i for i in range(1, 21)]
        random.shuffle(numbers)
        self.assertEqual(16, select(numbers, 16))

        numbers = [i for i in range(1, 101)]
        random.shuffle(numbers)
        self.assertEqual(41, select(numbers, 41))

        numbers = [i for i in range(1, 1001)]
        random.shuffle(numbers)
        self.assertEqual(999, select(numbers, 999))


if __name__ == '__main__':
    unittest.main()
