import unittest
from src.chapter_08.sorting_variable_length_strings \
    import sorting_variable_length_strings


class TestSortingVariableLengthStrings(unittest.TestCase):
    def test_sorting_variable_length_strings(self):
        strings = []
        sorting_variable_length_strings(strings)
        self.assertSequenceEqual([], strings)

        strings = ['cba', 'abc', 'a', 'b']
        self.assertSequenceEqual(
            ['a', 'abc', 'b', 'cba'], sorting_variable_length_strings(strings))

        strings = ['a', 'a', 'a', 'a', 'a']
        self.assertSequenceEqual(
            ['a', 'a', 'a', 'a', 'a'],
            sorting_variable_length_strings(strings))

        strings = ['abcedf', 'a', 'bcadefk', 'e', 'jlmk']
        self.assertSequenceEqual(
            ['a', 'abcedf', 'bcadefk', 'e', 'jlmk'],
            sorting_variable_length_strings(strings))


if __name__ == '__main__':
    unittest.main()
