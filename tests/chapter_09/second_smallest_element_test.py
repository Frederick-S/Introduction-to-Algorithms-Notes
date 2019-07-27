import unittest
from src.chapter_09.second_smallest_element import second_smallest_element


class TestSecondSmallestElement(unittest.TestCase):
    def test_second_smallest_element(self):
        numbers = [3, 2]
        self.assertEqual(3, second_smallest_element(numbers))

        numbers = [2, 5, 3, 0, 2, 3, 0, 3]
        self.assertEqual(0, second_smallest_element(numbers))

        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(1, second_smallest_element(numbers))

        numbers = [31, 41, 59, 26, 41, 58]
        self.assertEqual(31, second_smallest_element(numbers))


if __name__ == '__main__':
    unittest.main()
