def recursive_binary_search(numbers, target):
    return recursive_binary_search_internal(numbers, target,
                                            0, len(numbers) - 1)


def recursive_binary_search_internal(numbers, target, low, high):
    if low <= high:
        middle = (low + high) // 2
        middle_value = numbers[middle]

        if middle_value < target:
            return recursive_binary_search_internal(numbers, target,
                                                    middle + 1, high)
        elif middle_value > target:
            return recursive_binary_search_internal(numbers, target,
                                                    low, middle - 1)
        else:
            return True

    return False
