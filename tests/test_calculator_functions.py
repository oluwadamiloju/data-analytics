import unittest
from calculator_functions import add
from calculator_functions import sub
from calculator_functions import div
from calculator_functions import mul


class CalculatorFunctionsTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(3, 6), 9)
        self.assertEqual(add(-8, -2), -10)
        self.assertEqual(add(7087, 87766), 7087 + 87766)

    def test_add_result_type(self):
        self.assertIsInstance(add(3, 6), int)
        self.assertIsInstance(add(-8, -2), int)
        self.assertIsInstance(add(7087, 87766), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add('fasolatido', 2)
            add('sarah', 7.0)

    def test_sub_results(self):
        self.assertEqual(sub(10, 12), -2)
        self.assertEqual(sub(19128320, 23689), 19128320 - 23689)
        self.assertEqual(sub(-6, -4), -2)

    def test_sub_results_type(self):
        self.assertIsInstance(sub(10, 12), int)
        self.assertIsInstance(sub(19128320, 23689), int)
        self.assertIsInstance(sub(-6, -4), int)

    def test_sub_results_non_type(self):
        with self.assertRaises(TypeError):
            sub('hello world', 575)

    def test_div_results(self):
        self.assertEqual(div(10, 4), 2)
        self.assertEqual(div(21, 3), 7)
        self.assertEqual(div(-1928129, 7), -1928129 // 7)

    def test_div_results_type(self):
        self.assertIsInstance(div(10, 4), int)
        self.assertIsInstance(div(21, 3), int)
        self.assertIsInstance(div(-1928129, 7), int)

    def test_div_results_non_type(self):
        with self.assertRaises(ZeroDivisionError):
            div(123, 0)

        with self.assertRaises(TypeError):
            div(47887, 'tutu')

    def test_mul_results(self):
        self.assertEqual(mul(2, 6), 12)
        self.assertEqual(mul(74, 35671), 74 * 35671)
        self.assertEqual(mul(-2348, 3930), -2348 * 3930)

    def test_mul_results_type(self):
        self.assertIsInstance(mul(2, 6), int)
        self.assertIsInstance(mul(74, 35671), int)
        self.assertIsInstance(mul(-2348, 3930), int)

    def test_mul_results_non_type(self):
        with self.assertRaises(TypeError):
            mul("234", "higher")
            # try:
            #     mul("234", "higher")
            # raise TypeError:


if __name__ == '__main__':
    unittest.main()
