from .singly_linked_list import SinglyLinkedNode


class SinglyLinkedCircularList(object):
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
            self.tail.next = self.head
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

    def remove_head(self):
        if self.is_empty():
            raise Exception("List is empty")
        elif self.head == self.tail:
            head = self.head

            self.head = None
            self.tail = None

            return head
        else:
            head, self.head = self.head, self.head.next
            self.tail.next = self.head

            return head

    def search(self, key):
        node = self.head

        while node is not None and node.next != self.head and node.key != key:
            node = node.next

        return node if node is not None and node.key == key else None

    def insert(self, key, value=None):
        new = SinglyLinkedNode(key, value)

        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new.next, self.head = self.head, new
            self.tail.next = self.head

    def delete(self, key):
        if self.is_empty():
            raise Exception("List is empty")

        prev = None
        current = self.head

        while (current is not None and current.next != self.head and
               current.key != key):
            prev = current
            current = current.next

        if current == self.tail and current.key != key:
            raise Exception('The specified key does not exist')

        if current == self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = current.next
                self.tail.next = self.head
        else:
            prev.next = current.next

            if current == self.tail:
                self.tail = prev
