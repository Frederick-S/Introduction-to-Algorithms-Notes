import unittest
from src.chapter_10.stack_using_singly_linked_list \
    import StackUsingSinglyLinkedList


class TestStackUsingSinglyLinkedList(unittest.TestCase):
    def test_stack_using_singly_linked_list(self):
        stack = StackUsingSinglyLinkedList()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)

        self.assertEqual(5, stack.pop().key)
        self.assertEqual(4, stack.pop().key)
        self.assertEqual(3, stack.pop().key)
        self.assertEqual(2, stack.pop().key)
        self.assertEqual(1, stack.pop().key)
        self.assertRaises(Exception, stack.pop)


if __name__ == '__main__':
    unittest.main()
