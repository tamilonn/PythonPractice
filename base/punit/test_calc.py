import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(100, 50)
        self.assertEqual(result, 149)

    def test_substract(self):
        result = calc.substract(100, 50)
        self.assertEqual(result, 50)

    def test_multiply(self):
        result = calc.multiply(100, 50)
        self.assertEqual(result, 5000)

    def test_divide(self):
        result = calc.divide(100, 50)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()