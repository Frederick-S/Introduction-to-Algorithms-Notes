import math


def radix_sort(numbers):
    length = len(numbers)

    if length == 0:
        return numbers

    d = get_number_length(max(numbers))

    for i in range(1, d + 1):
        sort_on_digit(numbers, i)


def sort_on_digit(numbers, i):
    k = 9
    c = [0] * (k + 1)
    a = numbers[:]
    digits = []

    for j in range(0, len(numbers)):
        digit = get_digit(a[j], i)
        digits.append(digit)
        c[digit] += 1

    for j in range(1, k + 1):
        c[j] += c[j - 1]

    for j in range(len(numbers) - 1, -1, -1):
        digit = digits[j]
        numbers[c[digit] - 1] = a[j]
        c[digit] -= 1


def get_digit(number, i):
    if i > get_number_length(number):
        return 0
    else:
        return int(str(number)[-i])


def get_number_length(number):
    if number == 0:
        return 1
    else:
        return int(math.log(number, 10)) + 1
