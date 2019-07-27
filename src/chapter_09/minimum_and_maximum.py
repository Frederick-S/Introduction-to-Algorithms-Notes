def minimum_and_maximum(numbers):
    length = len(numbers)

    if length == 0:
        return []

    start = 0
    minimum = 0
    maximum = 0

    if length % 2 == 0:
        if numbers[0] < numbers[1]:
            minimum, maximum = numbers[0], numbers[1]
        else:
            minimum, maximum = numbers[1], numbers[0]

        start = 2
    else:
        start = 1
        minimum = numbers[0]
        maximum = numbers[0]

    for i in range(start, length, 2):
        if numbers[i] < numbers[i + 1]:
            maximum = max(maximum, numbers[i + 1])
            minimum = min(minimum, numbers[i])
        else:
            maximum = max(maximum, numbers[i])
            minimum = min(minimum, numbers[i + 1])

    return [minimum, maximum]
