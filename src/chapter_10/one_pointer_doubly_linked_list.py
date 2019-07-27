import ctypes


class OnePointerDoublyLinkedNode(object):
    def __init__(self, key):
        self.key = key
        self.np = None


class OnePointerDoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}

    def search(self, key):
        node = self.head
        prev = 0

        while node is not None and node.key != key:
            if node == self.tail:
                return None

            new_prev = id(node)
            node = ctypes.cast(node.np ^ prev, ctypes.py_object).value
            prev = new_prev

        return node

    def insert(self, key):
        new = OnePointerDoublyLinkedNode(key)

        if self.head is None:
            self.head = new
            self.head.np = 0 ^ 0
            self.tail = new
            self.tail.np = 0 ^ 0
        else:
            new.np = id(self.head) ^ 0
            self.head.np = (self.head.np ^ 0) ^ id(new)
            self.head = new

        # Keep reference of each node
        self.nodes[id(new)] = new

    def delete(self, key):
        node = self.head
        prev_pointer = 0
        prev_node = None

        while node is not None and node.key != key:
            if node == self.tail:
                raise Exception('The specified key does not exist')

            new_prev_pointer = id(node)
            prev_node = node
            node = ctypes.cast(node.np ^ prev_pointer, ctypes.py_object).value
            prev_pointer = new_prev_pointer

        if node is None:
            raise Exception('The specified key does not exist')

        if node == self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                next = ctypes.cast(node.np ^ 0, ctypes.py_object).value
                next.np = (next.np ^ id(node)) ^ 0
                self.head = next
        elif node == self.tail:
            prev_node.np = (prev_node.np ^ id(node)) ^ 0
            self.tail = prev_node
        else:
            next = ctypes.cast(node.np ^ prev_pointer, ctypes.py_object).value
            next.np = (next.np ^ id(node)) ^ prev_pointer
            prev_node.np = (prev_node.np ^ id(node)) ^ id(next)

        self.nodes.pop(id(node), None)

    def reverse(self):
        # self.head.np, self.tail.np = self.tail.np, self.head.np
        self.head, self.tail = self.tail, self.head
