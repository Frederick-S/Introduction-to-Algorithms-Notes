# Sorting n records, each record has the value 0 or 1
def sorting_in_place_in_linear_time(numbers):
    i = 0
    j = len(numbers) - 1

    while i < j:
        while numbers[i] == 0:
            i += 1

        while numbers[j] == 1:
            j -= 1

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
