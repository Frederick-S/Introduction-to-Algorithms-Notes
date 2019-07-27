import unittest
from src.chapter_10.queue_using_singly_linked_list \
    import QueueUsingSinglyLinkedList


class TestQueueUsingSinglyLinkedList(unittest.TestCase):
    def test_queue_using_singly_linked_list(self):
        queue = QueueUsingSinglyLinkedList()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        self.assertEqual(1, queue.dequeue().key)
        self.assertEqual(2, queue.dequeue().key)
        self.assertEqual(3, queue.dequeue().key)

        queue.enqueue(6)
        queue.enqueue(7)
        queue.enqueue(8)

        self.assertEqual(4, queue.dequeue().key)
        self.assertEqual(5, queue.dequeue().key)
        self.assertEqual(6, queue.dequeue().key)
        self.assertEqual(7, queue.dequeue().key)
        self.assertEqual(8, queue.dequeue().key)
        self.assertTrue(queue.is_empty())
        self.assertRaises(Exception, queue.dequeue)


if __name__ == '__main__':
    unittest.main()
