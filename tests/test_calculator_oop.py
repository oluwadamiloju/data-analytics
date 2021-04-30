import unittest
from calculator_oop import Calculator


class CalculatorOOPTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(Calculator.add(3, 6), 9)
        self.assertEqual(Calculator.add(-8, -2), -10)
        self.assertEqual(Calculator.add(7087, 87766), 7087 + 87766)

    def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(3, 6), int)
        self.assertIsInstance(Calculator.add(-8, -2), int)
        self.assertIsInstance(Calculator.add(7087, 87766), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.add('fasolatido', 2)
            Calculator.add('sarah', 7.0)

    def test_sub_results(self):
        self.assertEqual(Calculator.sub(10, 12), -2)
        self.assertEqual(Calculator.sub(19128320, 23689), 19128320 - 23689)
        self.assertEqual(Calculator.sub(-6, -4), -2)

    def test_sub_results_type(self):
        self.assertIsInstance(Calculator.sub(10, 12), int)
        self.assertIsInstance(Calculator.sub(19128320, 23689), int)
        self.assertIsInstance(Calculator.sub(-6, -4), int)

    def test_sub_results_non_type(self):
        with self.assertRaises(TypeError):
            Calculator.sub('hello world', 575)

    def test_div_results(self):
        self.assertEqual(Calculator.div(10, 4), 2)
        self.assertEqual(Calculator.div(21, 3), 7)
        self.assertEqual(Calculator.div(-1928129, 7), -1928129 // 7)

    def test_div_results_type(self):
        self.assertIsInstance(Calculator.div(10, 4), int)
        self.assertIsInstance(Calculator.div(21, 3), int)
        self.assertIsInstance(Calculator.div(-1928129, 7), int)

    def test_div_results_non_type(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.div(123, 0)

        with self.assertRaises(TypeError):
            Calculator.div(47887, 'tutu')

    def test_mul_results(self):
        self.assertEqual(Calculator.mul(2, 6), 12)
        self.assertEqual(Calculator.mul(74, 35671), 74 * 35671)
        self.assertEqual(Calculator.mul(-2348, 3930), -2348 * 3930)

    def test_mul_results_type(self):
        self.assertIsInstance(Calculator.mul(2, 6), int)
        self.assertIsInstance(Calculator.mul(74, 35671), int)
        self.assertIsInstance(Calculator.mul(-2348, 3930), int)

    def test_mul_results_non_type(self):
        with self.assertRaises(TypeError):
            Calculator.mul("234", "higher")


if __name__ == '__main__':
    unittest.main()
