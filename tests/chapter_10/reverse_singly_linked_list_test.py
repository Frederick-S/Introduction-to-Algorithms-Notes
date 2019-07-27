import unittest
from src.chapter_10.singly_linked_list import SinglyLinkedList
from src.chapter_10.reverse_singly_linked_list \
    import reverse_singly_linked_list


class TestReverseSinglyLinkedList(unittest.TestCase):
    def test_reverse_singly_linked_list(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.append(1)
        singly_linked_list.append(2)
        singly_linked_list.append(3)
        singly_linked_list.append(4)
        singly_linked_list.append(5)

        reversed_singly_linked_list = reverse_singly_linked_list(
            singly_linked_list)

        keys = []
        current = reversed_singly_linked_list.head

        while current is not None:
            keys.append(current.key)

            current = current.next

        self.assertEqual(5, reversed_singly_linked_list.head.key)
        self.assertEqual(1, reversed_singly_linked_list.tail.key)
        self.assertListEqual([5, 4, 3, 2, 1], keys)


if __name__ == '__main__':
    unittest.main()
