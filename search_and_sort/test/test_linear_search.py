from search_and_sort.src.linear_search import *

import unittest


class TestLinearSearch(unittest.TestCase):

    def test_zero_element(self):
        array = []
        value = 8
        self.assertEqual(linear_search(array, value), -1)

    def test_search_one_element(self):
        array = [0]
        value = 0
        self.assertEqual(linear_search(array, value), 0)
        value = 1
        self.assertEqual(linear_search(array, value), -1)
        array = [5]
        self.assertEqual(linear_search(array, value), -1)
        value = 5
        self.assertEqual(linear_search(array, value), 0)

    def test_two_elements(self):
        array = [2, 8]
        value = 2
        self.assertEqual(linear_search(array, value), 0)
        value = 8
        self.assertEqual(linear_search(array, value), 1)
        value = 9
        self.assertEqual(linear_search(array, value), -1)

    def test_three_elements(self):
        array = [2, 8, 9]
        value = 2
        self.assertEqual(linear_search(array, value), 0)
        value = 8
        self.assertEqual(linear_search(array, value), 1)
        value = 9
        self.assertEqual(linear_search(array, value), 2)
        value = 34
        self.assertEqual(linear_search(array, value), -1)

    def test_four_elements(self):
        array = [2, 8, 9, 34]
        value = 2
        self.assertEqual(linear_search(array, value), 0)
        value = 8
        self.assertEqual(linear_search(array, value), 1)
        value = 9
        self.assertEqual(linear_search(array, value), 2)
        value = 34
        self.assertEqual(linear_search(array, value), 3)
        value = 'str'
        self.assertEqual(linear_search(array, value), -1)

    def test_five_mixed_typed_elements(self):
        array = [2, '9', float(34.8), True, (1, 4)]
        value = 2
        self.assertEqual(linear_search(array, value), 0)
        value = '9'
        self.assertEqual(linear_search(array, value), 1)
        value = 34.8
        self.assertEqual(linear_search(array, value), 2)
        value = True
        self.assertEqual(linear_search(array, value), 3)
        value = (1, 4)
        self.assertEqual(linear_search(array, value), 4)
        value = 3
        self.assertEqual(linear_search(array, value), -1)


if __name__ == '__main__':
    unittest.main()
