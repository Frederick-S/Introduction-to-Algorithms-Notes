import unittest
from src.chapter_10.queue import Queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertRaises(Exception, queue.enqueue, 6)

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        queue.enqueue(6)
        queue.enqueue(7)
        queue.enqueue(8)
        self.assertTrue(queue.is_full())

        self.assertEqual(4, queue.dequeue())
        self.assertEqual(5, queue.dequeue())
        self.assertEqual(6, queue.dequeue())
        self.assertEqual(7, queue.dequeue())
        self.assertEqual(8, queue.dequeue())
        self.assertTrue(queue.is_empty())
        self.assertRaises(Exception, queue.dequeue)


if __name__ == '__main__':
    unittest.main()
