from .queue import Queue


class StackUsingTwoQueues(object):
    def __init__(self, n):
        self.queue = Queue(n)
        self.queue_auxiliary = Queue(n)

    def is_empty(self):
        return self.queue.is_empty()

    def is_full(self):
        return self.queue.is_full()

    def push(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.queue.enqueue(x)

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')

        x = -1

        while not self.queue.is_empty():
            x = self.queue.dequeue()

            if not self.queue.is_empty():
                self.queue_auxiliary.enqueue(x)

        self.queue, self.queue_auxiliary = self.queue_auxiliary, self.queue

        return x
