def heap_sort(numbers):
    length = len(numbers)
    heap_size = length

    build_max_heap(numbers)

    for i in range(length - 1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heap_size -= 1
        max_heapify(numbers, 0, heap_size)


def max_heapify(numbers, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left <= heap_size - 1 and numbers[left] > numbers[i]:
        largest = left

    if right <= heap_size - 1 and numbers[right] > numbers[largest]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]

        max_heapify(numbers, largest, heap_size)


def build_max_heap(numbers):
    heap_size = len(numbers)

    for i in range((heap_size - 1) // 2, -1, -1):
        max_heapify(numbers, i, heap_size)
