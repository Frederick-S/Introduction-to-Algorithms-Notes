import ctypes
import unittest
from src.chapter_10.one_pointer_doubly_linked_list \
    import OnePointerDoublyLinkedList


def get_all_keys(one_pointer_doubly_linked_list):
    keys = []
    node = one_pointer_doubly_linked_list.head
    prev = 0

    while node is not None:
        keys.append(node.key)

        if node == one_pointer_doubly_linked_list.tail:
            break

        new_prev = id(node)
        node = ctypes.cast(node.np ^ prev, ctypes.py_object).value
        prev = new_prev

    return keys


class TestOnePointerDoublyLinkedList(unittest.TestCase):
    def test_one_pointer_doubly_linked_list(self):
        one_pointer_doubly_linked_list = OnePointerDoublyLinkedList()
        one_pointer_doubly_linked_list.insert(1)
        one_pointer_doubly_linked_list.insert(2)
        one_pointer_doubly_linked_list.insert(3)
        self.assertTrue([1, 2, 3],
                        get_all_keys(one_pointer_doubly_linked_list))
        self.assertEqual(3, one_pointer_doubly_linked_list.head.key)
        self.assertEqual(1, one_pointer_doubly_linked_list.tail.key)
        self.assertEqual(2, one_pointer_doubly_linked_list.search(2).key)
        self.assertEqual(None, one_pointer_doubly_linked_list.search(4))

        one_pointer_doubly_linked_list.delete(3)
        self.assertEqual(None, one_pointer_doubly_linked_list.search(3))
        self.assertEqual(2, one_pointer_doubly_linked_list.head.key)
        with self.assertRaises(Exception):
            one_pointer_doubly_linked_list.delete(6)

        one_pointer_doubly_linked_list.insert(3)
        one_pointer_doubly_linked_list.delete(2)
        one_pointer_doubly_linked_list.delete(1)
        one_pointer_doubly_linked_list.delete(3)
        self.assertEqual(None, one_pointer_doubly_linked_list.head)
        self.assertEqual(None, one_pointer_doubly_linked_list.tail)
        with self.assertRaises(Exception):
            one_pointer_doubly_linked_list.delete(6)

        one_pointer_doubly_linked_list.insert(1)
        one_pointer_doubly_linked_list.insert(2)
        one_pointer_doubly_linked_list.insert(3)
        one_pointer_doubly_linked_list.insert(4)
        one_pointer_doubly_linked_list.insert(5)
        one_pointer_doubly_linked_list.reverse()
        self.assertEqual(1, one_pointer_doubly_linked_list.head.key)
        self.assertEqual(5, one_pointer_doubly_linked_list.tail.key)
        self.assertEqual([1, 2, 3, 4, 5],
                         get_all_keys(one_pointer_doubly_linked_list))


if __name__ == '__main__':
    unittest.main()
