from ..chapter_06.priority_queue import PriorityQueue


def i_largest_by_max_priority_queue(numbers, i):
    priority_queue = PriorityQueue(numbers)

    result = []

    for _ in range(i):
        result = [priority_queue.extract_max()] + result

    return result
