import unittest
from src.chapter_06.priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_priority_queue(self):
        elements = [1, 2, 6, 0, 4, 7, 8, 12, 5, 9, 13, 15]
        priority_queue = PriorityQueue(elements)

        self.assertEqual(15, priority_queue.maximum())
        self.assertEqual(15, priority_queue.extract_max())
        self.assertEqual(13, priority_queue.maximum())
        self.assertEqual(11, priority_queue.heap_size)

        priority_queue.increase_key(1, 20)
        self.assertEqual(20, priority_queue.maximum())

        priority_queue.insert(100)
        self.assertEqual(100, priority_queue.maximum())
        self.assertEqual(12, priority_queue.heap_size)

        priority_queue.delete(0)
        self.assertEqual(20, priority_queue.maximum())
        self.assertEqual(11, priority_queue.heap_size)


if __name__ == '__main__':
    unittest.main()
