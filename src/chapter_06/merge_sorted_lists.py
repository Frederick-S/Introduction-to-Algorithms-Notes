def merge_sorted_lists(lists):
    sorted_list = []
    min_heap_elements = []

    for i, value in enumerate(lists):
        min_heap_elements.append(MinHeapElement(i, 1, value[0]))

    min_heap = MinHeap(min_heap_elements)

    while not min_heap.is_empty():
        min_element = min_heap.extract_min()
        sorted_list.append(min_element.value)

        list_index = min_element.list_index
        next_index = min_element.next_index

        if next_index < len(lists[list_index]):
            next_element = MinHeapElement(
                list_index, next_index + 1, lists[list_index][next_index])

            min_heap.insert(next_element)

    return sorted_list


class MinHeapElement(object):
    def __init__(self, list_index, next_index, value):
        self.list_index = list_index
        self.next_index = next_index
        self.value = value


class MinHeap(object):
    def __init__(self, elements):
        self.elements = elements
        self.heap_size = len(elements)

        self.build_min_heap()

    def extract_min(self):
        assert not self.is_empty()

        minimum = self.elements[0]
        self.elements[0] = self.elements[self.heap_size - 1]
        self.heap_size -= 1

        self.min_heapify(0)

        return minimum

    def insert(self, element):
        self.heap_size += 1

        if len(self.elements) < self.heap_size:
            self.elements.append(element)
        else:
            self.elements[self.heap_size - 1] = element

        self.decrease_element(self.heap_size - 1, element)

    def decrease_element(self, i, element):
        assert i < self.heap_size
        assert element.value <= self.elements[i].value

        while i > 0 and self.elements[(i - 1) // 2].value > element.value:
            self.elements[i] = self.elements[(i - 1) // 2]
            i = (i - 1) // 2

        self.elements[i] = element

    def is_empty(self):
        return self.heap_size == 0

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minimum = i

        if (left <= self.heap_size - 1 and
                self.elements[left].value < self.elements[i].value):
            minimum = left

        if (right <= self.heap_size - 1 and
                self.elements[right].value < self.elements[minimum].value):
            minimum = right

        if minimum != i:
            self.elements[i], self.elements[minimum] = \
                self.elements[minimum], self.elements[i]

            self.min_heapify(minimum)

    def build_min_heap(self):
        for i in range((self.heap_size - 1) // 2, -1, -1):
            self.min_heapify(i)
