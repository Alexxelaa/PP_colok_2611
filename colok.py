import unittest

class Factorials:
    def __init__(self, n):
        if not isinstance(n, int) or n < 1:
            raise ValueError("Должно быть целое число большее 0")
        self.n = n
        self.factorials = self.calculate_factorials()

    def calculate_factorials(self):
        result = []
        factorial = 1
        for i in range(1, self.n + 1):
            factorial *= i
            result.append(factorial)
        return result

    def get_factorials(self):
        return self.factorials


class TestFactorials(unittest.TestCase):
    def test_valid_input(self):
        f = Factorials(5)
        self.assertEqual(f.get_factorials(), [1, 2, 6, 24, 120])

    def test_single_factorial(self):
        f = Factorials(1)
        self.assertEqual(f.get_factorials(), [1])

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            Factorials(-5)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            Factorials(0)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(ValueError):
            Factorials(3.5)

    def test_large_input(self):
        f = Factorials(10)
        expected = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        self.assertEqual(f.get_factorials(), expected)


x = Factorials(10)
print(x.get_factorials())