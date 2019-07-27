class Queue(object):
    def __init__(self, n):
        self.head = -1
        self.tail = 0
        self.size = n
        self.elements = [0] * n

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.head == self.tail

    def enqueue(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.elements[self.tail] = x

        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

        if self.head == -1:
            self.head = 0

    def dequeue(self):
        if self.is_empty():
            raise Exception('Underflow')

        x = self.elements[self.head]

        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1

        if self.head == self.tail:
            self.head = -1
            self.tail = 0

        return x
