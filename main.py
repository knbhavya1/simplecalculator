import unittest
class calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x-y

    def mul(self, x, y):
        return x*y

class testCalci(unittest.TestCase):
    def test_add(self):
        self.calc = calculator()
        result=self.calc.add(4, 5)
        expected=9
        self.assertEqual(result, expected)

    def test_sub(self):
        self.calc = calculator()
        result = self.calc.sub(8, 4)
        expected=4
        self.assertEqual(result, expected)

    def test_mul(self):
        self.calc = calculator()
        result = self.calc.mul(4, 4)
        expected=16
        self.assertEqual(result, expected)

unittest.main(argv = [''],verbosity=2, exit=False)





