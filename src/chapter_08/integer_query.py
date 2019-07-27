class IntegerQuery(object):
    def __init__(self, numbers):
        assert len(numbers) > 0

        self.c = []
        self.preprocess(numbers)

    def preprocess(self, numbers):
        k = max(numbers)
        self.c = [0] * (k + 1)

        for i in range(0, len(numbers)):
            self.c[numbers[i]] += 1

        for i in range(1, k + 1):
            self.c[i] += self.c[i - 1]

    def query(self, a, b):
        assert 0 <= a <= b

        if a - 1 < 0:
            return self.c[b]

        return self.c[b] - self.c[a - 1]
