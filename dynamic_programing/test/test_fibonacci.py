import unittest
from math import pi

from dynamic_programing.src.fibonacci_dynamic import fibonacci, dynamic_fibonacci


class TestFibonacci(unittest.TestCase):

    def test_invalid_input(self):
        self.assertRaises(ValueError, fibonacci, -1)
        self.assertRaises(ValueError, dynamic_fibonacci, -1, lookup=[None] * 101)
        self.assertRaises(TypeError, fibonacci, pi)
        self.assertRaises(TypeError, dynamic_fibonacci, pi, lookup=[None] * 101)
        self.assertRaises(TypeError, dynamic_fibonacci, 0, {})

    def test_fib_0(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(dynamic_fibonacci(0, lookup=[None] * 101), 0)

    def test_fib_1(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(dynamic_fibonacci(1, lookup=[None] * 101), 1)

    def test_fib_2(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(dynamic_fibonacci(2, lookup=[None] * 101), 1)

    def test_fib_3(self):
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(dynamic_fibonacci(3, lookup=[None] * 101), 2)

    def test_fib_4(self):
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(dynamic_fibonacci(4, lookup=[None] * 101), 3)

    def test_fib_5(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(dynamic_fibonacci(5, lookup=[None] * 101), 5)

    def test_fib_6(self):
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(dynamic_fibonacci(6, lookup=[None] * 101), 8)

    def test_fib_max(self):
        self.assertEqual(fibonacci(34), 5702887)
        self.assertEqual(dynamic_fibonacci(99, lookup=[None] * 101), 218922995834555169026)

    def test_fib_big_int(self):
        self.assertRaises(ValueError, fibonacci, 35)
        self.assertRaises(ValueError, dynamic_fibonacci, 100, lookup=[None] * 101)


if __name__ == '__main__':
    unittest.main()
