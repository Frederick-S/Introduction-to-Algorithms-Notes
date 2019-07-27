import sys


class DAryHeap(object):
    def __init__(self, d, elements):
        assert d >= 2

        self.d = d
        self.elements = elements
        self.heap_size = len(elements)

        self.build_max_heap()

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

        self.max_heapify(i)

    def maximum(self):
        assert not self.is_empty()

        return self.elements[0]

    def extract_max(self):
        assert not self.is_empty()

        maximum = self.elements[0]
        self.elements[0] = self.elements[self.heap_size - 1]
        self.heap_size -= 1

        self.max_heapify(0)

        return maximum

    def increase_key(self, i, key):
        assert not self.is_empty()
        assert 0 <= i < self.heap_size
        assert key >= self.elements[i]

        while i > 0 and self.elements[(i - 1) // self.d] < key:
            self.elements[i] = self.elements[(i - 1) // self.d]
            i = (i - 1) // self.d

        self.elements[i] = key

    def is_empty(self):
        return self.heap_size == 0

    def max_heapify(self, i):
        largest = i

        for k in range(self.d):
            child = self.d * i + k + 1

            if (child <= self.heap_size - 1 and
                    self.elements[child] > self.elements[largest]):
                largest = child

        if largest != i:
            self.elements[i], self.elements[largest] = \
                self.elements[largest], self.elements[i]

            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range((self.heap_size - 1) // self.d, -1, -1):
            self.max_heapify(i)
