import unittest
from calculator.calculator_class import Calculator


class CalculatorClassTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculate = self.calculator.calculate

    def test_should_sum_positive_numbers(self):
        self.assertEqual(self.calculate('2+2'), '4')

    def test_should_sum_negative_numbers(self):
        self.assertEqual(self.calculate('-2+-2'), '-4')

    def test_should_sum_negative_and_positive_numbers(self):
        self.assertEqual(self.calculate('-2+2'), '0')

    def test_should_calculate_complex_equation(self):
        self.assertEqual(
            self.calculate(
                '((2+(2*(2-((5/5)+32))))/2)+1+(1*(2^(2+(5.5-5.1))))'
            ),
            '-23.72196835690842'
        )

    def test_should_raise_overflowerror(self):
        with self.assertRaises(OverflowError):
            self.calculate('9^9^9^9')

    def test_should_raise_syntaxerror_for_empty_parentheses(self):
        with self.assertRaises(SyntaxError):
            self.calculate('()()')

    def test_should_raise_syntaxerror_if_not_an_equation(self):
        with self.assertRaises(SyntaxError):
            self.calculate('print')

    def test_should_raise_syntaxerror_for_parentheses_not_matching(self):
        with self.assertRaises(SyntaxError):
            self.calculate('(2+2))')
