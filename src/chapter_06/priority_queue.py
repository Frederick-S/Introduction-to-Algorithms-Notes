import sys
from .heap_sort import max_heapify, build_max_heap


class PriorityQueue(object):
    def __init__(self, elements):
        self.elements = elements
        self.heap_size = len(elements)

        build_max_heap(self.elements)

    def insert(self, key):
        self.heap_size += 1

        if len(self.elements) < self.heap_size:
            self.elements.append(-sys.maxsize)
        else:
            self.elements[self.heap_size - 1] = -sys.maxsize

        self.increase_key(self.heap_size - 1, key)

    def delete(self, i):
        assert not self.is_empty()
        assert 0 <= i < self.heap_size

        self.elements[i] = self.elements[self.heap_size - 1]
        self.heap_size -= 1

        max_heapify(self.elements, i, self.heap_size)

    def maximum(self):
        assert not self.is_empty()

        return self.elements[0]

    def extract_max(self):
        assert not self.is_empty()

        maximum = self.elements[0]
        self.elements[0] = self.elements[self.heap_size - 1]
        self.heap_size -= 1

        max_heapify(self.elements, 0, self.heap_size)

        return maximum

    def increase_key(self, i, key):
        assert not self.is_empty()
        assert 0 <= i < self.heap_size
        assert key >= self.elements[i]

        while i > 0 and self.elements[(i - 1) // 2] < key:
            self.elements[i] = self.elements[(i - 1) // 2]
            i = (i - 1) // 2

        self.elements[i] = key

    def is_empty(self):
        return self.heap_size == 0
