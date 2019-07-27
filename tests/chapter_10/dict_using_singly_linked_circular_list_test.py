import unittest
from src.chapter_10.dict_using_singly_linked_circular_list \
    import DictUsingSinglyLinkedCircularList


class TestDictUsingSinglyLinkedCircularList(unittest.TestCase):
    def test_dict_using_singly_linked_circular_list(self):
        dict_using_singly_linked_circular_list = \
            DictUsingSinglyLinkedCircularList()
        dict_using_singly_linked_circular_list.insert(1, 1)
        self.assertEqual(1, dict_using_singly_linked_circular_list.search(1))
        self.assertEqual(
            None, dict_using_singly_linked_circular_list.search(2))

        dict_using_singly_linked_circular_list.insert(2, 2)
        with self.assertRaises(Exception):
            dict_using_singly_linked_circular_list.insert(2, 2)

        dict_using_singly_linked_circular_list.delete(2)
        with self.assertRaises(Exception):
            dict_using_singly_linked_circular_list.delete(2)


if __name__ == '__main__':
    unittest.main()
