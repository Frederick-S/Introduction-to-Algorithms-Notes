import sys
import unittest
from src.chapter_06.young_tableau import *


class TestYoungTableau(unittest.TestCase):
    def test_young_tableau(self):
        matrix = [
                [2, 3, 4, 5], [8, 9, 12, 14],
                [16, sys.maxsize, sys.maxsize, sys.maxsize],
                [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]]
        self.assertEqual(2, young_tableau_extract_min(matrix))
        self.assertSequenceEqual([
            [3, 4, 5, 14],
            [8, 9, 12, sys.maxsize],
            [16, sys.maxsize, sys.maxsize, sys.maxsize],
            [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]],
            matrix)

        young_tableau_insert(matrix, 1)
        self.assertSequenceEqual([
            [1, 3, 4, 5],
            [8, 9, 12, 14],
            [16, sys.maxsize, sys.maxsize, sys.maxsize],
            [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]],
            matrix)

        self.assertTrue(young_tableau_find(matrix, 1))
        self.assertFalse(young_tableau_find(matrix, 20))


if __name__ == '__main__':
    unittest.main()
