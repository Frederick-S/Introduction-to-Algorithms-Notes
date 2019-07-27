def bubble_sort(numbers):
    length = len(numbers)

    for i in range(0, length - 1):
        exchanged = False

        for j in range(length - 1, i, -1):
            if numbers[j] < numbers[j - 1]:
                exchanged = True
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]

        if not exchanged:
            break
