import unittest
from src.chapter_10.set_union import set_union
from src.chapter_10.singly_linked_list import SinglyLinkedList


class TestSetUnion(unittest.TestCase):
    def test_queue_using_two_stacks(self):
        s1 = SinglyLinkedList()
        s1.append(1, 1)
        s1.append(2, 2)
        s1.append(3, 3)
        s2 = SinglyLinkedList()
        s2.append(4, 4)
        s2.append(5, 5)
        s2.append(6, 6)

        new_set = set_union(s1, s2)
        expected_values = [i for i in range(1, 7)]
        current = new_set.head

        while current is not None:
            self.assertEqual(expected_values.pop(0), current.value)

            current = current.next


if __name__ == '__main__':
    unittest.main()
