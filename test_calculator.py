import unittest
import calculator


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
        pass


class TestMultiplication(unittest.TestCase):
    pass


class TestDivision(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()