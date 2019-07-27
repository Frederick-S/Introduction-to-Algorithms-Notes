import unittest
from src.chapter_10.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_doubly_linked_list(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert(1)
        doubly_linked_list.insert(2)
        doubly_linked_list.insert(3)
        self.assertEqual(None, doubly_linked_list.search(4))
        self.assertEqual(1, doubly_linked_list.search(1).key)

        doubly_linked_list.delete(1)
        self.assertEqual(None, doubly_linked_list.search(1))

        doubly_linked_list.delete(2)
        doubly_linked_list.delete(3)
        self.assertTrue(doubly_linked_list.is_empty())

        doubly_linked_list.insert(1)
        doubly_linked_list.insert(2)
        doubly_linked_list.insert(3)
        doubly_linked_list.delete(2)
        node = doubly_linked_list.search(3)
        self.assertEqual(1, node.next.key)

        doubly_linked_list.delete(3)
        self.assertEqual(1, doubly_linked_list.head.key)

        with self.assertRaises(Exception):
            doubly_linked_list.delete(6)


if __name__ == '__main__':
    unittest.main()
