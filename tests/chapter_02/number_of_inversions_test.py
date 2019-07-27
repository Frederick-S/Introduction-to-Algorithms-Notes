import unittest
from src.chapter_02.number_of_inversions import number_of_inversions


class TestNumberOfInversions(unittest.TestCase):
    def test_number_of_inversions(self):
        numbers = []
        self.assertEqual(0, number_of_inversions(numbers))

        numbers = [1]
        self.assertEqual(0, number_of_inversions(numbers))

        numbers = [31, 41, 59, 26, 41, 58]
        self.assertEqual(5, number_of_inversions(numbers))

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(0, number_of_inversions(numbers))

        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(36, number_of_inversions(numbers))


if __name__ == '__main__':
    unittest.main()
