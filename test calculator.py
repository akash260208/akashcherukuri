"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        
    def test_multiplication(self)
        assert  6 == calculator.multication(2,3)
      
    def test_division(self)
        assert 8 == calculator.division(4,2)
