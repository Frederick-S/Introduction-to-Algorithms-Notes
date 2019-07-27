from .singly_linked_list import SinglyLinkedList


class StackUsingSinglyLinkedList(object):
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def is_empty(self):
        return self.singly_linked_list.head is None

    def push(self, x):
        self.singly_linked_list.insert(x)

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')

        return self.singly_linked_list.remove_head()
