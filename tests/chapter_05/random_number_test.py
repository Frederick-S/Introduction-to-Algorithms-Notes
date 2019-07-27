import unittest
from src.chapter_05.random_number import random_number


class TestRandomNumber(unittest.TestCase):
    def test_random_number(self):
        self.assertEqual(5, random_number(5, 5))
        self.assertEqual(True, 1 <= random_number(1, 10) <= 10)


if __name__ == '__main__':
    unittest.main()
