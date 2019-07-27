from .singly_linked_list import SinglyLinkedList


class QueueUsingSinglyLinkedList(object):
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def is_empty(self):
        return self.singly_linked_list.head is None

    def enqueue(self, x):
        self.singly_linked_list.append(x)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Underflow')

        return self.singly_linked_list.remove_head()
