import unittest
import calculator
from calculator import minus, times, divide


class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.add(4, 9), 13)

    def test_addition_negative(self):
        self.assertEqual(calculator.add(-2, -4), -6)

    def test_addition_zero(self):
        self.assertEqual(calculator.add(0, 0), 0)

    '''
    Do not call the function inside assertRaises
    '''
    # def test_addition_string(self):
    #     with self.assertRaises(ValueError):
    #         calculator.convert_to_int("cat")


class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(minus(9, 4), 5)

    def test_subtraction_zero(self):
        self.assertEqual(minus(6, 0), 6)
    
    def test_subtraction_negative(self):
        self.assertEqual(minus(-6, -10), 4)



class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(times(3, 2), 6)

    def test_multiplication_negative(self):
        self.assertEqual(times(-5, 2), -10)

    def test_multiplication_zero(self):
        self.assertEqual(times(8, 0), 0)


class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(divide(6, 2), 3)
    
    def test_division_negative(self):
        self.assertEqual(divide(-10, -2), 5.0)

    def test_division_zero(self):
        self.assertEqual(divide(10, 0), "Cannot divide by zero")


if __name__ == '__main__':
    unittest.main()