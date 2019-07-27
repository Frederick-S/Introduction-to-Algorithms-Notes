from .singly_linked_circular_list import SinglyLinkedCircularList


class DictUsingSinglyLinkedCircularList(object):
    def __init__(self):
        self.singly_linked_circular_list = SinglyLinkedCircularList()

    def insert(self, key, value):
        dict_value = self.search(key)

        if dict_value:
            raise Exception('The specified key already exists')
        else:
            self.singly_linked_circular_list.insert(key, value)

    def delete(self, key):
        value = self.search(key)

        if value:
            self.singly_linked_circular_list.delete(key)
        else:
            raise Exception('The specified key does not exist')

    def search(self, key):
        node = self.singly_linked_circular_list.search(key)

        return node.value if node else None
