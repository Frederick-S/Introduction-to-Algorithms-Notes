class DoublyLinkedNode(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def search(self, key):
        node = self.head

        while node is not None and node.key != key:
            node = node.next

        return node

    def insert(self, key):
        new = DoublyLinkedNode(key)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def delete(self, key):
        node = self.search(key)

        if node is None:
            raise Exception('The specified key does not exist')

        if node == self.head:
            self.head = node.next

            if node.next is not None:
                node.next.prev = None
        else:
            node.prev.next = node.next

            if node.next is not None:
                node.next.prev = node.prev
