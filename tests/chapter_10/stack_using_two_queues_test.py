import unittest
from src.chapter_10.stack_using_two_queues import StackUsingTwoQueues


class TestStackUsingTwoQueues(unittest.TestCase):
    def test_stack_using_two_queues(self):
        stack = StackUsingTwoQueues(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        with self.assertRaises(Exception):
            stack.push(6)

        self.assertEqual(5, stack.pop())
        self.assertEqual(4, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertRaises(Exception, stack.pop)


if __name__ == '__main__':
    unittest.main()
