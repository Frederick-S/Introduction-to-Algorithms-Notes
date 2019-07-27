def second_smallest_element(numbers):
    assert len(numbers) >= 2

    node = minify(numbers, 0, len(numbers) - 1)

    second_smallest = 0

    if node.left_is_smaller:
        second_smallest = node.right.value
        node = node.left
    else:
        second_smallest = node.left.value
        node = node.right

    while node is not None:
        if node.left_is_smaller:
            if node.right is not None:
                second_smallest = min(node.right.value, second_smallest)

            node = node.left
        else:
            if node.left is not None:
                second_smallest = min(node.left.value, second_smallest)

            node = node.right

    return second_smallest


def minify(numbers, low, high):
    if low < high:
        middle = (low + high) // 2

        left = minify(numbers, low, middle)
        right = minify(numbers, middle + 1, high)

        node = None

        if left.value < right.value:
            node = Node(left.value)
            node.left_is_smaller = True
        else:
            node = Node(right.value)
            node.left_is_smaller = False

        node.left = left
        node.right = right

        return node
    elif low == high:
        return Node(numbers[low])


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None

        # The smaller one of left and right
        self.value = value
        self.left_is_smaller = True
