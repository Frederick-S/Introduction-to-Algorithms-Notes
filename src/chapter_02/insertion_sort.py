def insertion_sort(numbers):
    length = len(numbers)

    for i in range(1, length):
        j = i - 1
        key = numbers[i]

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key
