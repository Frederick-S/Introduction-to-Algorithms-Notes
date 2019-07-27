def counting_sort_in_place(numbers):
    length = len(numbers)

    if length == 0:
        return numbers

    k = max(numbers)
    c = [0] * (k + 1)

    for i in range(0, length):
        c[numbers[i]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    i = 0

    while i <= length - 1:
        number = numbers[i]
        position = c[number] - 1

        if i >= position:
            i += 1
        elif number != numbers[position]:
            numbers[i], numbers[position] = numbers[position], numbers[i]
            c[number] -= 1
        else:
            c[number] -= 1
