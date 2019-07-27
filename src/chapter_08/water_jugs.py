import random


def water_jugs(red_jugs, blue_jugs):
    jug_pairs = []

    water_jugs_internal(red_jugs, blue_jugs, jug_pairs)

    return jug_pairs


def water_jugs_internal(red_jugs, blue_jugs, jug_pairs):
    length = len(red_jugs)

    if length == 0:
        return

    r = random.randint(0, length - 1)
    pivot = red_jugs[r]

    red_jugs_smaller_than_pivot = []
    red_jugs_larger_than_pivot = []
    blue_jugs_smaller_than_pivot = []
    blue_jugs_larger_than_pivot = []

    for i in range(length):
        red_jug = red_jugs[i]
        blue_jug = blue_jugs[i]

        if red_jug < pivot:
            red_jugs_smaller_than_pivot.append(red_jug)
        elif red_jug > pivot:
            red_jugs_larger_than_pivot.append(red_jug)

        if blue_jug < pivot:
            blue_jugs_smaller_than_pivot.append(blue_jug)
        elif blue_jug > pivot:
            blue_jugs_larger_than_pivot.append(blue_jug)
        else:
            jug_pairs.append([pivot, pivot])

    water_jugs_internal(
        red_jugs_smaller_than_pivot, blue_jugs_smaller_than_pivot, jug_pairs)
    water_jugs_internal(
        red_jugs_larger_than_pivot, blue_jugs_larger_than_pivot, jug_pairs)
