def selection_sort(numbers):
    length = len(numbers)

    for i in range(length):
        min_index = i

        for j in range(i + 1, length):
            if numbers[min_index] > numbers[j]:
                min_index = j

        if min_index != i:
            numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
