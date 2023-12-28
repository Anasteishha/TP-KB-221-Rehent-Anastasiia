import unittest
from unittest.mock import patch
class TestCalculator(unittest.TestCase):

    def test_is_number(self):
        self.assertTrue(self.calc.is_number('123'))
        self.assertFalse(self.calc.is_number('12a'))

    def test_get_priority(self):
        self.assertEqual(self.calc.get_priority('+'), 0)
        self.assertEqual(self.calc.get_priority('*'), 1)
        self.assertEqual(self.calc.get_priority('^'), 2)

    def test_to_to_reverse(self):
        self.assertEqual(self.calc.to_to_reverse('3+4*2/(1-5)^2'), ['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+'])

    @patch('your_module.Calculator.calculate', return_value=3.5)
    def test_calculate(self, mock_calculate):
        result = self.calc.calculate(['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+'])
        self.assertEqual(result, 3.5)
        mock_calculate.assert_called_once_with(['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+'])

if __name__ == '__main__':
    unittest.main()
