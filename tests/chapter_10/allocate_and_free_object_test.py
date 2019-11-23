import unittest
from src.chapter_10.allocate_and_free_object import SingleArrayObjects


class TestSingleArrayObjects(unittest.TestCase):
    def test_allocate_and_free_object(self):
        single_array_objects = SingleArrayObjects(15)

        self.assertEqual(0, single_array_objects.allocate_object())
        self.assertEqual(3, single_array_objects.allocate_object())
        self.assertEqual(6, single_array_objects.free)

        single_array_objects.free_object(3)
        self.assertEqual(3, single_array_objects.free)

        single_array_objects.allocate_object()
        single_array_objects.allocate_object()
        single_array_objects.allocate_object()
        single_array_objects.allocate_object()
        self.assertRaises(Exception, single_array_objects.allocate_object)


if __name__ == '__main__':
    unittest.main()
