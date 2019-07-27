class Deque(object):
    def __init__(self, n):
        self.elements = [-1] * n
        self.size = n
        self.left = -1
        self.right = n

    def is_empty(self):
        return self.left == -1 and self.right == self.size

    def is_full(self):
        return self.right - self.left == 1

    def append(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.right -= 1

        if self.right == -1:
            self.right = self.size - 1

        self.elements[self.right] = x

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')

        if self.right == self.size:
            self.right = 0

        x = self.elements[self.right]

        if self.left == self.right:
            self.left = -1
            self.right = self.size
        else:
            self.right = (self.right + 1) % self.size

        return x

    def append_left(self, x):
        if self.is_full():
            raise Exception('Overflow')

        self.left += 1

        if self.left == self.size:
            self.left = 0

        self.elements[self.left] = x

    def shift(self):
        if self.is_empty():
            raise Exception('Underflow')

        if self.left == -1:
            self.left = self.size - 1

        x = self.elements[self.left]

        if self.left == self.right:
            self.left = -1
            self.right = self.size
        else:
            self.left -= 1

            if self.left == -1:
                self.left = self.size - 1

        return x
