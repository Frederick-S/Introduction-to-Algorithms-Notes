def iterative_binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_value = numbers[middle]

        if middle_value < target:
            low = middle + 1
        elif middle_value > target:
            high = middle - 1
        else:
            return True

    return False
