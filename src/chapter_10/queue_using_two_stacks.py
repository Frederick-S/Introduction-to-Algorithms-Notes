from .stack import Stack


class QueueUsingTwoStacks(object):
    def __init__(self, n):
        self.size = n
        self.stack_in = Stack(n)
        self.stack_out = Stack(n)

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()

    def is_full(self):
        return self.stack_in.count + self.stack_out.count == self.size

    def enqueue(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.stack_in.push(x)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Underflow')

        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

            return self.stack_out.pop()
        else:
            return self.stack_out.pop()
