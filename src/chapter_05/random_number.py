import math
import random


def random_number(a, b):
    bits = math.ceil(math.log2(b - a + 1))

    while True:
        number = random_binay(bits)

        if a + number <= b:
            return a + number


def random_binay(bits):
    number = 0

    for _ in range(bits):
        number = number * 2 + random.randint(0, 1)

    return number
