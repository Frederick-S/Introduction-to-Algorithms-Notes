import unittest
from src.chapter_06.d_ary_heap import DAryHeap


class TestDAryHeap(unittest.TestCase):
    def test_d_ary_heap(self):
        elements = [1, 2, 6, 0, 4, 7, 8, 12, 5, 9, 13, 15]
        d_ary_heap = DAryHeap(4, elements)

        self.assertEqual(15, d_ary_heap.maximum())
        self.assertEqual(15, d_ary_heap.extract_max())
        self.assertEqual(13, d_ary_heap.maximum())
        self.assertEqual(11, d_ary_heap.heap_size)

        d_ary_heap.increase_key(1, 20)
        self.assertEqual(20, d_ary_heap.maximum())

        d_ary_heap.insert(100)
        self.assertEqual(100, d_ary_heap.maximum())
        self.assertEqual(12, d_ary_heap.heap_size)

        d_ary_heap.delete(0)
        self.assertEqual(20, d_ary_heap.maximum())
        self.assertEqual(11, d_ary_heap.heap_size)


if __name__ == '__main__':
    unittest.main()
