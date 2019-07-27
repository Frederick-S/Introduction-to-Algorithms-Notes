k = 255


def sorting_variable_length_strings(strings):
    length = len(strings)

    if length == 0:
        return strings

    return sorting_variable_length_strings_internal(strings, 0)


def sorting_variable_length_strings_internal(strings, string_start_index):
    length = len(strings)

    if length == 0:
        return strings

    if string_start_index >= max(map(len, strings)):
        return strings

    strings_by_start_letter = [[] for i in range(k + 1)]

    strings = counting_sort(strings, string_start_index)

    for i in range(length):
        strings_by_start_letter[get_digit(
            strings[i], string_start_index)].append(strings[i])

    for i in range(k + 1):
        strings_by_start_letter[i] = sorting_variable_length_strings_internal(
            strings_by_start_letter[i], string_start_index + 1)

    result = []

    for i in range(k + 1):
        result += strings_by_start_letter[i]

    return result


def counting_sort(strings, index):
    length = len(strings)

    if length == 0:
        return strings

    c = [0] * (k + 1)
    b = [''] * length

    for i in range(length):
        c[get_digit(strings[i], index)] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    for i in range(length - 1, -1, -1):
        b[c[get_digit(strings[i], index)] - 1] = strings[i]
        c[get_digit(strings[i], index)] -= 1

    return b


def get_digit(string, i):
    if i >= len(string):
        return 0

    return ord(string[i])
