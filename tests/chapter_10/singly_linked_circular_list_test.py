import unittest
from src.chapter_10.singly_linked_circular_list import SinglyLinkedCircularList


class TestSinglyLinkedCircularList(unittest.TestCase):
    def test_singly_linked_circular_list(self):
        singly_linked_circular_list = SinglyLinkedCircularList()
        singly_linked_circular_list.insert(1)
        singly_linked_circular_list.insert(2)
        singly_linked_circular_list.insert(3)
        self.assertEqual(None, singly_linked_circular_list.search(4))
        self.assertEqual(1, singly_linked_circular_list.search(1).key)

        singly_linked_circular_list.delete(1)
        self.assertEqual(None, singly_linked_circular_list.search(1))

        singly_linked_circular_list.delete(2)
        singly_linked_circular_list.remove_head()
        self.assertTrue(singly_linked_circular_list.is_empty())
        with self.assertRaises(Exception):
            singly_linked_circular_list.remove_head()

        singly_linked_circular_list.append(4)
        self.assertEqual(4, singly_linked_circular_list.head.key)
        self.assertEqual(
            singly_linked_circular_list.head,
            singly_linked_circular_list.tail.next)

        singly_linked_circular_list.append(5)
        singly_linked_circular_list.remove_head()
        self.assertEqual(5, singly_linked_circular_list.head.key)
        self.assertEqual(5, singly_linked_circular_list.tail.key)

        singly_linked_circular_list.delete(5)
        self.assertEqual(None, singly_linked_circular_list.head)
        self.assertEqual(None, singly_linked_circular_list.tail)
        with self.assertRaises(Exception):
            singly_linked_circular_list.delete(6)

        singly_linked_circular_list.insert(1)
        with self.assertRaises(Exception):
            singly_linked_circular_list.delete(2)


if __name__ == '__main__':
    unittest.main()
