import unittest
from src.chapter_09.weighted_median import weighted_median


class TestWeightedMedian(unittest.TestCase):
    def test_weighted_median(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        weights = [0.1, 0.35, 0.1, 0.05, 0.15, 0.05, 0.2]
        elements = create_elements(values, weights)
        self.assertEqual(3, weighted_median(elements))

        values = [0.1 for i in range(10)]
        weights = [0.1 for i in range(10)]
        elements = create_elements(values, weights)
        self.assertEqual(0.1, weighted_median(elements))


def create_elements(values, weights):
    elements = []

    for i, value in enumerate(values):
        elements.append({
            'value': value,
            'weight': weights[i]
        })

    return elements


if __name__ == '__main__':
    unittest.main()
