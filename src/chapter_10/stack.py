class Stack(object):
    def __init__(self, n):
        self.top = -1
        self.size = n
        self.count = 0
        self.elements = [0] * n

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.top += 1
        self.count += 1
        self.elements[self.top] = x

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')

        self.top -= 1
        self.count -= 1

        return self.elements[self.top + 1]
