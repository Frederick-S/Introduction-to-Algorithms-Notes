class SinglyLinkedNode(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, key, value=None):
        new = SinglyLinkedNode(key, value)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def remove_head(self):
        if self.head is not None:
            head, self.head = self.head, self.head.next

            if self.head is None:
                self.tail = None

            return head

    def search(self, key):
        node = self.head

        while node is not None and node.key != key:
            node = node.next

        return node

    def insert(self, key, value=None):
        new = SinglyLinkedNode(key, value)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next, self.head = self.head, new

    def delete(self, key):
        prev = None
        current = self.head

        while current is not None and current.key != key:
            prev = current
            current = current.next

        if current is None:
            raise Exception('The specified key does not exist')

        if prev is None:
            self.head = current.next

            if self.head is None:
                self.tail = None
        else:
            prev.next = current.next

            if prev.next is None:
                self.tail = prev
