import unittest
from src.chapter_08.water_jugs import water_jugs


class TestWaterJugs(unittest.TestCase):
    def test_water_jugs(self):
        red_jugs = []
        blue_jugs = []
        jug_pairs = water_jugs(red_jugs, blue_jugs)
        self.assertSequenceEqual([], jug_pairs)

        red_jugs = [1]
        blue_jugs = [1]
        jug_pairs = water_jugs(red_jugs, blue_jugs)
        self.assertSequenceEqual([[1, 1]], jug_pairs)

        red_jugs = [7, 6, 1, 3, 9, 2, 5]
        blue_jugs = [5, 1, 3, 6, 7, 2, 9]
        jug_pairs = water_jugs(red_jugs, blue_jugs)
        jug_pairs.sort()
        self.assertSequenceEqual(
            [[1, 1], [2, 2], [3, 3], [5, 5],
                [6, 6], [7, 7], [9, 9]], jug_pairs)

        red_jugs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        blue_jugs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        jug_pairs = water_jugs(red_jugs, blue_jugs)
        jug_pairs.sort()
        self.assertSequenceEqual(
            [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]], jug_pairs)


if __name__ == '__main__':
    unittest.main()
