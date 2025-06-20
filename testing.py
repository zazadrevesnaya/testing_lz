import unittest
from testiruemaia import Equation as eq


#тестирующая часть
class TestRoundSquare(unittest.TestCase):
    def test_integer_positive_number(self):
        self.assertEqual(eq(2, 5 ,7), 5.851315793834051)

    def test_zero_number(self):
        self.assertEqual(eq(0, 0 ,0), "ValueError:Parameter c must be greater than 0")
    
    def test_float_positive_number(self):
        self.assertEqual(eq(0.1, 0.2, 0.4), 0.7343194450616334)

    def test_error_input(self):
        self.assertEqual(eq("asdsa", "flmmf" ,"rhrfh"), "TypeError")
        self.assertEqual(eq("", "", ""), "TypeError")
        self.assertEqual(eq("10**-9","10**-9","10**-9"), "TypeError")

if __name__ == "__main__":
    unittest.main()

