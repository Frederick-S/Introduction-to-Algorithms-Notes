import unittest
from src.chapter_10.deque import Deque


class TestDeque(unittest.TestCase):
    def test_deque(self):
        deque = Deque(5)
        deque.append(1)
        deque.append(2)
        deque.append(3)
        self.assertEqual(3, deque.pop())

        deque.append_left(4)
        deque.append_left(5)
        self.assertEqual(5, deque.shift())
        self.assertEqual(4, deque.shift())
        self.assertEqual(1, deque.shift())
        self.assertEqual(2, deque.shift())
        self.assertRaises(Exception, deque.shift)
        self.assertRaises(Exception, deque.pop)

        deque.append_left(1)
        deque.append_left(2)
        deque.append_left(3)
        deque.append(4)
        deque.append(5)
        self.assertRaises(Exception, deque.append, 6)
        self.assertRaises(Exception, deque.append_left, 6)
        self.assertEqual(5, deque.pop())
        self.assertEqual(4, deque.pop())
        self.assertEqual(1, deque.pop())
        self.assertEqual(2, deque.pop())
        self.assertEqual(3, deque.pop())
        self.assertRaises(Exception, deque.pop)

        deque.append(1)
        deque.append(2)
        deque.append(3)
        deque.append_left(4)
        deque.append_left(5)
        deque.pop()
        deque.pop()
        deque.pop()
        deque.append(1)
        self.assertEqual(1, deque.pop())

        deque = Deque(5)
        deque.append_left(1)
        deque.append_left(2)
        deque.append_left(3)
        deque.append_left(4)
        self.assertEqual(1, deque.pop())

        deque.append_left(5)
        deque.append_left(6)
        self.assertEqual(6, deque.shift())

        deque = Deque(5)
        deque.append(1)
        self.assertEqual(1, deque.shift())


if __name__ == '__main__':
    unittest.main()
