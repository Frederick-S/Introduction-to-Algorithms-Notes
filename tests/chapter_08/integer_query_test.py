import unittest
from src.chapter_08.integer_query import IntegerQuery


class TestIntegerQuery(unittest.TestCase):
    def test_integer_query(self):
        integer_query = IntegerQuery([1])
        self.assertEqual(1, integer_query.query(0, 1))

        integer_query = IntegerQuery([2, 5, 3, 0, 2, 3, 0, 3])
        self.assertEqual(6, integer_query.query(1, 5))

        integer_query = IntegerQuery([31, 41, 59, 26, 41, 58])
        self.assertEqual(0, integer_query.query(10, 15))

        integer_query = IntegerQuery([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(9, integer_query.query(1, 9))


if __name__ == '__main__':
    unittest.main()
